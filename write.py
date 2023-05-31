import os
import sys
import shutil
import tarfile

from state_data import generate_ros_data
from urllib import request

class ArchiveNotExtracted(Exception):
    pass

def find_by_name(name, path):
    for root, _, files in os.walk(path):
        for i in files:
            if name in i:
                return os.path.join(root, i)

def write_state(state):
    
    if os.path.exists("./archive"):
        shutil.rmtree("./archive")

    #open the tarball and extract the pmlogger file
    while True:
        try:
            with tarfile.open('archive.tar.gz', 'r') as archive:
                before, after = os.listdir(), []
                archive.extractall(numeric_owner=True)
                after = os.listdir()
                extracted_dir = [i for i in after if i not in before][0]
                break
        except FileNotFoundError:
            print("Archive not found!")
            print(" Downloading a RHEL8 Idling archive.")
            remote_url = "https://github.com/RedHatInsights/ros-backend/raw/main/sample-files/rhel8/rhel8-insights-ip-aws-idle.tar.gz"
            local_file = "archive.tar.gz"
            request.urlretrieve(remote_url, local_file)

    #going inside of the extracted directory
    PATH = find_by_name("pmlogsummary", f"{extracted_dir}")

    if PATH:
        #writing state to the extracted file
        with open(PATH, 'w+') as pmlogger:
            state_data = generate_ros_data(state)
            pmlogger.write(state_data)
        
        with tarfile.open(f'ros-aws-{state}.tar.gz', mode='w:gz') as archive:
            archive.add(f"./{extracted_dir}", recursive=True)

    # #cleanups
    shutil.rmtree(extracted_dir)
    shutil.rmtree("__pycache__")

if __name__ == "__main__":
    args = sys.argv
    try:
        write_state(args[1])
    except IndexError:
        print("No state provided. Please pass a state in commandline argument or make use of MAKEFILE")
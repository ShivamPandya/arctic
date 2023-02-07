import tarfile, shutil, os
from state_data import generate_ros_data
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
    with tarfile.open('archive.tar.gz', 'r') as archive:
        archive.extractall(numeric_owner=True)

    PATH = find_by_name("pmlogsummary", "archive")

    #writing state to the extracted file
    with open(PATH, 'w+') as pmlogger:
        state_data = generate_ros_data(state)
        pmlogger.write(state_data)
    
    with tarfile.open('archive.tar.gz', mode='w:gz') as archive:
        archive.add("archive", recursive=True)

    #cleanups
    if os.path.exists("./archive"):
        shutil.rmtree("./archive")
        shutil.rmtree("__pycache__")
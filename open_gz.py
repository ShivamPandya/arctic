import tarfile, shutil, os
from state_data import generate_ros_data

FILE_PATH = "./archive/insights-ip-aws/insights-ip-172-31-28-69.ec2.internal-20211118062240/data/insights_commands/"
FILE_NAME = "pmlogsummary_.var.log.pcp.pmlogger.ros.20211117.index_mem.util.used_mem.physmem_kernel.all.cpu.user_kernel.all.cpu.sys_kernel.all.cpu.nice_kernel.all.cpu.steal_kernel.all.cpu.idle_disk.all.total_mem.util.cached_mem.util.bufmem_mem.util.free_kernel.all.cpu"

def write_state(state):
    
    if os.path.exists("./archive"):
        shutil.rmtree("./archive")

    #open the tarball and extract the pmlogger file
    with tarfile.open('archive.tar.gz', 'r') as archive:
        archive.extractall(numeric_owner=True)

    #writing state to the extracted file
    with open(FILE_PATH+FILE_NAME, 'w+') as pmlogger:
        state_data = generate_ros_data(state)
        pmlogger.write(state_data)
    
    with tarfile.open('archive.tar.gz', mode='w:gz') as archive:
        archive.add("archive", recursive=True)

    if os.path.exists("./archive"):
        shutil.rmtree("./archive")

write_state("idling")

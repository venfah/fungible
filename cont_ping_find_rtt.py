
'''
This script is to run ping continuously and get rtt (round trip time for ping)
so that we can average out rtt value
'''

from subprocess import CalledProcessError, check_output
from time import time, mktime, strptime, ctime

def run(cmd):
    print("{}: {}".format(ctime(), cmd))
    out = ''
    try:
        out = check_output(cmd, shell=True)
    except CalledProcessError as e:
        out = ""
    return out



if __name__ == '__main__':
    total = 100
    remote_numa_cpus = '0-7,16-23'
    same_numa_cpus = '8-15,24-31'
    source_if = 'enp216s0'
    target_ip = '15.1.15.2'
    ping_count = 100

    remote_numa_file = 'remote_numa_file'
    same_numa_file = 'same_numa_file'
    for each in range(total):
        print ("Iteration no {}".format(each + 1))
        if each == 0:
             run("taskset -c {} ping -I {} -c {} {} -i 0.2| grep ^rtt > {}".format(remote_numa_cpus, source_if, ping_count, target_ip, remote_numa_file))
             run("taskset -c {} ping -I {} -c {} {} -i 0.2| grep ^rtt > {}".format(same_numa_cpus, source_if, ping_count, target_ip, same_numa_file))
        else:
             run("taskset -c {} ping -I {} -c {} {} -i 0.2| grep ^rtt >> {}".format(remote_numa_cpus, source_if, ping_count, target_ip, remote_numa_file))
             run("taskset -c {} ping -I {} -c {} {} -i 0.2| grep ^rtt >> {}".format(same_numa_cpus, source_if, ping_count, target_ip, same_numa_file))

        

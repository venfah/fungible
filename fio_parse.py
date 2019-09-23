from subprocess import CalledProcessError, check_output
from time import ctime
import json
import sys


def run(cmd):
    print("{}: {}".format(ctime(), cmd))
    try:
        out = check_output(cmd, shell=True)
    except CalledProcessError as e:
        out = ""
    return out


if __name__ == '__main__':

    if len(sys.argv) != 5:
        help_cmd = '''
        HOWTO Run:
            python {} iotype cpus_allowed numjobs iodepth
        Help:
            iotype: randread/randwrite
            cpus_allowed: 0-7
            num_jobs: 1/32
            ipdepth: 1/32
        Example:
            python {} randread 0-7 1 1
            python {} randwrite 8-15,24-31 16 32
        '''.format(sys.argv[0], sys.argv[0], sys.argv[0])
        print (help_cmd)
        sys.exit(1)

    io_rw = sys.argv[1]
    io_cpu = sys.argv[2]
    io_nj = sys.argv[3]
    io_qd = sys.argv[4]

    cmd = "fio --filename=/dev/nvme0n1 --time_based --fill_device=1 --rw={} --prio=0 --bs=4k --direct=1 --cpus_allowed={} --cpus_allowed_policy=split --numjobs={} --ioengine=libaio --iodepth={} --name=rand_read_perf --runtime=60 --group_reporting --output-format=json".format(io_rw, io_cpu, io_nj, io_qd)

    output = run(cmd)
    output_json = json.loads(output)

    if sys.argv[1].endswith('read'):
        print ("read-iops: {}".format(output_json['jobs'][0]['read']['iops']))
        print ("sub latency: {} us".format(int(output_json['jobs'][0]['read']['slat_ns']['mean'])/1000.0))
        print ("comp latency: {} us".format(int(output_json['jobs'][0]['read']['clat_ns']['mean'])/1000.0))
        print ("cumulative latency: {} us".format(int(output_json['jobs'][0]['read']['lat_ns']['mean'])/1000.0))
    elif sys.argv[1].endswith('write'):
        print ("write-iops: {}".format(output_json['jobs'][0]['write']['iops']))
        print ("sub latency: {} us".format(int(output_json['jobs'][0]['write']['slat_ns']['mean'])/1000.0))
        print ("comp latency: {} us".format(int(output_json['jobs'][0]['write']['clat_ns']['mean'])/1000.0))
        print ("cumulative latency: {} us".format(int(output_json['jobs'][0]['write']['lat_ns']['mean'])/1000.0))
    elif sys.argv[1].endswith('trim'):
        print ("trim-iops: {}".format(output_json['jobs'][0]['trim']['iops']))
        print ("sub latency: {} us".format(int(output_json['jobs'][0]['trim']['slat_ns']['mean'])/1000.0))
        print ("comp latency: {} us".format(int(output_json['jobs'][0]['trim']['clat_ns']['mean'])/1000.0))
        print ("cumulative latency: {} us".format(int(output_json['jobs'][0]['trim']['lat_ns']['mean'])/1000.0))
    else:
        print ("--rw={} check for right parsing".format(sys.argv[1]))



'''
OUTPUT

[localadmin@cab02-qa-11 nazir]$ python fio_parse.py 

        HOWTO Run:
            python fio_parse.py iotype cpus_allowed numjobs iodepth
        Help:
            iotype: randread/randwrite
            cpus_allowed: 0-7
            num_jobs: 1/32
            ipdepth: 1/32
        Example:
            python fio_parse.py randread 0-7 1 1
            python fio_parse.py randwrite 8-15,24-31 16 32
        
[localadmin@cab02-qa-11 nazir]$ 

[root@cab02-qa-11 nazir]# python fio_parse.py randread 0-7 16 64
Mon Sep 23 05:56:28 2019: fio --filename=/dev/nvme0n1 --time_based --fill_device=1 --rw=randread --prio=0 --bs=4k 
--direct=1 --cpus_allowed=0-7 --cpus_allowed_policy=split --numjobs=16 --ioengine=libaio --iodepth=64 
--name=rand_read_perf --runtime=60 --group_reporting --output-format=json
read-iops: 524411.643139
sub latency: 28.076 us
comp latency: 1923.569 us
cumulative latency: 1951.792 us
[root@cab02-qa-11 nazir]#


'''

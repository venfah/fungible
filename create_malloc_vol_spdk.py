'''
HUGEMEM=8096 ~/spdk/scripts/setup.sh then run below script

This below script is to create 4 amalloc volumes
and create transport then create nqn for all volumes then listen from an nqn subsystem
'''

sudo python3 rpc.py bdev_malloc_create -b Malloc0 256 4096
sleep 5
sudo python3 rpc.py bdev_malloc_create -b Malloc1 256 4096
sleep 5
sudo python3 rpc.py bdev_malloc_create -b Malloc2 256 4096
sleep 5
sudo python3 rpc.py bdev_malloc_create -b Malloc3 256 4096
sleep 5


sudo python3 rpc.py nvmf_create_transport -t TCP -u 8192 -p 32
sleep 2
sudo python3 rpc.py nvmf_subsystem_create nqn.2016-06.io.spdk:cnode1 -a -s SPDK00000000000001
sleep 2

sudo python3 rpc.py nvmf_subsystem_add_ns nqn.2016-06.io.spdk:cnode1 Malloc0
sleep 2
sudo python3 rpc.py nvmf_subsystem_add_ns nqn.2016-06.io.spdk:cnode1 Malloc1
sleep 2
sudo python3 rpc.py nvmf_subsystem_add_ns nqn.2016-06.io.spdk:cnode1 Malloc2
sleep 2
sudo python3 rpc.py nvmf_subsystem_add_ns nqn.2016-06.io.spdk:cnode1 Malloc3
sleep 2

sudo python3 rpc.py nvmf_subsystem_add_listener nqn.2016-06.io.spdk:cnode1 -t tcp -a 15.1.15.2 -s 4420
~                                                                                                        

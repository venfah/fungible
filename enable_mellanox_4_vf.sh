mst status
mst start
mst status
mlxconfig -d /dev/mst/mt4119_pciconf0 q
sleep 5
echo 4 >  /sys/class/infiniband/mlx5_0/device/mlx5_num_vfs

echo 0000:d8:00.1 > /sys/bus/pci/drivers/mlx5_core/unbind
sleep 2
ip link set enp216s0 vf 0 mac d2:2a:82:43:82:52
sleep 2
echo 0000:d8:00.1 > /sys/bus/pci/drivers/mlx5_core/bind
sleep 2

echo 0000:d8:00.2 > /sys/bus/pci/drivers/mlx5_core/unbind
sleep 2
ip link set enp216s0 vf 1 mac d2:2a:82:43:83:53
sleep 2
echo 0000:d8:00.2 > /sys/bus/pci/drivers/mlx5_core/bind
sleep 2

echo 0000:d8:00.3 > /sys/bus/pci/drivers/mlx5_core/unbind
sleep 2
ip link set enp216s0 vf 2 mac d2:2a:82:43:84:54
sleep 2
echo 0000:d8:00.3 > /sys/bus/pci/drivers/mlx5_core/bind
sleep 2

echo 0000:d8:00.4 > /sys/bus/pci/drivers/mlx5_core/unbind
sleep 2
ip link set enp216s0 vf 3 mac d2:2a:82:43:85:55
sleep 2
echo 0000:d8:00.4 > /sys/bus/pci/drivers/mlx5_core/bind
sleep 2
~                             

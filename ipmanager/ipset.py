import psutil
import time
import subprocess
import socket

def get_nic_list():
    interfaces = psutil.net_if_stats().keys()
    return list(interfaces)

def get_ipv4_by_interface(interface):
    net_addrs = psutil.net_if_addrs()
    if interface in net_addrs:
        for addr in net_addrs[interface]:
            if addr.family == psutil.AF_INET:
                return addr.address
    return None

def monitor_nic_sent_bytes(interface, interval):
    stats = psutil.net_io_counters(pernic=True)
    while True:
        sent_bytes = stats[interface].bytes_sent  
        recv_bytes = stats[interface].bytes_recv
        print(f"Sent Bytes on {interface}: {sent_bytes}")
        print(f"Recv Bytes on {interface}: {recv_bytes}")
        time.sleep(interval)

def print_nicinfo():
    net_ifs = psutil.net_if_addrs()

    for name, addresses in net_ifs.items():
        print("Name: ", name)
        for addr in addresses:
            # print(addr)
            if addr.family == socket.AF_INET:
                print("IPV4: ", addr.address)
                print("Netmask:", addr.netmask)
            elif addr.family == psutil.AF_LINK:
                print("MAC: ", addr.address)   
        print()

def set_nic(interface, ip_address, subnet_mask, gateway):
    command = f"netsh interface ipv4 set address name={interface} gateway={gateway} static {ip_address} {subnet_mask}"
    subprocess.run(command, capture_output=True, text=True)

print(get_nic_list())
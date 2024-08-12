import netifaces

def get_local_ip():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ip_info = addrs[netifaces.AF_INET][0]
            return ip_info['addr'], ip_info['netmask']

local_ip, netmask = get_local_ip()
print(f"Local IP: {local_ip}, Netmask: {netmask}")

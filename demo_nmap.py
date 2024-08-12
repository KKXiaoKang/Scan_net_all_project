import nmap

def get_network_devices(ip_range):
    nm = nmap.PortScanner(nmap_search_path=['/usr/bin/nmap'])
    nm.scan(hosts=ip_range, arguments='-sn')
    devices = []
    for host in nm.all_hosts():
        devices.append({'ip': host, 'hostname': nm[host].hostname()})
    return devices

if __name__ == '__main__':
    devices = get_network_devices('192.168.1.0/24')
    for device in devices:
        print(f"IP: {device['ip']} - Hostname: {device['hostname']}")

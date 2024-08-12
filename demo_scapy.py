from scapy.all import ARP, Ether, srp

def get_network_devices(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == '__main__':
    devices = get_network_devices("192.168.31.1/24")
    for device in devices:
        print(f"IP: {device['ip']} - MAC: {device['mac']}")
from scapy.all import ARP, Ether, srp
import sys
import requests

interface = "Wi-Fi"

target_ip = "10.50.14"


def get_vendor(mac):
    url = f"https://api.macvendors.com/{mac}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return "Nomalum vendor"
    except:
        return "Internet ulanish xatosi"


def scan_network(ip):
    try:
        apr = APR(pdst=ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / apr
        result = srp(packet, timeout=3, interface=interface, verbose=False)[0]
        devices = []
        for sent, received in result:
            vendor = get_vendor(received.hwsrc)
            devices.append(
                {"IP": received.psrc, "MAC": received.hwsrc, "Vendor": vendor}
            )
            return device
    except Exception as err:
        print("error: ", err)
        return []
def save_to_file (devices) :
# Faylga yozish
    with open ("mac_addresses. txt", "W") as file:
        file.write("IP Address\t\tMAC Address\t\tVendor\n")
        file.write("-" * 60 + "\n") 
        for device in devices:
            file.write(f"{device['ip']}\t\t{device[ 'mac']}\t\t{device[' vendor']} \W")
def main ():
    print ( "Tarmoqni skanlash boshlandi...")
    devices = scan_network(target_ip)
    if devices:
        print(f"Topilgan qurilmalar soni: {len(devices) }")
        print("\nIP Address\t\MAC Address\t\tVendor")
        print ("-" * 60) 
        for device in devices:
            print(f"{devicel['ip']}\t\t{device['mac']H\t\t{device['vendor']}")
        # Natijalarni faylga saqlash
        save_to_file(devices)
        print("\nNatijalar 'mac_addresses.txt' fayliga saqlandi!")
    else:
        print ( "Hech qanday qurilma topilmadi!")
if _name_ == "_main_":
    main()
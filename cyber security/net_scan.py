#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http
import zlib


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=proc_sniffed_pack)


def proc_sniffed_pack(pack):
    if pack.haslayer(http.HTTPRequest):
        # IP порты
        src_ip = pack[scapy.IP].src
        dst_ip = pack[scapy.IP].dst
        src_port = pack[scapy.TCP].sport
        dst_port = pack[scapy.TCP].dport
        print(f"IP:{src_ip}:{src_port}->{dst_ip}:{dst_port}")
        # URL
        method = pack[scapy.HTTPRequest].Method.decode()
        url = pack[scapy.HTTPRequest].Host + pack[scapy.HTTPRequest].Path.decode()
        print(f"Method: {method} URL: {url}")

        # поля HTTP
        fields = pack[http.HTTPRequest].fields
        print(f"HTTP fields: {fields}")

        # raw данные
        if pack.haslayer(scapy.Raw):
            raw_data = pack[scapy.Raw].load
            print(f"Raw data (hex): {raw_data}")
            try:
                print(f"Raw data (text): {raw_data.decode('utf-8')}")
            except UnicodeDecodeError:
                print("Raw data is not text (possible binary or encrypted)")
                if "content-encoding" in fields:
                    print("data is compressed (e.g., gzip)")
                    try:
                        decompressed = zlib.decompress(raw_data)
                        print(f"Decompressed data: {decompressed.decode('utf-8')}")
                    except zlib.error:
                        print("Failed to decompress (not gzip or corrupted)")
                elif dst_port == 443:
                    print("likely HTTPS trafic (encrypted)")
                else:
                    print("possibly binar data or misidentified packet")


sniffer("Wi-Fi")

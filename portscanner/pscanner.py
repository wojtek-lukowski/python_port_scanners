import socket
from termcolor import colored, cprint


targets = input('[*] Enter targets (split by ,): ')
ports = int(input('[*] How many ports: '))


def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print('[+] Port opened: ', port)
        sock.close()
    except:
        pass


def scan(targets, ports):
    for port in range(1, ports + 1):
        scan_port(targets, port)


if ',' in targets:
    print('[*] Scanning multiple targets')
    for ip_addr in targets.split(','):
        print('Scanning ', ip_addr)
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)

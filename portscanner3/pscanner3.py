import socket
from colored import fg, bg, attr


ip = input('[+] Enter target (xxx.xxx.xx): ')
hosts = input('[+] Enter hosts (separate by ,): ')
# hosts_int = int(hosts)
ports = int(input('[+] Enter number of ports: '))
color_white = fg('#ffffff') + bg('#000000')
color_green = fg('green') + bg('#000000')
color_orange = fg('208') + bg('#000000')
res = attr('reset')


def scan_port(ip, port):
    # print('ip:', ip, 'port:', port)
    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ip, port))
        print(color_green + '[+] Port opened: ', port + res)
        sock.close()
    except socket.timeout:
        pass
        # print(color_orange + "[-] No host detected" + res)
    except:
        # print('[+] Port closed: ', port)
        pass


def scan(target, ports):
    for port in range(1, ports + 1):
        # print('[*] target port', port)
        scan_port(target, port)


if ',' in hosts:
    print(color_orange + '[*] Scanning multiple hosts' + res)
    for host in hosts.split(','):
        target = ip + '.' + str(host)
        print('[*] Scanning ', target)
        scan(target, ports)
else:
    target = ip + '.' + str(hosts)
    print(color_white + '[*] Scanning ', target + res)
    scan(target, ports)

scan(ip, ports)

# test comment

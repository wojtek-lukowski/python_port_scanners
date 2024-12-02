import socket
from colored import fg, bg, attr


ip = input('[+] Enter target (xxx.xxx.xx): ')
hosts = input('[+] Enter number of hosts (1-256): ')
hosts_int = int(hosts)
ports = int(input('[+] Enter number of ports: '))
color_white = fg('#ffffff') + bg('#000000')
color_green = fg('green') + bg('#000000')
color_orange = fg('208') + bg('#000000')
color_red = fg('red') + bg('#000000')
res = attr('reset')

status: int


def scan_port(ip, port):
    global status

    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((ip, port))
        print(color_green + '[+] Port opened: ', str(port) + res)
        sock.close()
        status = 2

    except socket.timeout:
        status = 0
        pass
    except:
        status = 1


def scan(ip, ports):
    global status
    host_status = []
    for host in range(0, hosts_int):
        target = ip + '.' + str(host)
        print(color_white + '[*] Scanning', target + res)
        for port in range(1, ports + 1):
            scan_port(target, port)
            host_status.append(status)
        if 0 in host_status:
            print(color_orange + "[-] No host detected" + res)
        elif 2 in host_status:
            pass
        else:
            print(color_red + "[-] No open ports" + res)
        host_status = []


scan(ip, ports)

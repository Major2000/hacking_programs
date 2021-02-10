#the library to use for this program
import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[- 0 Scanning Target] ' + str(target))

    for port in range(75, 85):
        port_scanner(converted_ip, port)


def check_ip(address):
    try:
        IP(address)
        return (address)
    except ValueError:
        return socket.gethostbyname(address)


#estabilish the connection using socket library
def port_scanner(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1.0)
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) + ' Is Open')
    except:
        pass

targets = input('[+] Enter Target(s) To Scan(Split multiple targets by ,): ')
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)
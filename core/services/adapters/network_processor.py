import socket
import pythonping


def is_ip_valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def get_ip_by_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        pass


def ping_ip(ip):
    return pythonping.ping(ip, count=1)


def check_is_port_open(ip, port):
    port_connection_tester = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = port_connection_tester.connect_ex((ip, int(port)))
    port_connection_tester.close()
    return result == 0

from core.services.adapters.network_processor import get_ip_by_domain


def add_required_ips(websites):
    for website in websites:
        if len(website.ips) == 0 and website.hostname:
            ip = get_ip_by_domain(website.hostname)
            if ip:
                website.ips.append(ip)


def normalize_ports_lists(websites):
    for website in websites:
        website.ports = [port for port in website.ports if port.isdigit()]

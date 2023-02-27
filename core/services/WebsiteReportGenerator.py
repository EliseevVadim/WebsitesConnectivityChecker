from core.models.ConnectivityReportItem import ConnectivityReportItem
from core.models.ReportContentItem import ReportContentItem
from core.services.adapters.network_processor import ping_ip, check_is_port_open


def generate_report(website):
    if len(website.ips) == 0:
        error_message = "Не удалось разрешить IP адрес для указанного домена."
        return ConnectivityReportItem(website_info=website, error_message=error_message)
    content = []
    for ip in website.ips:
        ping_response = ping_ip(ip)
        rtt = ping_response.rtt_avg
        loss = ping_response.packet_loss
        if len(website.ports) == 0:
            content.append(ReportContentItem(domain=website.hostname, ip_address=ip, loss=loss, rtt=rtt))
            continue
        for port in website.ports:
            is_port_open = check_is_port_open(ip, port)
            content.append(ReportContentItem(domain=website.hostname, ip_address=ip, loss=loss, rtt=rtt,
                                             is_port_open=is_port_open, port=port))
    return ConnectivityReportItem(website_info=website, content=content)

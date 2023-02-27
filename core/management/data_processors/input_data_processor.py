from core.models.Website import Website
from core.services.adapters.network_processor import is_ip_valid


class InputDataProcessor(object):
    UNKNOWN_DOMAIN_REPLACER = "???"

    def generate_websites_sequence(self, raw_data):
        websites = []
        for row in raw_data:
            host = row['Host']
            ips = []
            if not host:
                host = self.UNKNOWN_DOMAIN_REPLACER
            if self.__is_valid_ip(host):
                ips.append(host)
                host = self.UNKNOWN_DOMAIN_REPLACER
            ports = row['Ports'].split(',')
            websites.append(Website(host, ips, ports))
        return websites

    @staticmethod
    def __is_valid_ip(host):
        return is_ip_valid(host)

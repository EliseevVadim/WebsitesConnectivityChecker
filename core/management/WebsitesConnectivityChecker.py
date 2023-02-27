from core.management.data_processors import pre_check_data_processor
from core.services.WebsiteReportGenerator import generate_report


class WebsitesConnectivityChecker(object):
    def __init__(self, websites):
        self.__websites = websites

    def generate_connectivity_report(self):
        connectivity_report = []
        pre_check_data_processor.add_required_ips(self.__websites)
        pre_check_data_processor.normalize_ports_lists(self.__websites)
        for website in self.__websites:
            report_item = generate_report(website)
            connectivity_report.append(report_item)
        return connectivity_report

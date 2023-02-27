from core.management.data_processors.input_data_processor import InputDataProcessor
from core.management.WebsitesConnectivityChecker import WebsitesConnectivityChecker
from core.services.adapters.input_data_reader import read_data


def check_websites_from_file(file_path, delimiter):
    reader = read_data(file_path, delimiter)
    input_data_processor = InputDataProcessor()
    websites = input_data_processor.generate_websites_sequence(reader)
    connectivity_checker = WebsitesConnectivityChecker(websites)
    output = connectivity_checker.generate_connectivity_report()
    for item in output:
        item.display()

import datetime

from core.models.Displayable import Displayable


class ReportContentItem(Displayable):
    def __init__(self, domain, ip_address, loss, rtt, is_port_open=None, port=-1):
        self.__ping_date = datetime.datetime.now()
        self.__domain = domain
        self.__ip_address = ip_address
        self.__loss = loss
        self.__rtt = rtt
        self.__is_port_open = is_port_open
        self.__port = port

    def __str__(self):
        if self.__is_port_open is None:
            open_state = "???"
        else:
            open_state = ("Not opened", "Opened")[self.__is_port_open]
        return f"{self.__ping_date} | {self.__domain} | {self.__ip_address} | {self.__loss} |" \
               f" {round((self.__rtt * 1000), 2)} ms | {self.__port} | {open_state}"

    def display(self):
        print(self)

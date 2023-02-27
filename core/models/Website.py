from core.models.Displayable import Displayable


class Website(Displayable):
    def __init__(self, hostname=None, ips=None, ports=None):
        self.hostname = hostname
        self.ips = ips
        self.ports = ports

    def __str__(self):
        return f"[{self.hostname}, {self.ips}, {self.ports}]"

    def display(self):
        print(self)

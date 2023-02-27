from core.models.Displayable import Displayable


class ConnectivityReportItem(Displayable):
    def __init__(self, website_info, error_message=None, content=None):
        if content is None:
            content = []
        self.__website_info = website_info
        self.__error_message = error_message
        self.__content = content

    def display(self):
        self.__website_info.display()
        if self.__error_message:
            print(self.__error_message)
            print("\n")
            return
        for content_item in self.__content:
            content_item.display()
        print("\n")

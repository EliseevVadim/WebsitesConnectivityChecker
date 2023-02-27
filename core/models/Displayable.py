import abc


class Displayable(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def display(self):
        raise NotImplementedError

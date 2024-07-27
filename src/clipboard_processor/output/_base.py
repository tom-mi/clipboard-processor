import abc


class Output(abc.ABC):
    @abc.abstractmethod
    def show(self, title: str, content: str):
        raise NotImplementedError

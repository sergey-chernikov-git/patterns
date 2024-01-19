from abc import ABC, abstractmethod


class AbstractObservable(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self, observer):
        pass


class AbstractObserver(ABC):
    @abstractmethod
    def notify(self, observer):
        pass


class Observable(AbstractObservable):
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        try:
            self.observers.index(observer)
        except ValueError:
            self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.notify(message)


class ConsoleObserver(AbstractObserver):
    def notify(self, message):
        print(message)


class FileObserver(AbstractObserver):
    def notify(self, message):
        with open("observer.log", mode="a+") as file:
            file.write(message + '\n')
        file.close()


observable = Observable()
observable.subscribe(ConsoleObserver())
observable.subscribe(FileObserver())

observable.notify("test observer")

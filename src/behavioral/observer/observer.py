from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(self, observer):
        raise NotImplementedError

    @abstractmethod
    def notify(self, modifier=None):
        raise NotImplementedError


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, subject):
        raise NotImplementedError


class Subject(AbstractSubject):
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        try:
            self.observers.index(observer)
        except ValueError:
            self.observers.append(observer)

    def unsubscribe(self, observer):
        try:
            self.observers.remove(observer)
        except Exception as e:
            print(e)

    def notify(self, modifier=None):
        for observer in self.observers:
            if observer != modifier:
                observer.update(self)


class DataSubject(Subject):
    def __init__(self, name):
        Subject.__init__(self)
        self.name = name
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value=None):
        self._data = value
        self.notify()


class DataConsoleViewer(AbstractObserver):
    def update(self, subject):
        print(f"DataConsoleViewer: {subject.name} - {subject.data}  on console")


class DataFileViewer(AbstractObserver):
    def update(self, subject):
        print(f"DataFileViewer: {subject.name} - {subject.data} into file")


class DataPopUpMessageViewer(AbstractObserver):
    def update(self, subject):
        print(f"DataPopUpMessageViewer: {subject.name} - {subject.data} into file")


observable = DataSubject("Data observable")

data_console_viewer_observer = DataConsoleViewer()
data_file_viewer_observer = DataFileViewer()
data_pop_up_message_viewer_observer = DataPopUpMessageViewer()

observable.subscribe(data_console_viewer_observer)
observable.subscribe(data_file_viewer_observer)
observable.subscribe(data_pop_up_message_viewer_observer)

observable.data = "Test Data 1"
observable.data = "Test Data 2"
observable.data = "Test Data 3"

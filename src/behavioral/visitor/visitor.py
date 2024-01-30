from json import dumps
from abc import ABC, abstractmethod
from dataclasses import dataclass


class AbstractElement(ABC):
    @abstractmethod
    def accept(self, visitor=None):
        raise NotImplementedError


class AbstractVisitor(ABC):
    def visit(self, cls):
        raise NotImplementedError


class Element(AbstractElement):
    def accept(self, visitor=None):
        visitor.visit(self)

    def do_action(self):
        print("An action has been done")


class JSONVisitor(AbstractVisitor):
    def visit(self, cls):
        print(dumps(cls.__dict__))


class ConsoleVisitor(AbstractVisitor):
    def visit(self, cls):
        print(cls.__dict__)


class FileVisitor(AbstractVisitor):
    def visit(self, cls):
        print("Open a file")
        print(f"Export to file: {cls.__dict__}")
        print("Close a file")


@dataclass
class UserElement(Element):
    name: str
    age: int


@dataclass
class AccountElement(Element):
    account_number: int


@dataclass
class MortgageElement(Element):
    fee: int


mortgage = MortgageElement(32)
account = AccountElement(25571128587)
user = UserElement(name="Jane", age=25)

user.do_action()

json_visitor = JSONVisitor()
majority_visitor = FileVisitor()
console_visitor = ConsoleVisitor()

mortgage.accept(visitor=json_visitor)
user.accept(visitor=majority_visitor)
account.accept(visitor=console_visitor)

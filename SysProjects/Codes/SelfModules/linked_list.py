from dataclasses import dataclass, field

@dataclass
class Node:
        
        value = field(default=None)
        next = field(default=None)


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = Node

    def push_head(self, data):
        ...
    def push_tail(self, data):
        ...
    def push_to(self):
        ...


    def pop_head(self):
        ...
    def pop_tail(self):
        ...
    def pop_at(self):
        ...


    def update(self):
        ...

    def __repr__(self) -> str:
        return f'{self.list}'


class DoublyLinkedList():
    def __init__(self) -> None:
        pass

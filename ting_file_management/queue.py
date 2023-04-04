from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self.size() == 0:
            return self._data.pop(0)
        else:
            return None

    def search(self, index):
        try:
            return self._data[index]
        except IndexError:
            raise IndexError("Índice Inválido ou Inexistente")

    def size(self):
        return len(self._data)

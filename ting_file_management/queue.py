from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if self.is_empty():
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index in self._queue:
            return self._queue
        raise IndexError("Índice Inválido ou Inexistente")

    def is_empty(self):
        return len(self._queue) == 0

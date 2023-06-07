from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 44})
    queue.enqueue({"qtd_linhas": 2})
    queue.enqueue({"qtd_linhas": 1})
    queue.enqueue({"qtd_linhas": 5})
    assert len(queue) == 5

    removed = queue.dequeue()
    assert removed == {"qtd_linhas": 4}
    assert len(queue) == 4

    element1 = queue.search(0)
    element2 = queue.search(1)
    element2 = queue.search(2)
    element2 = queue.search(0)
    assert element1 == {"qtd_linhas": 2}
    assert element2 == {"qtd_linhas": 2}
    assert element2 == {"qtd_linhas": 2}
    assert element2 == {"qtd_linhas": 2}

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(444)

from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(50)

    priority = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3"],
    }

    not_priority = {
        "nome_do_arquivo": "teste.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [
            "linha1",
            "linha2",
            "linha3",
            "linha4",
            "linha5",
            "linha6",
        ],
    }

    queue.enqueue(not_priority)
    queue.enqueue(priority)

    assert len(queue) == 2

    item = queue.search(0)
    assert item["qtd_linhas"] == 3

    item2 = queue.search(1)
    assert item2["qtd_linhas"] == 6

    queue.dequeue()
    assert len(queue) == 1

    item3 = queue.search(0)
    assert item3["qtd_linhas"] == 6

"""
Faça uma lista de tarefas com as seguintes opções
    adiciona tarefa
    lista tarefas
    opão de desfazer(a cada ver que chamarmos, desfaz a ultima ação)
    opção de refazer (a cada vez que chamarmos, refaz a ultima ação)
"""


def show_op(todo_list):
    print()
    print("Tarefas")
    print(todo_list)
    print()


def do_add(todo, todo_list):
    todo_list.append(todo)


def do_ando(todo_list, redo_list):
    if not todo_list:
        print("Nada a Fazer")
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print("Nada a Refazer")
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


if __name__ == "__main__":

    todo_list = []
    redo_list = []

    while True:
        todo = input("Digite uma tarfe ou undo, redo, ls: ")

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == "undo":
            do_ando(todo_list, redo_list)
            continue
        elif todo == "redo":
            do_redo(todo_list, redo_list)
            continue
        do_add(todo, todo_list)

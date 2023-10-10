import datetime
import text


def menu():
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    select = input(text.select_menu)
    return select


def show_node(book: dict[int:dict[str, str]]):
    if book:
        for index, value in book.items():
            print(f"id {index} date:{value.get('date')}")
            print(f"{value.get('title')} \n{value.get('text')}")
    else:
        print_message(text.error_show)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def add_node():
    new = {}
    for key, value in text.new_node.items():
        value_node = input(value)
        if value_node:
            new[key] = value_node
            new['date'] = str(datetime.datetime.now())
        else:
            print(print_message(text.empty_node))
            break

    return new


def update_node(node):
    if node:
        print(text.updates_node, node.get("title"))
        title_node = input(text.new_title)
        print(text.updates_node, node.get("text"))
        text_node = input(text.new_title)
        if title_node and text_node:
            node["title"] = title_node
            node["text"] = text_node
            node['date'] = str(datetime.datetime.now())
        else:
            print(print_message(text.empty_node))

    else:
        print(print_message(text.error_id))


def search_word() -> str:
    return input(text.search_word)


def view_input(massage: str):
    return input(massage)
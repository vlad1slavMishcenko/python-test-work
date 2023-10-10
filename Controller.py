import view
import text
import model


def start():
    pb = model.NodeBook()
    if pb.open_file:
        view.print_message(text.load_successful)
    else:
        view.print_message(text.error_show)
    while True:
        select = view.menu()
        match select:
            case "show":
                view.show_node(pb.node)

            case "add":
                node = view.add_node()
                if node:
                    pb.add_node(node)
                    if pb.save_file():
                        view.print_message(text.save_successful)
                    else:
                        view.print_message(text.error_save)
                else:
                    view.print_message(text.empty_node)
            case "search":
                node = pb.search(view.search_word())
                view.show_node(node)

            case "update":
                date = pb.search(view.search_word())
                view.show_node(date)
                id_node = view.view_input(text.id_node)
                view.update_node(pb.update(id_node))
                if pb.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)

            case "delete":
                date = pb.search(view.search_word())
                view.show_node(date)
                id = view.view_input(text.id_node)
                delete_node = pb.remuve(id)
                if delete_node:
                    view.print_message(text.remuve_node(delete_node.get("date")))
                pb.save_file()

            case "exit":
                pb.save_file()
                view.print_message(text.good_bye)
                break
            case _:
                view.print_message(text.input_error)
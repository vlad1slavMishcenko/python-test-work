import json


class NodeBook:

    def __init__(self, path: str = 'node.json'):
        self.node: dict = {}
        self.path = path

    @property
    def open_file(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                self.node = json.load(file)

            return True
        except:
            return False

    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.node, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False

    def search(self, word: str) -> dict[int:dict[str, str]]:
        result = {}
        for index, node in self.node.items():
            if word.lower() in ' '.join(node.values()).lower():
                result[index] = node
        return result

    def check_id(self):
        if self.node:
            result = max(list(map(int, self.node))) + 1
            return str(result)
        return 1

    def add_node(self, new: dict[str, str]):
        node = {self.check_id(): new}
        self.node.update(node)

    def remuve(self, id_node: str):
        if id_node in self.node.keys():
            return self.node.pop(id_node)
        else:
            return False

    def update(self, id_node: str):
        if id_node in self.node.keys():
            return self.node.get(id)

class Trie:
    def __init__(self, value, path=''):
        self.value = value
        self.full_path = path + value
        self.children: list[Trie] = []
        self.count = 0

    def _get_child_by_value(self, v: str):
        for n in self.children:
            if n.value == v:
                return n

        node = Trie(v, self.full_path)
        self.children.append(node)
        return node

    def push(self, string):
        if len(string) > 1:
            string = string[1:]
            v = string[0]
            node = self._get_child_by_value(v)
            node.push(string)
        else:
            self.count += 1

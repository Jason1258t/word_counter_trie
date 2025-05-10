class Trie:
    default_relations_depth = 2

    def __init__(self, value, path=''):
        self.value = value
        self.full_path = path + value
        self.children: list[Trie] = []
        self.count = 0
        self.related_words = []

    @property
    def count_with_relations(self):
        return sum([x['cnt'] for x in self.related_words])

    def push(self, string):
        if len(string) <= 1:
            self.count += 1
            return

        string = string[1:]
        v = string[0]
        node = self._get_child_by_value(v)
        node.push(string)

    def _get_child_by_value(self, v: str):
        for n in self.children:
            if n.value == v:
                return n

        node = Trie(v, self.full_path)
        self.children.append(node)
        return node

    def get_related_children(self, depth):
        """calling this function also updates field related_words"""
        if depth == 0: return []
        if len(self.full_path) < 4 and (self.count == 0 or depth != self.default_relations_depth):
            return []

        res = []
        if self.count > 0:
            res.append({'word': self.full_path, 'cnt': self.count})

        indexes_to_remove = []
        for i in range(len(self.children)):
            related = self.children[i].get_related_children(depth - 1)
            if len(related) > 0:
                indexes_to_remove.append(i)
                res += related

        self._remove_children_from_indexes(indexes_to_remove)
        self.related_words = res
        return self.related_words

    def _remove_children_from_indexes(self, indexes):
        for i in range(len(indexes)):
            self.children.pop(indexes[i] - i)

    def __str__(self):
        return '{\n\t' + f"value: {self.value}\n\tpath: {self.full_path}\n\tchildren:" \
                         f" {self.children}\n\tcount: {self.count}\n\trelated: {self.related_words}\n" + '}'

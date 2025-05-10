from trie import *

class WordStatistics:
    _tree_root = '#'

    def __init__(self):
        self.root = Trie(self._tree_root)

    def push_word(self, word: str):
        word = self._prepare_word(word)
        self.root.push(word)

    def get_stats(self):
        return self._get_node_statistics(self.root)

    def _get_node_statistics(self, node: Trie):
        node.get_related_children(Trie.default_relations_depth)
        stats = {}
        if len(node.children) == 0 or node.count != 0:
            words = [self._normalize_word(w['word']) for w in node.related_words]
            stats = {**stats, **{', '.join(words): node.count_with_relations}}
        for n in node.children:
            stats = {**stats, **self._get_node_statistics(n)}
        return stats

    @classmethod
    def _prepare_word(cls, word: str):
        return cls._tree_root + word.lower()

    @classmethod
    def _normalize_word(cls, word: str):
        return word[word.index(cls._tree_root) + 1:]
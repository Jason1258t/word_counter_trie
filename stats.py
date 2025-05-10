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
        node.get_related_children(Trie.default_depth)
        if len(node.children) == 0:
            words = [self._normalize_word(w['word']) for w in node.related_words]
            if  node.count_with_relations == 0:
                print(node)
            return {str(words): node.count_with_relations}

        stats = {}
        for n in node.children:
            stats = {**stats, **self._get_node_statistics(n)}
        if node.count != 0:
            words = [self._normalize_word(w['word']) for w in node.related_words]
            stats = {**stats, **{str(words): node.count_with_relations}}
        return stats

    @classmethod
    def _prepare_word(cls, word: str):
        return cls._tree_root + word.lower()

    @classmethod
    def _normalize_word(cls, word: str):
        return word[word.index(cls._tree_root) + 1:]
class TrieNode:
    __slots__ = ('value', 'end_of_word', 'children', 'weight', 'completeName', 'photo', 'id')

    def __init__(self, value: str, end_of_word=False):
        self.value = value
        self.end_of_word = end_of_word
        self.children = {}
        self.weight = -1

    def add(self, word_part: str, completeName : str, photo : str, id : int, *, weight: int=-1) -> None:
        if len(word_part) == 0:
            self.end_of_word = True
            self.weight = weight
            self.completeName = completeName
            self.photo = photo
            self.id = id
            return

        first_char = word_part[0]
        node = self.children.setdefault(first_char, TrieNode(first_char))
        node.add(word_part[1:],  completeName, photo, id, weight=weight)

    def find_all(self, word_part: str, path: str=""):
        if self.end_of_word:
            yield path + self.value, self.completeName, self.photo, self.id

        if len(word_part) > 0:
            char = word_part[0]
            node = self.children.get(char)

            if node is not None:
                yield from node.find_all(word_part[1:], path + self.value)
        else:
            for node in self.children.values():
                yield from node.find_all("", path + self.value)





from Model.DAL import FireBase as DAL
from Controllers.factory.Trie_Patern import TrieNode


class SearchEngine :
    __slots__ = ("searchedString", "data", "Controller")

    def __init__(self, word, dataType):

        self.searchedString = word.capitalize()
        self.data = DAL.FireBase(dataType).getAll()
        self.Controller = TrieNode("")


        for user in self.data :
            self.Controller.add(user["first_name"].capitalize(), completeName=user["last_name"], photo=user["photo"], id=user["id"])
            self.Controller.add(user["last_name"].capitalize(),  completeName=user["first_name"], photo=user["photo"], id=user["id"])

    def exec(self):
        split_words = self.searchedString.split()
        last_word = split_words[-1]
        return self.getResult(last_word)

    def getResult(self, word):
        prefix = ' '.join(word[:-1])
        suggestions = self.Controller.find_all(word)
        full_suggestions = []
        for suggestion in suggestions:
            suggestionHash = {'name' : suggestion[0], 'lastName' : suggestion[1], 'photo' : suggestion[2], 'id' : suggestion[3]}
            full_suggestions.append(suggestionHash)
        return{'match': list(full_suggestions)}

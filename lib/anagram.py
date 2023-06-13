# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []
        for word in possible_anagrams:
            if sorted(word) == sorted(self.word):
                matches.append(word)
        return matches

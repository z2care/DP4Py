'''
Created on 2013-10-23

@author: zhangzhi
@contact: z2care@gmail.com
'''
from copy import deepcopy

class WordOccurrences(object):
    
#   The list of the index of each occurrence of the word in the text.
    occurrences = []
    
#   input: the text in which the occurrences have to be found
#   input: the word that should appear in the text
    def WordOccurrences(self, text, word):
#       Clear the occurrences list
        del self.occurrences[:]
        start = 0        
        
        while (start <= len(text)-len(word)):
            wordIndex = text.find(word, start)
            if wordIndex != -1:
                self.occurrences.append(wordIndex)
                start = wordIndex + 1
            else:
                break

#   input: a number to point on the nth occurrence.
#   output: the index of the nth occurrence.
    def getOneOccurrenceIndex(self,n):
        return self.occurrences.pop(n)
#   Return the nth item of the occurrences field if any.

#   output: a WordOccurrences object containing the same data.
    def clone(self):
        return deepcopy(self)

if __name__ == '__main__':
    text = "The prototype pattern is a creational design pattern in software development first described in design patterns, the book."
    word = "pattern"
    searchEngine = WordOccurrences()
    searchEngine.WordOccurrences(text, word)
    print searchEngine.getOneOccurrenceIndex(0)
    
    anotherSearchEngine = searchEngine.clone()
    anotherSearchEngine.WordOccurrences(text, "des")
    print anotherSearchEngine.getOneOccurrenceIndex(0)
    
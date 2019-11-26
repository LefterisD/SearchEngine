import os

class doc():

    def __init__(self,Name):
        self.totalWords=0       #How many words are in this document
        self.maxNumOfWords=0    #How many times the most frequent word appears.
        self.maxFrequency=0
        self.name = Name        #Name of the document
        self.words = {}
        #self.fileName = os.path.basename(Name)

    def add(self,word):
        self.totalWords = self.totalWords + 1
        if word in self.words:
            self.words[word] = self.words[word] + 1
        else:
            a = {word:1}
            self.words.update(a)

        if self.words[word] > self.maxNumOfWords:
            self.maxNumOfWords = self.words[word]
        self.maxFrequency = self.maxNumOfWords / self.totalWords


    def getTotalWords(self):
        return self.totalWords

    def getMaxFrequency(self):
        return self.maxFrequency

    def getMaxNumberOfWords(self):
        return self.maxNumOfWords

    def getName(self):
        return self.name

    def getNumOfWords(self):
        return numOfWords

    def getWords(self):
        return self.words

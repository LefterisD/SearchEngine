import glob
from pathlib import Path
import string

#path = 'C:\\Users\\AlexL\\Desktop\\Information Retrieval\\Assignment\\InvertedIndex\\*.txt'
path = 'C:\\Users\\lefteris\\Desktop\\alex\\SearchEngine\\InvertedIndex\\*.txt'
files = glob.glob(path)


class invIndx():
    def __init__(self):
        self.catalog = {}
        self.docs = []

    def search_topK(self,querry,k):
        pass

    def printCatalog(self):
        for keyword in self.catalog:
            print(keyword,"  :  ",self.catalog[keyword])

    def add(self,keyword,doc):
        flag= False
        if keyword in self.catalog:
            self.catalog[keyword][0] = self.catalog[keyword][0] + 1
            for document in self.catalog[keyword][1]:
                if doc == document[1]:
                    document[0] = document[0] + 1
                    flag = True
                else:
                    flag=False
            if flag == False:
                self.catalog[keyword][1].append([1,doc])
        else:
            new_keyword = {keyword:[1,[ [1,doc] ] ]}
            self.catalog.update(new_keyword)

    def removePuncuation(self,line):
        tr = str.maketrans("", "", string.punctuation)
        line=line.translate(tr)
        return line

    def search(self,line):
        intersection= []
        keywordsList = []
        keywords = line.split(" ")
        for keyword in keywords:
            keywordList = self.findDocs(keyword)
            keywordsList.append(keywordList)
        #---intersection---
        #If users searches one word then no intersection should be made
        if len(keywordsList) ==1:
            return keywordsList
        else:
            intersection.append(set(keywordsList[0]))
            for i in range(1,len(keywordsList)):
                intersection[0] = list(set(intersection[0]) & set(keywordsList[i]))
            return intersection

    def findDocs(self,keyword):
        self.docs = []
        if  keyword in self.catalog:
            for a in self.catalog[keyword][1]:
                self.docs.append(a[1])
        return self.docs

if __name__ == "__main__":
    myInvertedIndex = invIndx()
    for name in files:
        with open(name) as file:
            for line in file:
                line = myInvertedIndex.removePuncuation(line)
                fields = line.split(" ")
                for keyword in fields:
                    kwd = keyword.split("\n")
                    myInvertedIndex.add(kwd[0],name)
    #myInvertedIndex.printCatalog()
    #myInvertedIndex.findDocs("new")
    #print(myInvertedIndex.docs)
    print(myInvertedIndex.search("new"))

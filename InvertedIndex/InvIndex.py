import glob
import string
import os
import math

path = "{}\*.txt".format(os.getcwd())
files = glob.glob(path)


class invIndx():
    def __init__(self):
        self.catalog = {}
        self.docs = []

    def search_topK(self,querry,k):
        pass

    def findweight(self,keyword):
        #print("Keyword:",keyword)
        weights = []
        numberOfAppearences = self.catalog[keyword][0]
        numberOfDocuments = len(self.catalog[keyword][1])
        idf = abs(math.log(numberOfDocuments/numberOfAppearences))
        #print("IDF= ",idf)
        for numberOfTimes in self.catalog[keyword][1]:
            freq = numberOfTimes[0]
            #print("freq= ",freq)
            tf = 1 + math.log(freq)
            #print("TF= ",tf)
            w = tf * idf
            weights.append([w,numberOfTimes[1]])
        print(weights)


    def findDocs(self,keyword):
        self.docs = []
        if keyword in self.catalog:
            for a in self.catalog[keyword][1]:
                self.docs.append(a[1])
        return self.docs

    def search(self,line):
        keywordsList = []
        intersection = []
        keywords = line.split(" ")
        for keyword in keywords:
            keywordList = self.findDocs(keyword)
            keywordsList.append(keywordList)
        if len(keywordsList) == 1:
            return keywordsList
        else:
            intersection.append(set(keywordsList[0]))
            for i in range(1,len(keywordsList)):
                intersection[0] = list(set(intersection[0]) & set(keywordsList[i]))
            return intersection


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

    def removePunctuation(self,line):
        tr = str.maketrans("", "", string.punctuation)
        line = line.translate(tr)
        return line

if __name__ == "__main__":
    myInvertedIndex = invIndx()
    for name in files:
        with open(name) as file:
            for line in file:
                line = myInvertedIndex.removePunctuation(line)
                fields = line.split(" ")
                for keyword in fields:
                    keyword = keyword.lower()
                    kwd = keyword.split("\n")
                    myInvertedIndex.add(kwd[0],name)
    print(myInvertedIndex.search("Lorem Ipsum"))

import glob
import string
import os
import math
from  doc import doc

path = "{}/*.txt".format(os.getcwd())
files = glob.glob(path)


class invIndx():
    def __init__(self):
        self.catalog = {}
        self.numberOfDocuments = 0


    def top_k_inverted(self,documents,query,k):
        q = dict.fromkeys(documents)
        for x in q:
            q[x] = 0
        for keyword in query:
            if keyword in self.catalog:             #If the word isnt in the catalog then its weight will be 0, no need to do operations
                ni = len(self.catalog[keyword][1])
                N = self.numberOfDocuments
                IDF = math.log(1 + N/ni)
                for doc in documents:
                    if keyword in doc.getWords():
                        freq = doc.getWords()[keyword]
                        TF = 1 + math.log(freq)
                        q[doc] = q[doc] + TF*IDF
                        #print("doc: {}\n keyword: {}, ni: {}, N: {}, IDF: {}, TF: {} (freq = {}), W: {} \n\n".format(doc.getName(),keyword,ni,N,IDF,TF,freq,TF*IDF))
        for a in q:
            q[a] = q[a]/ math.sqrt(a.getTotalWords())                       #Division by Ld
        q = sorted(q.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
        if k > self.numberOfDocuments:
            return q
        return q[:k]

    def search(self,query,k):
        documentList = []
        finalQuery = []
        query = self.removePunctuation(query)
        query = query.split(" ")
        for keyword in query:
            kwd = keyword.split("\n")
            kwd = kwd[0].lower()
            finalQuery.append(kwd)
            keywordList = self.findDocs(kwd)
            documentList.extend(keywordList)
        documentList = list(dict.fromkeys(documentList))  #list with all the documents that have one or more words from the query
        return self.top_k_inverted(documentList,finalQuery,k)

    def findDocs(self,keyword):
        docs = []
        if keyword in self.catalog:
            for a in self.catalog[keyword][1]:
                docs.append(a[1])
        return docs

    def add(self,keyword,doc):
        flag = False
        if keyword in self.catalog:
            self.catalog[keyword][0] = self.catalog[keyword][0] + 1
            for document in self.catalog[keyword][1]:
                if doc.getName() == document[1].getName():
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

    def printList(self,list):
        for doc in list:
                print(doc.getName())

    def printCatalog(self):
        for keyword in self.catalog:
            print(keyword," ",self.catalog[keyword][0])
            for k in self.catalog[keyword][1]:
                print("      [",k[0],",",k[1].getName(),"]")



if __name__ == "__main__":
    myInvertedIndex = invIndx()
    for name in files:
        myInvertedIndex.numberOfDocuments += 1
        newDoc = doc(name)
        with open(name) as file:
            for line in file:
                line = myInvertedIndex.removePunctuation(line)
                fields = line.split(" ")
                for keyword in fields:
                    kwd = keyword.split("\n")
                    kwd = kwd[0].lower()
                    newDoc.add(kwd)
                    myInvertedIndex.add(kwd,newDoc)                 ## TO-DO SEARCH FOR "Lorem"
    #print(myInvertedIndex.printCatalog())
    answer = myInvertedIndex.search("Lorem",4)
    for i in range(0,len(answer)):
        print("{})  {}    {}".format(i+1,answer[i][0].getName(),answer[i][1]))

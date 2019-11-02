import glob

path = 'C:\\Users\\Lefteris\\Desktop\\GitHub\\SearchEngine\\InvertedIndex\\*.txt'
files = glob.glob(path)

class invIndx():
    def __init__(self):
        self.catalog = {}

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

if __name__ == "__main__":
    myInvertedIndex = invIndx()
    for name in files:
        with open(name) as file:
            for line in file:
                fields = line.split(" ")
                for keyword in fields:
                    kwd = keyword.split("\n")
                    myInvertedIndex.add(kwd[0],name)
    myInvertedIndex.printCatalog()

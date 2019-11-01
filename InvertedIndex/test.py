import glob

catalog = {}
path = 'C:\\Users\\AlexL\\Desktop\\testing\\InvertedIndex\\*.txt'
files = glob.glob(path)


def add(keyword,doc):
    flag= False
    if keyword not in catalog:
        new_keyword = {keyword:[1,[ [1,doc] ] ]}
        catalog.update(new_keyword)
    else:
        catalog[keyword][0] = catalog[keyword][0] + 1
        for document in catalog[keyword][1]:
            if doc == document[1]:
                document[0] = document[0] + 1
                flag = True
            else:
                flag=False
        if flag == False:
            catalog[keyword][1].append([1,doc])


for name in files:
    with open(name) as file:
        for line in file:
            fields = line.split(" ")
            for keyword in fields:
                #print("This is the name: ",name)
                add(keyword, name)

print(catalog)

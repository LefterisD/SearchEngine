import glob

catalog = {}
path = 'C:\\Users\\AlexL\\Desktop\\testing\\InvertedIndex\\*.txt'
files = glob.glob(path)


def add(keyword,doc):
    if keyword in catalog:
        catalog[keyword][0] = catalog[keyword][0] + 1
        #print("#fores uparxei to keyword se ola ta documents = ",catalog[keyword][0])
        #print(catalog)
        flag = False
        for document in catalog[keyword][1]:
            #print("Poses fores uparxei kai se poia document = ",document)
            if document[1] == doc:
                document[0] = document[0] + 1
                flag = True
        if (not flag):
            print("flag is false")
            catalog[keyword][1].append([1,doc])

    else:
        #print(doc)
        a = {keyword:[1, [ [1, doc] ] ]}
        catalog.update(a)

for name in files:
    with open(name) as file:
        for line in file:
            fields = line.split(" ")
            for keyword in fields:
                #print("This is the name: ",name)
                add(keyword, name)

print("\n\n")
print(catalog)

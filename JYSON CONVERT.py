"""
import json
# Data to be written
dictionary=[]
with open('/Users/birkankalyon/PycharmProjects/word_aplication/data translate/english02.json', "r") as file:
    ortak=[]
    file.seek(0)
    for i in file:
        i=i
        dictionary.append(i)
        print(i)
print(dictionary)

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

"""
import json
dictionary={}
with open('/Users/birkankalyon/PycharmProjects/word_aplication/data translate/english01.json') as f:
    data = json.load(f)
    for i in data:
        dictionary.update(i)
        #print(i)
#print(dictionary)
#for key, value in dictionary.items():
    #print (key,':--->', value)

#print(dictionary.items())
#print(dictionary.values())
#print(dictionary.keys('zeta'))


kelime="bike"
def hop(dictionary, key):
    if key in dictionary.keys():
        #print(key)
        print(dictionary[key],end="")
    else:
        print("N/A")
hop(dictionary,kelime)
"""
def hop2(dictionary, key):
    if key in dictionary:
        print("Present, ", end=" ")
        print(dictionary[key])
    else:
        print("Not present")


key = 'bike'
hop2(dictionary, key)

"""
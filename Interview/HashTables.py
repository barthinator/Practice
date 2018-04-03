#Ransom note

#This can be updated with just one hastable that decrements
#when ransom is found, if any are negative then wont work

magazine = ["give", "me", "one", "grand", "today", "night"]
ransom = ["give", "me", "one", "grand"]

#Creates first string dictionary
magDict = {}
for word in magazine:
    #.keys() will give a list of keys in the dict
    if word not in magDict.keys():
        #Sets a new value with the word if word not added yet
        magDict.update({word: 1})
    else:
        #increments value if already there
        magDict[word] += 1

#Creates ransom hash table
ransomDict = {}
for word in ransom:
    #.keys() will give a list of keys in the dict
    if word not in ransomDict.keys():
        #Sets a new value with the word if word not added yet
        ransomDict.update({word: 1})
    else:
        #increments value if already there
        ransomDict[word] += 1

#Zip allows you to iterate though two lists or dicts
for m, r in zip(magDict, ransomDict):
    #Checks to make sure it is not Nothing
    if ransomDict[r] is not None:
        if ransomDict[r] <= magDict[r]:
            continue
        else:
            #return "No"
            print("NOPE")
    else:
        #return "no"
        print("NOPE")

#return "yes"

print(list(zip(magDict, ransomDict)))

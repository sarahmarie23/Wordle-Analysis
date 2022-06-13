from pprint import pprint


def compute():

    with open('sorted.txt') as myfile:
        words = myfile.read().splitlines()

    greendict = {}
    yellowdict = {'r': 1 , 'o' : 2, 'd' : 4}
    greylist = ['a', 'i', 's', 'l', 'e', 'p', 'u',  ]
    # TODO: account for guessing a double letter. Say the word is "basic" and you guess "bossy". There would be a greendict for s:2 but 
    # the 2nd s can't be in greylist 
    for i in list(words):
        if checkgreen(i, greendict) is True:
            words.remove(i)
            
        elif checkyellow(i, yellowdict) is True:
            words.remove(i)
            
        else: 
            if checkgrey(i, greylist) is True:
                words.remove(i)
    print('The {} possible words are:'.format(len(words)))
    pprint(words)

    myfile.close()
                
def checkgreen(i, greendict):
    for k, v in greendict.items():
        if i[v] != k:
            return True
    return False

def checkyellow(i, yellowdict):
    if not all(letter in i for letter in yellowdict.keys()):
        return True
    else:
        for k, v in yellowdict.items():
            if i[v] == k:
                return True
    return False

def checkgrey(i, greylist):
    if any(letter in i for letter in greylist):
        return True
    return False

        


        
        


        

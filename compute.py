from pprint import pprint


def compute():

    with open('sorted.txt') as myfile:
        words = myfile.read().splitlines()

    greendict = {'s':3}
    yellowlist = ['e']
    #TODO: account for the position of yellow letters
    greylist = ['t', 'a', 'i', 'r', 'c', 'l', 'u', 'd', 'm', 'y', ]
    #TODO: account for guessing a double letter. We know s is at position 3 but there's no second s
    for i in list(words):
        if checkgreen(i, greendict) is True:
            words.remove(i)
            
        elif checkyellow(i, yellowlist) is False:
            words.remove(i)
            
        else: 
            if checkgrey(i, greylist) is True:
                words.remove(i)
    print('The possible words are:')
    pprint(words)

    myfile.close()
                
def checkgreen(i, greendict):
    for k, v in greendict.items():
        if i[v] != k:
            return True
    return False

def checkyellow(i, yellowlist):
    if (all(letter in yellowlist for letter in i)):
        return False
    return True

def checkgrey(i, greylist):
    if any(letter in i for letter in greylist):
        return True
    return False

        


        
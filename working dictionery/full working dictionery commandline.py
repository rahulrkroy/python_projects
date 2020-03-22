import json
from difflib import *

filepath='/home/shikari/coding/python_Projects/dict_data.json'
data=json.load(open(filepath))


def findMeaning(s):
    if s in data:
        print("Meaning of ",s," is:")
        print(*data[s],sep='\n')
    elif(len(get_close_matches(s,data.keys()))>0):
        word=get_close_matches(s,data.keys())[0]
        yn=input("{} not found. Did you mean {}. Press Y for yes or any other key for no \n".format(s,word)).lower()
        if(yn=='y'):
            findMeaning(word)
        else:
            print("The word {} doesnt exist. Please recheck".format(s))
    else:
        print("The word {} doesnt exist. Please recheck".format(s))


enterWord=input("Enter the word whose meaning you wanna find \n").lower()
findMeaning(enterWord)

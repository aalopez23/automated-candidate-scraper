import spacy # pip install spacy
import re  # built-in rgeex library
import phonenumbers as pn # pip install phonenumbers

def name_scrape(inputText):
    names = []
    nlp = spacy.load("en_core_web_lg") #python -m spacy download en_core_web_lg
    inputText = nlp(inputText)
    for ent in inputText.ents:
        if ent.label_ == "PERSON" and (ent.text == "Pamela" or ent.text == "Pamela Toro"):
            ## Don't do anything.
            print("Picked up Pamela's name.")
        elif ent.label_ == "PERSON" and (ent.text == "Cilinda" or ent.text == "Cilinda Brown"):
            ## Don't do anything.
             print("Picked up Cilinda's name.")
        elif ent.label_ == "PERSON":
            names.append(ent.text)
    print(names)
    return names

def email_scrape(inputText):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", inputText)
    print (emails[0:])
    return emails

###                       Regex Approach                        ###
### Basically, the regular expression (regex) lays out these rules:
### 1.) The matched string may start with '+' or '(' symbol.
### 2.) It has to be followed by a number between 1-9.
### 3.) It has to end with a number between 0-9.
### 4.) It may contain 0-9 (space) .-() in the middle.

def phone_scrape(doc):  ### Returns an array
    numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', doc)
    print(numbers)
    return numbers

def count_ints(string):
    nums = ['1','2','3','4','5','6','7','8','9','0']
    cnt = 0
    for i in range(len(string)):
        if string[i] in nums:
            cnt += 1
    return cnt
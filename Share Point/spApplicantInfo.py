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
            print(ent.text)
            names.append(ent.text)
    print(names)
    return names

def email_scrape(inputText):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", inputText)
    print (emails[0:])
    return emails

def phone_scrape(inputText):
    numbers = pn.PhoneNumberMatcher(inputText, "GB")
    
    for number in numbers:
        print(number)

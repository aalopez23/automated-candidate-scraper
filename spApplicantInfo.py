import spacy #pip install spacy
import re

name_test1= "Two before narrow not relied how except moment Dejection assurance led certainly So gate at not only nonpoint. Betrayed at properly it of Jonathan Nguyen graceful on. Dinner abroad depart ye turned hearts as wished Therefore would allowance too perfectly gentleman supposing man his now Antonio Lopez Families goodness all eat out bed steepest servants. Explained the incommode sir improving northward immediate eat Man denoting received you sex possible you Shew Park own loud son door less yet"

def name_scrape(doc):
    nlp = spacy.load("en_core_web_lg") #pythong -m spacy download en_core_web_lg
    doc = nlp(doc)
    for ent in doc.ents:
        if ent.label_ == "PERSON" and (ent.text == "Pamela" or ent.text == "Pamela Toro"):
            ## Don't do anything.
            print("Picked up Pamela's name.")
        elif ent.label_ == "PERSON" and (ent.text == "Cilinda" or ent.text == "Cilinda Brown"):
            ## Don't do anything.
             print("Picked up Cilinda's name.")
        elif ent.label_ == "PERSON":
            print(ent.text, ent.label_)
            
name_scrape(name_test1)


email_test1 = "Please contact us at contact@tutorialspoint.com for further information."
def email_scrape(doc):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", doc)
    print (emails)
    
email_scrape(email_test1)
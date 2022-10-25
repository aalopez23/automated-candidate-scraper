import spacy #pip install spacy

test1= "Two before narrow not relied how except moment Dejection assurance led certainly So gate at not only nonpoint. Betrayed at properly it of Jonathan Nguyen graceful on. Dinner abroad depart ye turned hearts as wished Therefore would allowance too perfectly gentleman supposing man his now Antonio Lopez Families goodness all eat out bed steepest servants. Explained the incommode sir improving northward immediate eat Man denoting received you sex possible you Shew Park own loud son door less yet"

def name_scrape(test):
    nlp = spacy.load("en_core_web_lg") #pythong -m spacy download en_core_web_lg
    doc = nlp(test)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            print(ent.text, ent.label_)
        elif ent.label_ == "PERSON" and (ent.text == "Pamela" or ent.text == "Pamela Toro"):
            ## Don't do anything.
            print("Picked up Pamela's name.")
        elif ent.label_ == "PERSON" and (ent.text == "Cilinda" or ent.text == "Cilinda Brown"):
            ## Don't do anything.
             print("Picked up Cilinda's name.")
            
name_scrape(test1)
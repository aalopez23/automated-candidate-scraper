import spacy

NER = spacy.load("en_core_web_sm")
doc = NER("testDOC.txt")
for ent in doc.ents:
    print(ent.text, "|", ent.label_)
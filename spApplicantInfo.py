import spacy #pip install spacy
import re
import phonenumbers as pn

name_test1= "Two before narrow not Pamela Toro relied how except moment Dejection assurance led Cilinda Brown certainly So gate at not only nonpoint. Betrayed at properly it of Jonathan Nguyen graceful on. Dinner abroad depart ye turned hearts as wished Therefore would allowance too perfectly gentleman supposing man his now Antonio Lopez Families goodness all eat out bed steepest servants. Explained the incommode sir improving northward immediate eat Man denoting received you sex possible you Shew Park own loud son door less yet"
name_test2= "https://www.linkedin.com/in antonio lopez 13a48a212/"
def name_scrape(doc):
    names = []
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
            print(ent.text)
            names.append(ent.text)
    print(names)
    return names
            
name_scrape(name_test2)


email_test1 = "Please contact us at contact@tutorialspoint.com for further information. jsn006@ucsd.edu and I also want to test this one: 36363@fjd"
def email_scrape(doc):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", doc)
    print (emails[0])
       
email_scrape(email_test1)

# Test Strings
#phone_example = "(209) 921-6581"  # U.S phone 

text = "Hi Jane, thank you for reaching out to learn more about Data Science Sphere! The best way to learn more about us is to call us. Feel free to call us at 020 8366 1177 or at 020 8785 7465. There will be no obligation to sign up to our newsletter after the call! Best regards."


def phone_scrape(text):
    #parsed_number = pn.parse(phone_example, "US") # Returns U.S country code (+1) and phone number
    #print(parsed_number)

    numbers = pn.PhoneNumberMatcher(text, "GB")
    
    for number in numbers:
        print(number)
        

### Run 
#phone_scrape(phone_example)
phone_scrape(text)
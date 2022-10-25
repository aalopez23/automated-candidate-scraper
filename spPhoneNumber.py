import phonenumbers as pn
import re

# Test Strings
phone_example = "3774728288"  # U.S phone 
text = "Hi Jane, thank you for reaching out to learn more about Data Science Sphere! The best way to learn more about us is to call us. Feel free to call us at 020 8366 1177 or at 020 8785 7465. There will be no obligation to sign up to our newsletter after the call! Best regards."


def phone_scrape(text):
    parsed_number = pn.parse(phone_example, "US") # Returns U.S country code (+1) and phone number
    print(parsed_number)


    numbers = pn.PhoneNumberMatcher(text, "GB")  # Returns phone # character start and end positions, followed by actual phone number
    for number in numbers:
        print(number)
        

### Run 
""" phone_num1 = str(phone_scrape(phone_example))
phone_num2 = str(phone_scrape(text)) """

print(phone_scrape(phone_example))

def find_numbers(doc):
    numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', doc)
    print(numbers)
    
find_numbers(text)
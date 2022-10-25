import phonenumbers as pn

phone_number_string = "(209) 921-6581"
parsed_number = pn.parse(phone_number_string, "US")

print(parsed_number)

text = "Hi Jane, thank you for reaching out to learn more about Data Science Sphere! The best way to learn more about us is to call us. Feel free to call us at 020 8366 1177 or at 020 8785 7465. There will be no obligation to sign up to our newsletter after the call! Best regards."

numbers = pn.PhoneNumberMatcher(text, "GB")

for number in numbers:
    print(number)
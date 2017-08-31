# Fancy Phone number
phone_number = input("Please enter your ten-digit phone number: ")
# Split the string into several str([]) components, adding the necessary punctuation
print (f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}")

def fancy_phone(number):
    print(f"({number[0:3]}) {number[3:6]}-{number[6:]}")

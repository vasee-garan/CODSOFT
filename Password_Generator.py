import random
import string
lower_case_letters = string.ascii_lowercase

upper_case_letters = string.ascii_uppercase
symbols = string.punctuation
numbers = string.digits

combination = lower_case_letters + upper_case_letters + symbols + numbers
password_length = int(input("Enter the length of Password :"))
password = "".join(random.sample(combination,password_length))
print("The Generated Password is :",password)

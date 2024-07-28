import string
import random
def Emailgenerator ():
    chars_after_at = int(input("How much chars you want in gmail b/w 4 to 20"))
    emails = int(input("How many emails do you want: "))
    
    if((chars_after_at < 4) or (chars_after_at > 20)):
        print("Enter chars b/w 4 to 20 max!")
        exit()
    else:
        for i in range(emails):
            letters_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase]
            
            letterrs_list_to_str ="".join(letters_list)
            
            email_format = "@gmail.com"
            
            email_generated = "".join(random.choices(letterrs_list_to_str, k= chars_after_at)) +email_format
            
            print(email_generated)
Emailgenerator()
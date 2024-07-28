email = input("Enter your email: ")
#name23@gmail.com
k,j, d=0,0,0
if len(email) <= 6: # 1 Email size must be greater or equal to 6
    if email[0].isalpha(): # 2 Email's first letter never digit
        if ("@"in email) and (email.count("@")==1): # 3 In email must be only one @
            if (email[-4]==".") ^ (email[-3]=="."): # 4 In email '.'must be have at [-3] position
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d = 1  
                              
                if k==1 or j==1 or d==1:
                    print("Invalid email")
            else:
                print("Invalid email")
        else:
            print("Invalid email") 
    else:
        print("Invalid email")
else:
    print("Invalid Email.")
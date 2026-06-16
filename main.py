user_name = "SQZ0111"

#Datenstrukturen
#Array
user_names = ["SQZ0111","SLK111","ReAm","ABC!"]

user_names_containing_s = []
#print(user_names[:3]) #equivalent zu print(user_names[0:3])
#print(user_names[::-2]) #print(user_names[0:4:2])

#user_names.append("NewUser")

#print(user_names)

user_names_uppercase = []
    
for username in user_names:
    #if "s" in username or "S" in username:
    #    user_names_containing_s.append(username)
    
    if username.find("s") != -1 or username.find("S") != -1:
        user_names_containing_s.append(username)
    else:
        print(f"{username} contains no s|S")
    
    ##Makes String elements uppercase
    #username_uppercase = username.upper()
    #user_names_uppercase.append(username_uppercase) 
    
    #ist äquivalent zu oben 
    #user_names_uppercase.append(username.upper())
    
    
print(user_names_containing_s)
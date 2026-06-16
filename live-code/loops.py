user_tries = 0
# while True:
#     if user_tries == 3:
#         print("End")
#         break
#     user_name = input("Input username\n")
#     if user_name == "admin":
#         print("welcome!")
#         break
#     user_tries += 1 #user_tries = user_tries + 1

for i in range(0,3):
    user_name = input("Input username\n")
    if user_name == "admin":
        print("welcome!")
        break

print("End")

# for i in range(0,4):
#    print(i)

# for i in "text":
#     print(i)
# Test

#1. Ersetze aalle while schleifen durch for Schleifen (nach Möglichkeit)
print("Welcome to the Voter Registration System!")
print(r'''
             __..--"""""""""""""""""::|
     __..--""                _..--""  |
   .:______________________.:| |      |
   |       __________      ||| |    ()|
   | __====::::::::::====__||| |()    |
   ||\_____________________||| |      |
   |||                     ||| |      |
   |||                     ||| |      |
   |||                     ||| |      |
   |||_____________________||| |      |
   |||---------------------||| |      |
   ||| :-----------------: ||| |      |
   ||| |              32x| ||| |      |
   ||| '"""""""""""""""""' ||| |      |
   ||| o = =       o [] [] ||| |      |
   |||---------------------||| |      |
   |||"""""""""""""""""""""||| |      |
   |||    |==========|     ||| |      |
   |||    | o """  ()|     ||| |      |
   |||_____________________||| |      |
   ||/_____________________||| |      |
   ||                      ||| |      |
   |'.                    .'|| |      |
   | '--__           __--'  || |      |
   |      """""""""""       || |      |
   |                        || |      |
   |                        || |      |
   |       |_____|          || |      |
   |       (____(|          || |      |
   |       |     |          || |      |
   |                        || |      |
   |       ||   ||          || |      |
   |       ((   ((          || |      |
   |       ||   ||          || |      |
   |                        || |      |
   |                        || |      |
   |  .: : : : : : : : .    || |    ()|
   |  |: : : : : : : : |    || |      |
   |  |':':':':':':':':|    || |()    |
   |  | '.'.'.'.'.'.'.'|    || |      |
   |  |/""""""""""""""";.   || |     .'
   |  :      x          '.  || |   .'
   |  :      x:          :  || | .'
   | ."      x:          ". || :'
   |_:____________________:_|:' 
''')
# voter registration system
name = input("What is your name?" )
if name:
    print("Your name is valid.")
else:
    print("Your name is invalid.")
date_of_birth = int(input("What is your Date of Birth? "))
calculated_age = 2026 - date_of_birth
age = calculated_age
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
nin = int(input("What is your National Identification Number (NIN)? "))
if nin == 11:
    print("Your NIN is valid.")
else:
    print("Your NIN is invalid.")
gender = input("What is your gender? ")
if gender in ["Male", "Female"]:
    print("Your gender is valid.")
else:
    print("Your gender is invalid.")
phone_number = int(input("What is your phone number? "))
if phone_number == 11:
    print("Your phone number is valid.")
else:
    print("Your phone number is invalid.")
email_address = input("What is your email address? ")
if email_address.endswith("@gmail.com") or email_address.endswith("@yahoo.com") or email_address.endswith("@outlook.com"):
    print("Your email address is valid.")
else:
    print("Your email address is invalid.")
state = input("What state do you live in? ")
if state in ["Lagos", "Abuja", "Oyo", "Kaduna", "Enugu",  "Delta", "Ogun", "Edo", "Ekiti", "Osun"]:
    print("You are eligible to vote in your state.")
else:
    print("You are not eligible to vote in your state.")
local_government_area = input("What is your Local Government Area (LGA)? ")
if local_government_area in ["Ikeja", "Mushin", "Surulere", "Yaba", "Alimosho", "Ifako-Ijaiye", "Kosofe", "Shomolu", "Agege", "Apapa", "Ijebu-ode", "Abeokuta North", "Abeokuta South", "Ewekoro", "Ijebu East", "Ijebu North", "Ijebu North East", "Ijebu South West", "Ketu North", "Ketu South", "Odogbolu", "Sagbama", "Yenagoa","Bwari", "Gwagwalada", "Kuje", "Abaji", "Kwali"]:
    print("You are eligible to vote in your Local Government Area.")
else:
    print("You are not eligible to vote in your Local Government Area.")
residential_address = input("What is your residential address? ")
if residential_address:
    print("Your residential address is valid.")
else:
    print("Your residential address is invalid.")
country = input("What is your country? ")
if country == "Nigeria":
    print("You are eligible to vote in Nigeria.")
else:
    print("You are not eligible to vote in Nigeria.")
registration_status = input("Have you registered to vote? (yes/no) ")
if registration_status == "yes":
    print("You are registered to vote.")
else:
    print("You are not registered to vote.")

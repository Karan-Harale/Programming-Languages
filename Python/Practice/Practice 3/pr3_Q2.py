letter='''Dear<|name|>, 
Greetings from xyz coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Ashu

You're Selected! 

<|Date|>'''

name= input("Enter Name \n")
date= input("Enter Date \n")
letter=letter.replace("<|name|>", name)
letter=letter.replace("<|Date|",date)

print(letter)
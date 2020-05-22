print("*".center(80, '*'))
print("Welcome to Algorithm for Manjila and Seeman classification of jugular " + \
      "bulb \nlocation - Written on Python 3.7.2, Dr Hrishikesh Sarkar MCh")

print("*".center(80, '*'))
print()
print("Enter 0 for no, 1 for yes")
print()
print("Is there a visible jugular bulb?") 
Bulb = int(input())

if Bulb == 0:
    print("This is a Manjila and Seeman Type 1 location.")

if Bulb == 1:
    print ("Are there multiple dehiscences present in around IAC, middle ear?")

Multiple = int(input())

if Multiple == 1:
    print("This is a Manjila and Seeman Type 5 location")
else:
    print("Where is the location of Jugular bulb?" + \
          "\nEnter 0 for inferior margin of posterior semicircular canal," + \
          "\nEnter 1 for inferior margin of internal auditory canal and," + \
          "\nEnter 2 for above inferior margin of auditory canal")

Location = int(input())

if Location == 0:
     print("Is middle ear dehiscence present?: Enter 0 for no and 1 for yes.")
     middle = int(input())
     if middle == 0:
         print("This is a Manjila and Seeman Type 2a location.")
     else:
         print("This is a Manjila and Seeman Type 2b location. ")
     
if Location == 1:
    print("Is middle ear dehiscence present?: Enter 0 for no and 1 for yes.")
    iac = int(input())
    if iac == 0:
         print("This is a Manjila and Seeman Type 3a location.")
    else:
         print("This isa Manjila and Seeman Type 3b location.")
     
if Location == 2:
    print("Is internal auditory dehiscence present?: Enter 0 for no and 1 for yes.")
    dahi = int(input())
    if dahi == 0:
         print("This is a Manjila and Seeman Type 4a location.")
    else:
         print("This is a Manjila and Seeman Type 4b location.")
     
print("*".center(80, '*'))

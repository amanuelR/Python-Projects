
def print_opposite_case( sentence:str)->None:
    for each_ch in sentence:
        changed_ch = get_changed_case(each_ch) # assigning a function value to a variable
        print(changed_ch,end='')


#   This function accepts a character and returns its lower or upper case
#   in case of Alphabets, for numbers and space it returns the orginal character
def get_changed_case(ch:str)->str:
    if ord(ch) >=  65 and ord(ch) <=  90:
        # find ASCII decimal number and add 32 to find the upper case,
        # then change it to a character after that return the character
        return chr(ord(ch) + 32) 
    elif ord(ch) >=  97 and ord(ch) <=  122:
        # find ASCII decimal number and substract 32 to find the lower case,
        # then change it to a character after that return the character
        return chr(ord(ch) - 32)
    else:
        return ch   #   return orignal 
    
#   This loop will iterate continously
#   untill the user decided to enter q,which is quit.    
while True:
    s = input("Enter a string to convert case to upper or lower \
    (Press 'q' to exit):\n")
    if(s == 'q'):
        break #exits the program
    print_opposite_case(s) # call a function and pass an argument
    print("\n")
print("Goodbye")

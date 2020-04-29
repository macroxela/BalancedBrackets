##########################################################################################################
#  Balanced Brackets Verifier                                                                            #
# • For the balanced parentheses problem, checks if any kind of brackets are balanced                    #
#   Brackets can be mixed including () [] and {}                                                         #
# • Creates random sequences of brackets                                                                 #
#                                                                                                        #
# Alex Marroquin                                                                                         #
# 29 April 2020                                                                                          #
#                                                                                                        #
##########################################################################################################

import random
##########################################################################################################

#Given stack st, opening character a, closing character b and character c
#it checks if c matches the opening or closing character and modifies the
#stack accordingly
def CheckMatch(st, a, b, c):
    val = False
    if c == a:
        st.append(c)
        val = True
    elif c == b and len(st) == 0: #In case there are no ([{ left
        val= False
    elif c == b and st[len(st)-1] != a: #Check if they match
        val = False
    elif c == b:
        st.pop()
        val =  True
    return val

#Checks if the # of ( [ { equals the # of )]} and if they match
#Abstracts away the stack manipulation & match checking
def CheckBalancedMatching2(a):
    stack = []
    if len(a) == 0:
        return False
    for i in a:
        val = 5 
        #For ()
        if i == "(" or i == ")":
            val = CheckMatch(stack, "(", ")", i)
        #For []
        if i == "[" or i == "]":
            val = CheckMatch(stack, "[", "]", i)
        #For {}
        if i == "{" or i == "}":
            val = CheckMatch(stack, "{", "}", i)
        #In case there was no match or extra )]}
        if not val:
            return val     

    #If stack is empty then (), [], and {} are balanced and matching
    if len(stack) == 0:
        return True
    else:
        return False

#Checks if the # of ( [ { equals the # of )]} and if they match
def CheckBalancedMatching1(a):
    stack = []
    if len(a) == 0:
        return False
    for i in a:
        #For parentheses ()
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) == 0: #In case there are no ( left
            return False
        elif i == ")" and stack[len(stack)-1] != "(": #Check if they match
            return False
        elif i == ")":
            stack.pop()
            
        #For brackets []
        if i == "[":
            stack.append(i)
        elif i == "]" and len(stack) == 0: #In case there are no [ left
            return False
        elif i == "]" and stack[len(stack)-1] != "[": #Check if they match
            return False
        elif i == "]":
            stack.pop()

        #For curly braces {}
        if i == "{":
            stack.append(i)
        elif i == "}" and len(stack) == 0: #In case there are no } left
            return False
        elif i == "}" and stack[len(stack)-1] != "{": #Check if they match
            return False
        elif i == "}":
            stack.pop()

    #If stack is empty then (), [], and {} are balanced and matching
    if len(stack) == 0:
        return True
    else:
        return False
##########################################################################################################
#Only checks if the # of ( equals the # of ) as well as [] and {}
#Does not check if they close properly
def CheckBalanced(a):
    stackP = []
    stackB = []
    stackC = []
    if len(a) == 0:
        return False
    for i in a:
        #For parentheses ()
        if i == "(":
            stackP.append(i)
        elif i == ")" and len(stackP) == 0: #In case there are no ( left
            return False
        elif i == ")":
            stackP.pop()
            
        #For brackets []
        if i == "[":
            stackB.append(i)
        elif i == "]" and len(stackB) == 0: #In case there are no [ left
            return False
        elif i == "]":
            stackB.pop()

        #For curly braces {}
        if i == "{":
            stackC.append(i)
        elif i == "}" and len(stackC) == 0: #In case there are no { left
            return False
        elif i == "}":
            stackC.pop()

    #If all stacks are empty then (), [], and {} are balanced
    if  len(stackP) == 0 and len(stackB) == 0 and len(stackC) == 0:
        return True
    else:
        return False

##########################################################################################################

#Checks for equal amount of two characters
def CheckBalancedChar(a, char1, char2):
    stack = []
    if len(a) == 0:
        return False
    for i in a:
        if i == char1:
            stack.append(i)
        elif i == char2 and len(stack) == 0: #In case there are no 1st char left
            return False
        elif i == char2:
            stack.pop()

    #If all stacks are empty then characters are balanced
    if len(stack) == 0:
        return True
    else:
        return False

#Checks for balanced ()
def CheckBalancedP(a):
    stack = []
    if len(a) == 0:
        return False
    for i in a:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) == 0: #In case there are no ( left
            return False
        elif i == ")":
            stack.pop()

    #If all stacks are empty then parentheses are balanced
    if len(stack) == 0:
        return True
    else:
        return False
##########################################################################################################
#The code below creates a string of random () or mix of (), [], and {} for testing purposes

#Creates string of ()
def par_generator():    
    parenthesis = ""
    length = random.randint(1, 25) #make sure for randint(a,b) b-a is even or it will generate only false cases
    for i in range(1, length): #Length of string
        if random.randint(1,100)%2 == 0:
            parenthesis += "("
        else:
            parenthesis += ")"
    return parenthesis

#Creates string of () [] {}
def pbc_generator():    
    parenthesis = ""
    length = random.randint(1, 31) #make sure for randint(a,b) b-a is even or it will generate only false cases
    for i in range(1, length): #Length of string
        dummy = random.randint(1,60)
        if dummy%6 == 0:
            parenthesis += "("
        elif dummy%6 == 1:
            parenthesis += ")"
        elif dummy%6 == 2:
            parenthesis += "["
        elif dummy%6 == 3:
            parenthesis += "]"
        elif dummy%6 == 4:
            parenthesis += "{"
        else:
            parenthesis += "}"
    return parenthesis

#Creates a string using two given characters
def char_generator(a, b):
    characters = ""
    length = random.randint(1, 25) #make sure for randint(a,b) b-a is even or it will generate only false cases
    for i in range(1, length): #Length of string
        if random.randint(1,100)%2 == 0:
            characters += a
        else:
            characters += b
    return characters

#Creates a string using characters from the given list
def char_generator_list(char_list):
    characters = ""
    length = random.randint(1, 25) #make sure for randint(a,b) b-a is even or it will generate only false cases
    num_char = len(char_list) #Number of characters
    for i in range(1, length):
        ran = random.randint(1, num_char*100)
        for j in range(0,num_char):
            if ran%num_char == j:
                characters += str(char_list[j])
        
    return characters

##########################################################################################################
'''
#Code below for testing purposes
#Uncomment to test

#()
p = []
truelistp = []

for i in range(1, 1000):
    p.append(par_generator())

for i in p:
    ch = CheckBalancedP(i)
    if ch:
        truelistp.append(i)

print("Only ()")
for i in truelistp:
    print(i)

print(" ")

#()[]{} without matching
pbc = []
truelist1 = []

for i in range(1, 1000):
    pbc.append(pbc_generator())

for i in pbc:
    ch1 = CheckBalanced(i)
    if ch1:
        truelist1.append(i)

print("()[]{} without matching")
for i in truelist1:
    print(i)

print(" ")


#()[]{} with matching
truelist2 = []

for i in pbc:
    ch2 = CheckBalancedMatching1(i)
    if ch2:
        truelist2.append(i)

print("()[]{} with matching")
for i in truelist2:
    print(i)

print(" ")

#()[]{} with matching & abstraction
truelist3 = []

for i in pbc:
    ch3 = CheckBalancedMatching2(i)
    if ch3:
        truelist3.append(i)

print("()[]{} with matching & abstraction")
for i in truelist3:
    print(i)

'''

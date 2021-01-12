# WRITE YOUR NAME and YOUR COLLABORATORS HERE
# Ayush Kapoor - 11638482 
from collections import defaultdict
#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

def opPop():
    if len(opstack) > 0:
        counter = opstack[-1]
        opstack.pop()
    else:
        print("Sorry! Empty List")
        return 0
    return (counter)
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)
    return opstack

#-------------------------- 16% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

def dictPop():
    if (len (dictstack) > 0):
        counter = dictstack[-1]
        dictstack.pop()
    return (counter)

    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    global index 
    dictstack.append(d)
    return dictstack
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.


def define(name, value, scope):
    if scope == 'static':
        if len(dictstack) == 0:
            dictPush((0, {name:value}))
        else:
            currentindex = len(dictstack) - 1
            dictstack[currentindex][1][name] = value
    elif scope == 'dynamic':
        if len(dictstack) == 0:
            dictPush((0, {name: value}))
        else:
            temp = dictstack[-1]
            (key1, value1) = temp
            value1[name] = value


def lookup(dictstack, name, scope):
    if name.startswith('/') == False:
        name = '/' + name
    if scope == 'static':
        try:
            temp = dictstack[-1][0]
        except IndexError:
            temp = 0
        incr = temp + 1 - len(dictstack)
        for a,b in dictstack[::-1]:
            for x1, y1 in b.items():
                if x1 == name:
                    opPush(y1)
                    return y1
            return lookup(dictstack[:incr], name,scope) # Recursive function call 
    elif scope =='dynamic':
        for (key,value) in dictstack[::-1]:
            for (key_1,value_1) in value.items():
                if key_1 == name:
                    opPush(value_1)
                    return (value_1)
    print("Sorry but the name",name,"was not found")



    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        first = opstack.pop()
        second = opstack.pop()
        if isinstance(first, int) and isinstance(second, int):
            opPush(first + second)
        else:
            opPush(first)
            opPush(second)
    else:
        print("Error:add expects 2 operands.")

def sub():
    if len(opstack) > 1:
        first = opstack.pop()
        second = opstack.pop()
        if isinstance(first, int) and isinstance(second, int):
            opstack.append( second - first)
        else:
            print("Error sub, need BOTH to be integers")
            opPush(first)
            opPush(second)
    else:
        print("Error: None of them are integers, or need operands")

def mul():
    if len(opstack) > 1:      
        first = opstack.pop()
        second = opstack.pop()
        if isinstance(first, int) and isinstance(second, int):
            opPush (first * second)
        else:
            print("Error! Mul")
            opPush(first)
            opPush(second)
    else:
        print("Error! Mul needs to operands")

def eq():
    if len(opstack) > 1:
        first = opstack.pop()
        second = opstack.pop()
        if isinstance(first, int) and isinstance(second, int):
            if(second != first):
                opstack.append(False) 
            else:
                opstack.append(True) 
        else:
            print("Error, eq - Need BOTH to be integer")
            opPush(first)
            opPush(second)
    else:
        print("Error, eq needs two integers")

def lt():
    if len(opstack) > 1:
        first = opstack.pop()
        second = opstack.pop()
        if isinstance(first, int) and isinstance(second, int):
            if (first > second):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error, lt needs BOTH to be integers")
            opPush(first)
            opPush(second)
    else:
        print("Error, lt needs two integers")

def gt():
    if len(opstack) > 1:
        first = opstack.pop()
        second = opstack.pop()
        if type(first) == int and type (second) == int:
            if (first < second):
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error, gt needs BOTH to be integers")
    else:
        print("Error, gt needs two integers")
#--------------------------- 20% -------------------------------------
# String operators: define the string operators length, get, getinterval,  putinterval, search
def length():
    if (len(opstack) > 0):
        get_string = opstack.pop()
        if type(get_string) == str:
            opPush(len(get_string)-2)
        else:
            print("Error ,length needs a string")
            opPush(get_string)
    else:
        print("Error,length needs an argument")
    
def get():
    if (len (opstack) > 0):
        index_to_get = opstack.pop()
        sample_str = opstack.pop()
        if(isinstance(sample_str, str)):
            temp = sample_str[index_to_get + 1]
            opPush(ord(temp)) #return an integer representing the UNIcode point of the charactar
        else:
            print("Error, get needs a string argument")
            opPush(sample_str)
            opPush(index_to_get)
    else:
        print("Error,get needs more arguments")

def getinterval():
    if (len (opstack) > 2):
        compute = opstack.pop()
        index_to_get = opstack.pop()
        sample_str = opstack.pop()
        if(type(sample_str) == str):
            temp = sample_str[(index_to_get + 1):(index_to_get + compute + 1)]
            temp = "(" + temp + ")"
            opPush(temp)
        else:
            print("Error, getinterval needs a string")
            opPush(sample_str)
            opPush(index_to_get)
            opPush(compute)
    else:
        print("Error, getinterval needs more arguments")

def putinterval():
    if(len(opstack)>2):
        str2=opstack.pop()
        index=opstack.pop()
        str1=opstack.pop()
        if(type(str1) == str):
            ans=str1[:index+1] + str2[1:len(str2)-1] +str1[len(str2)-1+index:]
            for i in range(0,len(opstack)):
                if (opstack[i]==str1):
                    opstack[i] = ans
                else:
                    pass
            if(len(dictstack)!=0):
                for (k,v) in dictstack:
                    for k1,v1 in v.items():
                        if(v==str1):
                            i[k]=ans
        else:
             print("Error: expected string argument")
             opPush(str1)
             opPush(index)
             opPush(str2)
    else:
        print("Error: Not enough arguments in opStack to perform getinterval()")


def search():
    if(len(opstack)>0):
        first=opstack.pop()
        dup = first
        string_to_get = opstack.pop()
        first=first[1:len(first)-1]
        if first in string_to_get:    
            x=string_to_get.split(first,1)
            x[1] = "(" +x[1]
            x[0] = x[0]+")"
            opPush(x[1])
            opPush(dup)
            opPush(x[0])
            opPush(True)
        else:
            opPush(string_to_get)
            opPush(False)
    else:
        print(" Error, search needs more arguments ")


#--------------------------- 18% -------------------------------------
# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore

def evaluateArray(aInput, scope):
    list1 = []
    counter = 0
    opstack.append('[') #Step over arrary symbol 
    for i in aInput:
        if type(i) == int or type(i) == bool:
            opPush(i)
        elif type(i) == str:
            if i.startswith('('):
                opPush(i)
            elif i in all_func.keys(): #dictionary defined at the bottom with all postscript inbuilt functions
                operation = all_func[i]
                operation()
            else:
                lookup(dictstack,i, scope)
    for counter in opstack[::-1]: #Reverse the opstack order
        if counter == '[':
            break
        else:
            list1.append(opPop())
    opstack.pop() #Popping from opstack
    #Last element of opstack would be last element of the return list
    list1.reverse() 
    return (list1)
    #should return the evaluated array

def aload():
    curr_value = opPop()
    for item in curr_value:
        opPush(item)
    opPush(curr_value)
    return opstack

def astore():
    curr_value = opPop()
    for item in range(len(curr_value)):
        curr_value[item] = opPop()
    curr_value = list(curr_value[::-1])
    opPush(curr_value)

#--------------------------- 6% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, stack
def dup():
    if len(opstack) > 0:
        first = opPop()
        opstack.append(first)
        opstack.append(first)
    else:
        print("Error, interpreter needs a list to duplicate")

def copy():
    if(len(opstack) > 0):
        addup = opPop()
        dup = [] #Empty list
        for  x in range(0,addup):
            dup.append(opPop())
        for item in dup[::-1]:
            opstack.append(item)
        for item in dup[::-1]:
            opstack.append(item)
    else:
        print("Error: interpreter needs an argument to copy")

def count():
    opstack.append(len(opstack))

def pop():
    if len (opstack) > 0:
        opstack.pop()

def clear():
    opstack [:] = []
    dictstack[:] = []

def exch():
    v1 = opPop()
    v2 = opPop()
    opPush(v1)
    opPush(v2)

def stack():
    print("==============")
    if (len(opstack) > 0):
        for each in range(len(opstack)):
                print(opstack[-(each + 1)])

    print("==============")

    dictIndex = len(dictstack) - 1
    while(dictIndex != -1):
        m = dictIndex #m is the index that will identify the dictionary
        n = dictstack[dictIndex][0] #n is the index that represents the static link for the dictionary printed

        print("----" + str(m) + "----" + str(n) + "----")
        for i in dictstack[dictIndex][1]:
            print(i + "    " + str(dictstack[dictIndex][1].get(i)))
        dictIndex = dictIndex - 1
    print("==============")


def staticLink(dictstack,name):
    if name[0] != '/':
        name = '/' + name
    val = dictstack[-1][0]
    i = val + 1 - len(dictstack)
    for a,b in dictstack[::-1]:
        for x1, y1 in b.items():
            if x1 == name:
                return a 
        return staticLink(dictstack[:i], name)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.
def psDict():
    opPop()
    opPush({})
    return dictstack

def begin():
    val = opstack.pop()
    dictPush({})
    
def end():
    dictPop()

def psDef():
    value = opPop()
    key = opPop()
    if type(key) ==str:
        define(key, value,'dynamic')
    else:
        print("Error, psdef needs a string")
        opPush(key)
        opPush(value)
#PART2
import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s\(\)!][a-zA-Z-?0-9_\s\(\)!]*[\]]|[\()][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\)]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)  

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            res.append(groupMatch(it))
        else:
            try:
                res.append(int(c))
            except ValueError:
                if(c.startswith('[')):
                    stripped =c.strip('][').split(' ') #Eliminate/Strip the unnecessary symbols.
                    for item in range(0,len(stripped)):
                        try:
                            stripped[item]=int(stripped[item]) #Confirmation
                        except ValueError:
                            pass #Step over
                    res.append(stripped)
                else:
                    res.append(c)
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            try:
                res.append(int(c))
            except ValueError:
                if(c.startswith('[')):
                    stripped =c.strip('][').split(' ') #Eliminate/Strip the unnecessary symbols.
                    for item in range(0,len(stripped)):
                        try:
                            stripped[item]=int(stripped[item]) #To make sure(confirmation)
                        except ValueError:
                            pass
                    res.append(stripped)
                else:
                    res.append(c)
    return {'codearray':res}


def psif(scope):
    first = opPop()
    second = opPop()
    if type(second) == bool and second == True: #Check the condition of the bool term
        interpretSPS(first, scope) 
    else:
        opstack.append(second) 
        opstack.append(first)

def psifelse(scope):
    first = opstack.pop()
    second = opstack.pop()
    third = opstack.pop()
    if type(third) == bool and third == True:
        interpretSPS(second, scope) #Either this 
    else:
        interpretSPS(first, scope) #else the first variable

def psfor(scope):
    first = opstack.pop()
    last = opstack.pop()
    counter = opstack.pop()
    it = opstack.pop()
    if (counter > 0):
        last += 1
    else:
        last -= 1
    for item in range(it, last, counter):
        opstack.append(item)
        interpretSPS(first, scope)

def interpretSPS(code, scope): # code is a code array
    for key, value in code.items():
        for item in value:
            if type(item) == str:
                if item[0] == '/':
                    opPush(item)
                elif item[0] == '(':
                    opPush(item)
                elif item == 'if':
                    psif(scope)
                elif item == 'for':
                    psfor(scope)
                elif item == 'def':
                    psDef()
                elif item == 'ifelse':
                    psifelse(scope)
                elif item in all_func.keys():
                    operation = all_func[item]
                    operation()

                else:
                    res = lookup(dictstack, item, scope)
                    if type(res) ==  dict:
                        if scope == 'dynamic':
                            dictPush((0,{}))
                        elif scope == 'static':
                            dictPush((staticLink(dictstack,item),{}))
                        interpretSPS(res, scope)
                    else:
                        pass
            elif type(item) == int or type(item) == bool or type(item) == dict: #As they yield the same implementation
                opPush(item)
            elif type(item) == list:
                opPush(evaluateArray(item, scope))
            else:
                print("Sorry, there was an error processing this argument/operation",item)

def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clear opstack and dictstack
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

#Dictionary that will be called by interpretSPS and evalArray 
all_func = {'pop':opPop,'push':opPush,'add':add,'sub':sub,'mul':mul,
            'eq':eq,'lt':lt,'gt':gt,'exch':exch,'begin':begin,
            'end':end,'dict':psDict,'def':psDef,'clear':clear,
            'length':length,'search':search,'getinterval':getinterval,
            'putinterval':putinterval,'dup':dup,'stack':stack,
            'aload':aload,'astore':astore,'count':count,'copy':copy}


def sspsTests():

    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

    testinput2 = """
    /x 4 def
    (static_?) dup 7 (x) putinterval /x exch def
    /g { x stack } def
    /f { /x (dynamic_x) def g } def
    f
    """

    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """

    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput5 = """
    /x 2 def
    /n 5  def
    /A { 1  n -1 1 {pop x mul} for} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """

    testinput7 = """
    /x [1 2 3 4] def
    /A { x aload pop add add add } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

    testinput8 = """
    /x [2 3 4 5] def
    /a 10 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """

    testinput9 = """
    /z 10 def
    /s { z stack } def
    /f { /z 20 def s } def
    f
    """

    testinput10 = """
    /z 40 def
    /J { z } def
    /D { /x 40 def J stack } def
    /B { /x 30 def /J { z } def D } def
    B
    """
    testinput11 = """
    /x [3 4] def
    /A { x aload pop add add add } def
    /C { /x [40 50] def A stack } def
    /B { /x [6] def /A { x } def C } def
    B
    """

    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4,testinput5, testinput6, testinput7, testinput8, testinput9, testinput10, testinput11]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')

if __name__ == '__main__':
    sspsTests()


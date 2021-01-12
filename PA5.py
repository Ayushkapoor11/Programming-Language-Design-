from helpPA5 import *
import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        elif(RepresentsInt(c)) :
            res.append(int(c))
        elif(c == 'True' or c == 'true'):
            res.append(True)
        elif (c == 'False' or c == 'false'):
            res.append(False)
        elif(c[:1]=='['):
            d = c[1:-1]
            D_ELEM = d.split()
            for index, i in enumerate(D_ELEM):
                if(RepresentsInt(i)==True):
                    D_ELEM[index] = int(i)
                elif(i == 'True' or i == 'true'):
                    D_ELEM[index] = True
                elif (i == 'False' or i == 'false'):
                    D_ELEM[index] = False
               
            res.append((len(D_ELEM),D_ELEM))
        else:
            res.append(c)
    return False

def groupMatchlist(it):
    res = []
    for c in it:
        if c == ']':
            return res
        elif c=='[':
            
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        elif(RepresentsInt(c)) :
            res.append(int(c))
        elif(c == 'True' or c == 'true'):
            res.append(True)
        elif (c == 'False' or c == 'false'):
            res.append(False)
        else:
            res.append(c)
    return False


# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if (c == ','):
            continue
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            continue
        elif c=='{':
            res.append(groupMatch(it))
        elif isinstance(c,list):
            res.append((len(c),c))
        elif(c[:1]=='['):
            d = c[1:-1]
            D_ELEM = d.split()
            for index, i in enumerate(D_ELEM):
                if(RepresentsInt(i)==True):
                    D_ELEM[index] = int(i)
                elif(i == 'True' or i == 'true'):
                    D_ELEM[index] = True
                elif (i == 'False' or i == 'false'):
                    D_ELEM[index] = False
               
            res.append((len(D_ELEM),D_ELEM))  
        elif(RepresentsInt(c)==True):
            res.append(int(c))
        elif(c == 'True' or c == 'true'):
            res.append(True)
        elif (c == 'False' or c == 'false'):
            res.append(False)
        else:
            res.append(c)
    return res

# COMPLETE THIS FUNCTION 
# Write auxiliary functions if you need them. This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
def interpretSSPS(code,scope): # code is a code array
    for c in code:
        #print(c)
        getScope(scope)
        if(RepresentsInt(c)):
            opPush(int(c))
        elif(c[0]=='/'):
            opPush(c)
        elif(c=='def'):
            psDef()
        elif(c=='mul'):
            mul()
        elif(c=='add'):
            add()
        elif(c=='sub'):
            sub()
        elif(c=='aload'):
            aload()
        elif (c=='gt'):
            gt()
        elif (c=='lt'):
            lt()
        elif (c == 'gt'):
            gt()
        elif (c == 'eq'):
            eq()
        elif (c == 'astore'):
            astore()
        elif (c=='get'):
            get()
        elif (c=='put'):
            put()
        elif (c=='length'):
            length()
        elif (c=='exch'):
            exch()
        elif (c=='dup'):
            dup()
        elif (c=='copy'):
            copy()
        elif (c=='count'):
            count()
        elif (c=='pop'):
            opPop()        
        elif (c=='clear'):
            clear()
        elif (c=='stack'):
            stack()
        elif (c=='dict'):
            psDict()
       
        elif (c == 'ifelse'):
            fal_cond = operationsopstack.pop()
            true_cond = operationsopstack.pop()
            if(operationsopstack.pop()==True):
                interpretSSPS(true_cond,scope)
            else:
                interpretSSPS(fal_cond,scope)
                operationsopstack.reverse()
        elif (c == 'if'):
            operationsopstack.reverse()
            boool = operationsopstack.pop()
            operation = operationsopstack.pop()
            if(boool==True):
                operationsopstack.reverse()
                #operationsopstack.pop()
                interpretSSPS(operation,scope)
        elif (isinstance(c,list)):
            opPush((c))
        elif isinstance(c,tuple):
            opPush(c)
        elif (c == 'for'):
            op = operationsopstack.pop()
            final = operationsopstack.pop()
            incr = operationsopstack.pop()
            init = operationsopstack.pop()
            #THIS IS THE ADDED PART AFTER DEBUGGING WITH PROF.
            #BEGIN
            if(incr>0):
                final+=1
            else:
                final-=1
            #END
            for i in range(init,final,incr):
                opPush(i)
                interpretSSPS(op,scope)
                operationsdictstack.pop()
        elif(c == 'true'):
            opPush(True)
        elif(c == 'false'):
            opPush(False)
        else:
            res = lookup(c,scope)
            if(res==None):
                continue
            if isinstance(res,list):
                interpretSSPS(res,scope)
                operationsdictstack.pop()
            else:
                opPush(res)
        #print(operationsopstack)
        #print(operationsdictstack)



#clears both stacks
def clearBoth():
    operationsopstack[:] = []
    operationsdictstack[:] = []
        
        
s =  """
            /x [1 2 3 4] def
            /A { x length } def
            /C { /x [10 20 30 40 50 60] def A stack } def
            /B { /x [6 7 8 9] def /A { x 0 get} def C } def
            B
        """

def interpreter(s,scope): # s is a string
    interpretSSPS(parse(tokenize(s)),scope)

#print(tokenize(s))
#print(parse(tokenize(s)))
#print(interpreter(s,'static'))
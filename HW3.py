# CptS 355 - Fall 2020 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1-a) getNumCases - 10%
# class HW3SampleTests(unittest.TestCase):   
def getNumCases(data,counties,months):
    sum = 0 # initializing counter 
    for county in counties:
        if data.get(county,0) != 0:
            for month in months:
                if data.get(county).get(month,0) != 0:
                    sum +=  data.get(county).get(month) 
                    #On the else condition, it will continue to the previous loop,... #
                    #...rejecting the remaining statments
    return sum 
## problem 1-b) getMonthlyCases - 15%
from functools import reduce
def getMonthlyCases(data):
    newdict = {}
    for county,logs in data.items():
        for month,sale in logs.items(): 
            if month not in newdict:
                temp = {}
            else:
                temp = newdict[month] 
            temp[county] = sale
            newdict[month] = temp       
    return newdict

## problem 1-c) mostCases - 15%
def mostCases(data):
    most = max(list(map(helperfunc, getMonthlyCases(data).keys(), getMonthlyCases(data).items())), key = lambda x:x[1])
    return (most)

def helperfunc(x, di):
    total = sum(di[1].values())
    return (x,total)

## problem 2a) searchDicts(L,k) - 5%
def searchDicts(L, k):
    for iter in range(len(L)- 1, -2, -1):
        if k in L[iter]:
            return L[iter][k]
    return None

## problem 2b) searchDicts2(L,k) - 10%
def searchDicts2(L,k):
        res = helper(len(L)-1,L,k)
        return res

def helper(ind, L, k):
    if(L[ind][1].get(k,0) == 0 and L[ind][0] == ind):
        return None
    elif (L[ind][1].get(k,0) == 0):
        res = helper(L[ind][0],L,k)
        return res
    else:
        return L[ind][1].get(k)

## problem 3 - adduptoZero - 10%
from itertools import combinations 
def adduptoZero(L, n):
    total = []
    for i in range(1,len(L)+1):
        for subset in combinations(L, n):
            if (sum(subset) == 0):
                total += [list(subset)] 
            elif (sum(subset) != 0):
                continue
            else:
                return [] 
        return list(sorted(total))

## problem 4 - getLongest - 10%
def getLongest(L):
    if type(L) == str:
        return L  
    return max([getLongest(x) for x in L])

## problem 5 - apply2nextN - 20% 
class apply2nextN():
    #Init method/constructor
    def __init__ (self, op , n, L):
        self.L = L
        self.n = n
        self.op = op
    #All objects will have different self which will contain their attributes
    #This is the object that defines how to iterate over and what will be the next value
    def __next__ (self): 
        self.counter = 0
        self.eval = 0 
        if self.L is not None:   
                for self.iter in self.L:
                    self.eval = self.op (self.eval, self.iter)
                    self.counter = self.counter + 1
                    if(self.counter != self.n):
                        continue
                    else:
                        break
        else:
            return StopIteration
        while(self.eval == 0):
            raise StopIteration
        else:
            return self.eval
    #Deals with the object that will be iterated over(so it can be used in the loop) 
    def __iter__(self):
        return self

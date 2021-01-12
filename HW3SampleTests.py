import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        self.CDCdata = { 'King':{'Mar':2706,'Apr':3620,'May':1860,'Jun':2157,'July':5014,'Aug':4327,'Sep':2843},
            'Pierce':{'Mar':460,'Apr':965,'May':522,'Jun':647,'July':2470,'Aug':1776,'Sep':1266}, 
            'Snohomish':{'Mar':1301,'Apr':1145,'May':532,'Jun':568,'July':1540,'Aug':1134,'Sep':811}, 
            'Spokane':{'Mar':147,'Apr':222,'May':233,'Jun':794,'July':2412,'Aug':1530,'Sep':1751}, 
            'Whitman' : {'Apr':7,'May':5,'Jun':19,'July':51,'Aug':514,'Sep':732, 'Oct':278} }

    def test_getNumCases(self):
        self.assertEqual(getNumCases(self.CDCdata,['Whitman'],['Apr','May','Jun']),31)
        self.assertEqual(getNumCases(self.CDCdata,['King','Pierce'],['July','Aug']),13587)
        self.assertEqual(getNumCases(self.CDCdata,['Whitman'],['Aug']),514)
        self.assertEqual(getNumCases(self.CDCdata,['Spokane'],['Aug']),1530)

    def test_getMonthlyCases(self):
        monthlyCases = {'Mar': {'King': 2706, 'Pierce': 460, 'Snohomish': 1301, 'Spokane': 147}, 'Apr': {'King': 3620, 'Pierce': 965, 'Snohomish': 1145, 'Spokane': 222, 'Whitman': 7}, 'May': {'King': 1860, 'Pierce': 522, 'Snohomish': 532, 'Spokane': 233, 'Whitman': 5}, 'Jun': {'King': 2157, 'Pierce': 647, 'Snohomish': 568, 'Spokane': 794, 'Whitman': 19}, 'July': {'King': 5014, 'Pierce': 2470, 'Snohomish': 1540, 'Spokane': 2412, 'Whitman': 51}, 'Aug': {'King': 4327, 'Pierce': 1776, 'Snohomish': 1134, 'Spokane': 1530, 'Whitman': 514}, 'Sep': {'King': 2843, 'Pierce': 1266, 'Snohomish': 811, 'Spokane': 1751, 'Whitman': 732}, 'Oct': {'Whitman': 278}}
        self.assertDictEqual(getMonthlyCases(self.CDCdata),monthlyCases)

    def test_mostCases(self):
        self.assertEqual(mostCases(self.CDCdata),('July', 11487))
        self.assertEqual(mostCases(self.CDCdata),('July', 11487))
        self.assertEqual(mostCases(self.CDCdata),('July', 11487))

    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"t"),None)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"q"),None)
        self.assertEqual(searchDicts(dictList,"e"),None)

    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),True)
        self.assertEqual(searchDicts2(dictList2,"t"),None)
        self.assertEqual(searchDicts2(dictList2,"p"),None)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"a"),None)

    
    def test_adduptoZero(self):
        numbers1 = [1,-2,3,-4,-5,6,-7,8,9,-10]
        numbers2 = list(range (-3,3))
        numbers3 = list(range (1,10))
        numbers4 = [25,-23,13,-2,6,80]
        numbers5 = [1,3,7,-4,-3,-2]
        self.assertEqual(adduptoZero(numbers1,3),[[-4, -5, 9], [-2, -7, 9], [-2, -4, 6], [1, 3, -4], [1, 6, -7], [1, 9, -10]])
        self.assertEqual(adduptoZero(numbers2,4),[[-3, 0, 1, 2], [-2, -1, 1, 2]])
        self.assertEqual(adduptoZero(numbers3,2),[])
        self.assertEqual(adduptoZero(numbers2,4),[[-3, 0, 1, 2], [-2, -1, 1, 2]])
        self.assertEqual(adduptoZero(numbers4,3),[[25, -23, -2]])
        self.assertEqual(adduptoZero(numbers5,3),[[1, 3, -4],[7, -4, -3]])
        

    def test_getLongest(self):
        strings = ['1',['22',['333',['4444','55555',['666666']],'7777777'],'4444'],'22']
        pets=[['cat',['dog','horse'],['bird',['bunny','fish']]]]
        names = ['Ayush','Kapoor','Chan','Sharmal','Morenz']
        food = [['Tomato'],['Corn','Pork','Plum','Apple']]
        self.assertEqual(getLongest (strings), '7777777')
        self.assertEqual(getLongest (pets), 'horse')
        self.assertEqual(getLongest (names), 'Sharmal')
        self.assertEqual(getLongest (food), 'Tomato')

    # Helper function for test_apply2nextN.
    # Creates an infinite iterator representing the sequence of even numbers starting at "init"
    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    # Helper function for test_apply2nextN. 
    # This function assumes that the first value in L is less than or equal to N.
    def getnextN(self,L,n):
        tempL = []
        for item in L:
            tempL.append(item)
            n-=1
            if n==0: break
        return tempL

    def test_apply2nextN(self): #test_
    	#test 1
        iSequence = apply2nextN(lambda a,b:a+b, 3, iter(range(1,32)))
        self.assertEqual(iSequence.__next__(),6)
        self.assertEqual(iSequence.__next__(),15)
        self.assertEqual(iSequence.__next__(),24)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,[33, 42, 51, 60, 69, 78, 87, 31])

    	#test 2
        strIter =iter('aaaabbbbccccddddeeeeffffgggghhhhjjjjkkkkllllmmmm')
        iSequence = apply2nextN(lambda a,b:a+b, 4, strIter)
        self.assertEqual(iSequence.__next__(),'aaaa')
        self.assertEqual(iSequence.__next__(),'bbbb')
        self.assertEqual(iSequence.__next__(),'cccc')
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['dddd','eeee','ffff','gggg','hhhh','jjjj','kkkk','llll','mmmm'])

        #test3
        evens = self.OddsEvens(2)
        iSequence = apply2nextN(lambda a,b:a+b, 2, evens)

        self.assertEqual(iSequence.__next__(),6)
        upto100 = self.getnextN(iSequence,10)
        self.assertEqual(upto100,[14, 22, 30, 38, 46, 54, 62, 70, 78, 86])
        self.assertEqual(iSequence.__next__(),94)

if __name__ == '__main__':
    unittest.main()


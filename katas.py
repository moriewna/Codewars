# Katas resolved.

def is_prime(n):
  return n > 1 and all(n % i for i in xrange(2, n))

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    self.bark = lambda: "Woof"

def openOrSenior(data):
    return ['Senior' if x[0]>55 and x[1]>7  else 'Open' for x in data]

def disemvowel(string):
    return ''.join(["" if x.lower() in ['a','e','i','o','u'] else x for x in string])

def vampire_test(x, y):
    return all([True if a in str(x*y) and b in str(x*y)and len(str(x*y))==len(str(x)+str(y)) else False for a in str(x) for b in str(y)])

def capitals(word):
    return [word.index(l) for l in word if l.isupper()]

def in_array(array1, array2):
    return list(set([a for a in array1 for b in array2 if a in b ]))

def presses(phrase):
    c = 0
    d={1:"1",2:"ABC2",3:"DEF3",4:"GHI4",5:"JKL5",6:"MNO6",7:"PQRS7",8:"TUV8",9:"WXYZ9",0:" 0","#":"#","*":"*"}
    for let in phrase.upper() :
        for key, letters in d.iteritems():
            if let in letters : c+=int(letters.index(let))+1
    return c
#print presses("#codewars #rocks")

def stock_list(listOfArt, listOfCat):
    c = [0 for i in range(len(listOfCat))]
    for i,cat in enumerate(listOfCat):
        for book in listOfArt:
            if book[0].upper() == cat : c[i] += int(book.split()[-1])
    s = ""
    for i, j in enumerate(listOfCat):
        s += "({0} : {1}) - ".format(j,c[i])
    return s[:-3]

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
#print stock_list(b,c)


def dirReduc(arr):
    return checkDir(checkDir(checkDir(arr)))

def checkDir(arr):
    par = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    if len(arr) < 2 :return arr
    else :
        if arr[1] == par[arr[0]] : return checkDir(arr[2:])
        else: return [arr[0]] + checkDir(arr[1:])


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
u = ["NORTH", "WEST", "SOUTH", "EAST"]
#print dirReduc(a)

def createDict(keys, values):
    d = {}
    for i,k in enumerate(keys):
        if i < len(values):
            d[k] = values[i]
        else :
            d[k] = None
    return d


keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]

#print createDict(keys,values)
# return dict([(keys[x], values[x]) if x < len(values) else (keys[x], None) for x in range(len(keys))])

def duplicate_encode(word):
    return "".join(["("if word.lower().count(x) == 1 else ")" for x in word.lower()])

def count_squares(n):
    if n == 1 : return 1
    else : return n*n + count_squares(n-1)

#print count_squares(3)

def isValidWalk(walk):
    return all([walk.count('n')%4 == 0 , walk.count('s')%4 == 0, walk.count('e')%4 == 0, walk.count('w')%4 == 0, walk.count('w') == 10])

# print isValidWalk(['n', 's', 'e', 'w', 'e', 's', 's', 's', 's', 'e', 'w', 'w', 'w', 's', 'e'])


def addsup2(a1, a2, a3):
    return [[v1,v2,v3] for v1 in a1 for v2 in a2 for v3 in a3 if v1+v2==v3]

#print (addsup2([1,2,5],[3,1],[5,4,6]))


def f(n, m):
    return sum([i%int(m) for i in range(1,int(n)+1)])

#print f(5, 88)

def midpoint_sum(ints):
    if len(ints) <= 2 : return None
    for i in range(1,len(ints)-1):
        if sum(ints[0:i]) == sum(ints[i+1:]) : return i
    return None

#print midpoint_sum([4,1,7,9,3,9])

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

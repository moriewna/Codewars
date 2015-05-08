# rank of values
def ranks(a):
    return [sorted(a,reverse = True).index(num)+1 for num in a ]

#print ranks([9,9,3,10])
#print ranks([9,3,6,10])

#VALIDATE SUDOKU NxN
class Sudoku(object):
    def __init__(self, arr):
        self.arr = arr
        self.size = len(self.arr)**0.5

    def is_valid(self):
        if self.size%1 != 0 : return False
        if not all([True  for lis in self.arr if len(self.arr) != len(lis)]): return False
        sets = [[] for i in range(0,self.size*3)]
        for a, lis in enumerate(self.arr):
            sets.append(self.size*2,lis)
            for i, v in enumerate(lis):
                sets[i+self.size].append(v)
                sets[(a/self.size)*self.size+i/self.size].append(v)
        return all([len(set(each))==size for each in sets])


# PING PONG SCORES
def service(score):
    s = (int(score.split(":")[0])+int(score.split(":")[1]))
    if ((s/5)%2 == 0 and s < 40) or (s > 40 and (s-40)%4 <= 1) : return "first"
    else : return "second"

#print service("0:5")
#print service("5:5")
#print service("10:5")
#print service("11:13")


# ROMAN NUMBERS ENCODER
def solution(roman):
    d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    l = [d[let] for let in roman]
    for i in range(1,len(l)):
        if l[i-1]<l[i] : l[i-1] = -l[i-1]
    return sum(l)

#print solution("MCDXLIV")


# CHINESE NUMBER DECODER
def toChineseNumeral(num) :
    print num
    numerals = {"-":"负",".":"点",0:"零",1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",100:"百",1000:"千",10000:"万"}
    s = ""
    n = int(abs(num))
    if num < 0 : s+= numerals["-"]
    if n/10000 != 0 :
        s += numerals[n/10000]+numerals[10000]
        n -= 10000*(n/10000)
    if n/1000 != 0 :
        s+= numerals[n/1000]+numerals[1000]
        n -= 1000*(n/1000)
    if n/100 != 0 :
        s+= numerals[n/100]+numerals[100]
        n -= 100*(n/100)
    if n == 0 : return s
    if n > 19 and n/10 != 0:
        s+= numerals[n/10]+numerals[10]
        n -= 10*(n/10)
    if n == 10 : return s+numerals[10]
    if n <= 19 and n > 10:
        s+= numerals[10]+numerals[n-10]
        n -= n%10
    if n == 0 : return s
    s += numerals[int(n)]
    return s


#print toChineseNumeral(-12312)

# Letter frequency

def letter_frequency(text):
    t = []
    s = []
    for letter in text.lower():
        if letter.isalpha() and letter.lower() not in t :
            t.append(letter.lower())
            s.append(1)
        elif letter.isalpha() and letter.lower() in t :
            s[t.index(letter.lower())] += 1
    return sorted(sorted(zip(t,s),key=lambda A: A[0]),key=lambda l: l[1], reverse = True)

#print letter_frequency('wklv lv d vhfuhw phvvdjh')

def snail(array):
    if len(array) == 1 : return array[0]
    else :
        l = [[] for i in range(0,len(array)-1)]
        d = [v for a, lis in enumerate(array) for i,v in enumerate(lis)  if a == 0 or i == len(lis)-1]
        for a, lis in enumerate(array):
            for i, v in enumerate(lis):
                if a != 0 and i !=len(lis)-1:
                    l[abs(a-len(array))-1].insert(0,v)
    return d + snail(l)




a1 = [[1,2,3,5],
    [4,5,6,1],
    [7,0,9,0],
    [3,4,7,1]]

a2 = [[1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11]]

#print snail(a1)
#print snail(a2)




class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      print self.collection
      self.items = items_per_page
      if len(self.collection) % self.items == 0 : self.pages = len(self.collection) / self.items
      else : self.pages = (len(self.collection) / self.items) +1

  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)

  # returns the number of pages
  def page_count(self):
      return self.pages

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      if page_index >= self.pages : return -1
      elif page_index < (self.pages-1) : return self.items
      else : return len(self.collection) % self.items

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index > (len(self.collection)-1) or item_index < 0 : return -1
      else : return item_index/self.items

#helper = PaginationHelper(['a','b','c','d','e','f'], 4)
#helper.page_count # should == 2
#helper.item_count # should == 6
#helper.page_item_count(0)  # should == 4
#helper.page_item_count(1) # last page - should == 2
#helper.page_item_count(2) # should == -1 since the page is invalid

def rgb(*args):

    return  "".join([hex(i)[2:].upper() if i <= 255 and i > 15 else "0"+hex(i)[2:].upper() if i > 0 and i <16 else "FF" if i > 255 else "00" for i in args ])


#print rgb(0,0,0)
#print rgb(255,255,255)
 #print rgb(8,5,10)

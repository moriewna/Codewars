def sum_pairs(ints, s):
    if len(ints) == 1 : return None
    else :
        for i in range(1,len(ints)):
            if ints[0]+ints[i] == s : return [ints[0],ints[i]]
        return sum_pairs(ints[1:], s)

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

#print sum_pairs(l1, 8)
#print sum_pairs(l2, -6)
#print sum_pairs(l3, -7)
#print sum_pairs(l4, 2)
#print sum_pairs(l5, 10)

def sum_pairs2(ints, s):
    for a in range(len(ints)):
      for b in range(0,a):
          if ints[b]+ints[a] == s : return [ints[b],ints[a]]

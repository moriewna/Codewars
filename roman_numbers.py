# ROMAN NUMBER ENCODER
def solution(n):
    d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    dr = {v: k for k, v in d.items()}
    l = []
    for i in [1000,100,10,1]:
        print n/i
        if n/i < 4:
            l.extend([dr[i] for b in range(0,n/i)])
        elif n/i == 4:
            l.extend([dr[i],dr[i*5]])
        elif n/i == 9:
            l.extend([dr[i],dr[i*10]])
        else :
            l.extend([dr[i*5]])
            l.extend([dr[i] for b in range(0,n/i-5)])
        n -= n/i*i
    return "".join(l)

#print solution(1999)

# ROMAN NUMBERS DECODER
def solution(roman):
    d = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    l = [d[let] for let in roman]
    for i in range(1,len(l)):
        if l[i-1]<l[i] : l[i-1] = -l[i-1]
    return sum(l)

#print solution("MCDXLIV")

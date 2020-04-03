# target: find numerator and denominator
# uniqueness: 
'''
numirator: 6 digit
denominator: 2 digit
10th place of denominator is : 1
denominator completely devides the numerator
denominator also completely devides the firt last four digits of numerator
least significant digit of numirator is 4
second least significant seems 1, but not sure
second most significant digit is 7


numerator: x 7 x x x 4 (num)
corr var:  a 7 b c d 4 (dnum)
a > 0
denominator: x x
corr var:    f e
e > 0

'''
num = ""
fnum="" #four digit number
dnom = "" # denominator

rlist = {} # required list

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(1,10):
                        num = num+str(a)+str(7)+ str(b)+str(c)+str(d)+str(4)
                        fnum = fnum +str(a)+str(7)+ str(b)+str(c)
                        dnom = dnom+str(1)+str(e)
                        
                        dnom = int(dnom)
                        num = int(num)
                        fnum = int(fnum)
                        #print(dnom,num)
                        #if(num % dnom==0 and fnum % dnom==0):
                        if((num % dnom==0) and fnum%dnom == 0):
                            rlist[dnom]= num
                        num=""
                        fnum=""
                        dnom=""


print(rlist)

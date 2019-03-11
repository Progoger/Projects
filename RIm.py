def translator(romnum):
    counter =[0,0,0,0,0,0,0,0]
    cur=0
    l = len(romnum)-1
    while (l>0):
        if (romnum[l]=='I'):
            if (cur>1):
                return -1
            counter[1]+=1
            if (counter[1]>3):
                return -1
            counter[0]+=1
            cur = 1
        elif (romnum[l]=='V'):
            if (counter[2] > 0):
                return -1
            if(romnum[l-1]=='I'):
                if cur>=4:
                    return -1
                if (counter[1]>0):
                    return -1
                else:
                    counter[2]=1
                    counter[1]=3
                    counter[0]+=4
                    cur = 4
                    l -= 1
            else:
                if cur>=5:
                    return -1
                counter[2]=1
                counter[0]+=5
                cur = 5
        elif (romnum[l]=='X'):
            if (counter[3] > 2):
                return -1
            if(romnum[l-1]=='I'):
                if cur>=9:
                    return -1
                if (counter[1]>0):
                    return -1
                else:
                    counter[3]+=1
                    counter[1]=3
                    counter[0]+=9
                    cur = 9
                    l -= 1
            else:
                if cur>10:
                    return -1
                counter[3]+=1
                counter[0]+=10
                cur = 10
        elif (romnum[l]=='L'):
            if (counter[4] > 0):
                return -1
            if(romnum[l-1]=='X'):
                if cur>=40:
                    return -1
                if (counter[3]>0):
                    return -1
                else:
                    counter[4]=1
                    counter[3]=3
                    counter[0]+=40
                    cur = 40
                    l-=1
            else:
                if cur>=50:
                    return -1
                counter[4]=1
                counter[0]+=50
                cur = 50
        elif (romnum[l]=='C'):
            if (counter[5] > 2):
                return -1
            if(romnum[l-1]=='X'):
                if cur>=90:
                    return -1
                if (counter[3]>0):
                    return -1
                else:
                    counter[5]+=1
                    counter[3]=3
                    counter[0]+=90
                    cur = 90
                    l-=1
            else:
                if cur>100:
                    return -1
                counter[5]+=1
                counter[0]+=100
                cur = 100
        elif (romnum[l]=='D'):
            if (counter[6] > 0):
                return -1
            if(romnum[l-1]=='C'):
                if cur>=400:
                    return -1
                if (counter[5]>0):
                    return -1
                else:
                    counter[6]=1
                    counter[5]=3
                    counter[0]+=400
                    cur = 400
                    l-=1
            else:
                if cur>=500:
                    return -1
                counter[6]=1
                counter[0]+=500
                cur = 500
        elif (romnum[l]=='M'):
            if (counter[7] > 2):
                return -1
            if(romnum[l-1]=='C'):
                if cur>=900:
                    return -1
                if (counter[5]>0):
                    return -1
                else:
                    counter[7]+=1
                    counter[5]=3
                    counter[0]+=900
                    cur = 900
                    l-=1
            else:
                counter[7]+=1
                counter[0]+=1000
                cur = 1000
        l-=1
    if len(romnum)!=0 and (cur!=4 or cur!=9 or cur!=40 or cur!=90 or cur!=400 or cur!=900):
        if romnum[0]=="I":
            if cur>1 or counter[1]>2:
                return -1
            else:
                return counter[0]+1
        elif romnum[0]=="V":
            if cur>=5 or counter[2]>0:
                return -1
            else:
                return counter[0]+5
        elif romnum[0]=="X":
            if cur>10 or counter[3]>2:
                return -1
            else:
                return counter[0]+10
        elif romnum[0]=="L":
            if cur>=50 or counter[4]>0:
                return -1
            else:
                return counter[0]+50
        elif romnum[0]=="C":
            if cur>100 or counter[5]>2:
                return -1
            else:
                return counter[0]+100
        elif romnum[0]=="D":
            if cur>=500 or counter[6]>0:
                return -1
            else:
                return counter[0]+500
        elif romnum[0]=="M":
                return counter[0]+1000
    else:
        return counter[0]
















    return counter

def action(number1, sign, number2):
    if (sign=='+'):
        result = number1+number2
    elif (sign=='-'):
        result = number1-number2
    elif (sign=='*'):
        result = number1*number2
    elif (sign=='/'):
        result= number1/number2
    return result

def retranslator(number):
    romnum=""
    while (number>0):
        if (number//1000>=1):
            number-=1000
            romnum+='M'
        elif (number//900>=1):
            number-=900
            romnum+='CM'
        elif(number//500>=1):
            number-=500
            romnum+='D'
        elif(number//400>=1):
            number-=400
            romnum+='CD'
        elif(number//100>=1):
            number-=100
            romnum+='C'
        elif(number//90>=1):
            number-=90
            romnum+='XC'
        elif(number//50>=1):
            number-=50
            romnum+='L'
        elif(number//40>=1):
            number-=40
            romnum+='XL'
        elif(number//10>=1):
            number-=10
            romnum+='X'
        elif(number//9>=1):
            number-=9
            romnum+='IX'
        elif(number//5>=1):
            number-=5
            romnum+='V'
        elif(number//4>=1):
            number-=4
            romnum+='IV'
        else:
            number-=1
            romnum+='I'
    return romnum







path = 'input.txt'
f = open(path, 'r')
s = f.readline()
a, b, c=s.split(' ')
f.close()
vocabulary = {'M': 1000, 'D': 500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
number1 = translator(a)
number2 = translator(c)
f1 = open('output.txt', 'w')
print(str(number1)+" "+ str(number2))
if number1==-1 or number2==-2:
    f1.write("Неправильно введены данные")
else:
    result = action(number1, b, number2)
    romNumber = retranslator(result)
    f1.write(romNumber)
f1.close()


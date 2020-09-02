import random
def getnum():
    x=[]
    y=[]
    for i in range(1,34):
        x.append(i)
    for i in range(1,17):
        y.append(i)
    red=random.sample(x,6)
    blue=random.choice(y)
    return red,blue

def check(award,a1,a2,a3,a4,a5,a6):
    red,blue=getnum()
    red1,blue1=getnum()
    ins=list(set(red).intersection(set(red1)))
    bins=False
    if blue==blue1:
        bins=True
    done=False
    if len(ins)==6 and bins==True:
        a1+=1
        award+=10000000

    if len(ins)==6 and bins==False:
        a2+=1
        award+=5000000

    if len(ins)==5 and bins==True:
        a3+=1
        award+=3000

    if (len(ins)==5 and bins==False)or(len(ins)==4 and bins==True):
        a4+=1
        award+=200

    if (len(ins)==3 and bins==True)or(len(ins)==4 and bins==False):
        a5+=1
        award+=10
    if len(ins)<3 and bins==True:
        a6+=1
        award+=5
    return award,a1,a2,a3,a4,a5,a6

def main():
    award=0
    a1=0
    a2=0
    a3=0
    a4=0
    a5=0
    a6=0
    done=False
    while not done:
        try:
            t=int(input('how much to buy?\n'))
            done=True
        except ValueError:
            1
    for i in range(0,t):
        award,a1,a2,a3,a4,a5,a6=check(award,a1,a2,a3,a4,a5,a6)  
    print('TotalAward',award,'1d',a1,'2d',a2,'3d',a3,'4d',a4,'5d',a5,'6d',a6)
    print('TotalInvestment:{},BackRate:{:.2f},TotalIncome:{}'.format(2*t,award/(2*t),award-2*t))

if __name__=='__main__':
    main()
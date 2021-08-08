#assume each folder has X number of things
import random



#We will be limited by one of the layers likely
#Need a decay function to generate but ensure distribution of accessories
#Could implement a naming and description thing here for later use
#If we had more time could give people the chance to name the monkey if they own it

#really we need to generate a list of unique values all


#ID
#CoinNum
#HeadNum
#AccessoryNum
coinCeil = 530
headCeil = 530
faceEarsCeil = 530
eyesMouthCeil = 530



accessoryCeil = 20


monkies = []
def monkeyGen(id):
    newMonkey = (id+1, 
                random.randint(0,coinCeil), 
                random.randint(0,headCeil), 
                random.randint(0,faceEarsCeil),
                random.randint(0,eyesMouthCeil))
                #[10 if x == 0 else 1 for x in range(accessoryCeil)])[0])
    
    if newMonkey not in monkies:
        monkies.append(newMonkey)

for i in range(5,10):
    monkeyGen(i)
for x in monkies:
    print(x)
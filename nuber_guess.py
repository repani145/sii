import random
low=int(input("enter starting number :"))
up=int(input("enter end number :"))
a=random.randint(low,up)

count=7
remain_options=7
while count:
    guess = int(input("enter your guessing number :"))
    if a==guess:
        break
    elif a<guess:
        print("gessing BIG")
        count -= 1
        #print("### NOT MATCHED TRY AGAIN ###")
        print("You Have %d ChanceS" % (count))
    elif a>guess:
        print("guessing smaller")
        count -= 1
        #print("### NOT MATCHED TRY AGAIN ###")
        print("You Have %d ChanceS" % (count))
    else:
        count-=1
        print("### NOT MATCHED TRY AGAIN ###")
        print("You Have %d ChanceS"%(count))
if count==0:
    print("The number is =",a)
    print("     GAME ENDED     ")
    print(" ...BETTERLUCK NEXTTIME...")
else:
    print("YOU WON THIS MATCH")
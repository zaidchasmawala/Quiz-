print("Welcome to Stock market quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("The indian stock market is regulated by?")
if answer.lower() == "sebi" or "securities and exchange board of india":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Stock market is a place where? ")
if answer.lower() == "stock buyer and seller meet":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("stock trading involves? ")
if answer.lower() == "capital risk":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The largest stock market in india is?")
if answer.lower() == "National stock exchange" or "NSE":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer =input("The oldest stock market in india is?")
if answer.lower()=="bombay stock exchage" or "BSE":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("Share holder are the_____?")
if answer.lower()=="owner of the company":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("Share of profit,if distributed by management in cash is call as?")
if answer.lower()=="dividend":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("The Share Price is decided by?")
if answer.lower=="buyer and seller" or "demand and supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("What is meant by bullish market?")
if answer.lower()=="an upward movement":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer=input("Which all factor effect the market?")
if answer.lower()=="domestic and global":
    print("Correct!")
    score += 1
else:
    print("Incorrecr!")
    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%.")

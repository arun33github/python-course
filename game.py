print("Welcome to puzzle game!!")
print("your puzzle is :")
print("who is the captain of our Indian cricket")
i=0
while i<3:
    ans=input("Enter your Ans:")
    if ans.lower()=="rohit sharma":
        print("you won the game!!")
        exit()
    i+=1
    if i==1:
        print("clue 1:His jersey Number is 45 :")
        

    elif i==2:
        print("He won the five trophies in ipl ")
    

print("you lose the game....")


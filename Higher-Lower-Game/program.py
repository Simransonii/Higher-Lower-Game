import art
import data
import random


print(art.logo)
celebrity_data=data.celebrities

#randomly choosing value for choice A and Choice B 
first_choice= random.choice(celebrity_data)
second_choice=random.choice(celebrity_data)

guess=True
you_win=0
#loop will run unless we lose
while(guess):
    
    
    
    #checking if Choice A is equal to Choice B
    if first_choice==second_choice:
        ran=random.choice(celebrity_data)
        first_choice=ran
        
    
    print("Compare A : %s, %s, from %s "%(first_choice["name"],first_choice["description"],first_choice["country"]))
    print(art.vs)
    print("Compare B : %s, %s, from %s "%(second_choice["name"],second_choice["description"],second_choice["country"]))
    
    user_value=input("Pick who has more followers (A/B) ")
    
    
    #condition to check who has more followers
    if(first_choice["follower_count"]>second_choice["follower_count"] and user_value=="a"):
        print("Win")
        you_win +=1
        if(you_win>=1):
            first_choice=second_choice
            second_choice=random.choice(celebrity_data)
        print("your score : ",you_win)
        
    elif(first_choice["follower_count"]<second_choice["follower_count"] and user_value=="b"):
        print("Win")
        you_win +=1
        if(you_win>=1):
            first_choice=second_choice
            second_choice=random.choice(celebrity_data)
        print("your score : ",you_win)
    else:
        print("You Lose")
        guess=False

print("your score : ",you_win)

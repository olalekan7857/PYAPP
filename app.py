name = input("Enter your name: ")
score = float(input("What is your score: "))

if 80 <= score <= 100:
    print("Excellent")
elif 60 <= score < 80:
    print("Very good")    
elif 40 <= score < 60:
    print("Good")    
elif score < 40:
    print("Fair")   
else:
    print("Score cant be above 100")     
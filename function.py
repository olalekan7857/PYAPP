myFile = open("text.txt", mode="w")
def scores(name,score):
    if 80 <= score <= 100:
        print("Excellent")
        myFile.writelines(f"{name} {score} Excellent")
    elif 60 <= score < 80:
        print("Very good")  
        myFile.writelines(f"{name} {score} Very good")  
    elif 40 <= score < 60:
        print("Good")
        myFile.writelines(f"{name} {score} Good") 
    elif score < 40:
        print("Fair")   
        myFile.writelines(f"{name} {score} fair")
    else:
        print("Score cant be above 100") 
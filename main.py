print('Enter your name -') #asks the user for their name
username = input()#makes the name the user puts into a variable
print("Hello, " + username) 

#This is where the questions and answers are stored.
questions = ["what main classes are in A block?", " what main classes are in B block?", " what main classes are in C block", " what main classes are in D block", " what main classes are in E block", "What is the main subject studied in F-block?", "what main classes are in G block?", "what main classes are in H block?", "what main classes are in K block?", "what main classes are in M block?", ] #questions variable
answers = ["Art", "Tech", "Math", "Social Studies", "Tech", "Science", "English", "Food", "Languages", "Music"] #answers variable 
points = 0
def start():
  print("Welcome to my quiz on what subjects are in each block at RHS.") #prints the introduction to the quiz

start()

def function():#makes the function for correct
  print("Correct!")

def point(): #makes the point function and stores the points
    #
    return 1 
    
#Code for going through the the questions and seeing if the answer from the user is correct, or incorrect

for i in range(len(questions)):
    print("Question", i+1, "-", questions[i]) #prints the next question
    user_answer = input("Answer - ") #tells the user to answer the question
    if user_answer.lower() == answers[i].lower(): #my if statement
       function() #activates the function that shows the user they got it correct by telling them in the console.
       points = points + point() # sends 1 point to the point function
    else:
        print("Incorrect, the correct answer is", answers[i])    #doesn't add 1 to the points because you got it incorrect, and also shows the correct answer to the user.

print("Your total points are:", points, "/", len(questions))    #calculates the amount of questions you got correct and how many you got incorrect.

def end():
  print("Thanks for playing", username,"!") #prints the ending message and the username and a !
  
end()  #overcomplication of printing the ending
quit()
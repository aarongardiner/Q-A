#This is where the questions and answers are stored.
questions = ["what main classes are in A block?", " what main classes are in B block?", " what main classes are in C block", " what main classes are in D block", " what main classes are in E block", "What is the main subject studied in F-block?", "what main classes are in G block?", "what main classes are in H block?", "what main classes are in K block?", "what main classes are in M block?", ] #questions variable
answers = ["Art", "Tech", "Math", "Social Studies", "Tech", "Science", "English", "Food", "Languages", "Music"] #answers variable 


def function():
#Code for the questions
  point = 0   

  print("Welcome to my quiz on what subjects are in each block at RHS")

  for i in range(len(questions)):
      print("Question", i+1, "-", questions[i]) #prints the next question
      user_answer = input("Answer - ") #tells the user to answer 
      if user_answer.lower() == answers[i].lower(): 
          print("Correct!") #shows the user they got it correct and adds 1 point
          point = point + 1   
      else:
          print("Incorrect, the correct answer is", answers[i])    #doesn't add 1 to the points because you got it incorrect, and also shows the correct answer to the user.

  print("Your total points are:", point, "/", len(questions))    #calculates the amount of questions you got correct and how many you got incorrect.

input (function())

import sqlite3
conn=sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

table_name = input('''What subject would you like to study today? \nThe options are Accounting, ManagerialFinance, ApplicationsDevelopment, FederalTax, and ComputerForensics.\n''')

cr.execute('''SELECT question, answer FROM '''+ table_name)

subject_Questions=cr.fetchall()

for question, correct_answer in subject_Questions:
     print(question)
     answer= input('Your answer: ').lower()
     correct_answer_lower= correct_answer.lower()

     if answer == correct_answer_lower:
        print ("\033[38;2;0;225;0m"+"Correct!\033[0m\n")
     else:
        print ("\033[38;2;225;0;0mIncorrect."+"The correct answer is "+ correct_answer + '.\033[0m\n' )

print("Quiz ended.")
print('')
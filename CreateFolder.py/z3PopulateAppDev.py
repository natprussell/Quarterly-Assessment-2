import sqlite3
conn= sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

def add_question(question, answer):
    cr.execute('''
        INSERT INTO ApplicationsDevelopment(question, answer) 
        VALUES (?,?)''', (question, answer)
        )
    conn.commit()

add_question("'Hello World' is an example of what?", "String")
add_question("Python recognizes PEMDAS (true/false)?", "true")
add_question("Variable names can include spaces (true/false)?", "false")
add_question("Functions are stored in what?", "Modules")
add_question("What kind of data types are either True or False?", "Boolean")
add_question("An ordered collection of information is what??", "list")
add_question("What module would you import to generate random integers?", "random module")
add_question("An example of a loop that repeats an action a predefined number of times?", "for loop")
add_question("An example of a loop that repeats an action until the program determines it needs to stop?", "while loop")
add_question("An ordered arrangement of objects/ elements is what?", "sequence")

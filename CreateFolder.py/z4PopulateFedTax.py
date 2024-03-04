import sqlite3
conn= sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

def add_question(question, answer):
    cr.execute('''
        INSERT INTO FederalTax(question, answer) 
        VALUES (?,?)''', (question, answer)
        )
    conn.commit()

add_question("What is a payment to support the cost of government?", "Tax")
add_question("What is a person or organization that pays tax (includes individuals and corporations)?", "Taxpayer")
add_question("What is right of a government to tax a particular taxpayer?", "Jurisdiction")
add_question("What is the total amount of tax collected by the government and available for use?", "Tax revenue")
add_question("What is tax levied on 'real' property?", "Real property tax")
add_question("What is tax imposed on the retail sale of specific goods or services?", "Excise tax")
add_question("What is tax imposed on individuals who live in a state and those who do not live in the state but earn income in the state?", "Personal income tax")
add_question("These taxes provide help to workers who become unemployed through no fault of their own: ", "Unemployment taxes")
add_question("A good tax must be which of the following: \n A) Sufficient  B) Convenient  C) Efficient  D) Fair  E) All of the above ", "E")
add_question("What kind of revenue forecast assumes the tax base stays the same?", "Static forecast")
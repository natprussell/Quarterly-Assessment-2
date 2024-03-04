import sqlite3
conn= sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

def add_question(question, answer):
    cr.execute('''
        INSERT INTO ManagerialFinance(question, answer) 
        VALUES (?,?)''', (question, answer)
        )
    conn.commit()

add_question("Unincorporated businesses are owned by: \n A) Sole proprietors  B) Partnerships  C)Both","C"),
add_question("What is the primary goal for managers of publicly owned companies?", "Maximize shareholder value"),
add_question("What is intrinsic value?", "The estimate of a stock's 'true' value."),
add_question("Which financial statement shows a firm's revenues, expenses, and profits during a specific period of time?", "Income Statement"),
add_question("Which of the following is(are) considered a fixed asset on the firm's balance sheet? \n A) Inventory B) Bonds C) Retained Earnings D) Copyrights E) Notes payable F) Equipment", "D and F"),
add_question("Income not distributed to shareholders is: ", "Retained Earnings"),
add_question("Which type of ratios capture a firm's ability to manage its debt?", "Debt ratios"),
add_question("When the quick ratio increases, it generally indicates a(n) (improvement/deterioriation) in the firm's position?", "improvement"),
add_question("Interest earned on principal and on prior period's interest: ", "Compound interest"),
add_question("A stream of equal periodic cash flows over a stated period of time: ", "Annuity")

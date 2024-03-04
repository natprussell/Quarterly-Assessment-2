import sqlite3
conn= sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

def add_question(question, answer):
    cr.execute('''
        INSERT INTO Accounting(question, answer) 
        VALUES (?,?)''', (question, answer)
        )
    conn.commit()

add_question('Calculate the total assets given liabilities of $50,000 and equity of $30,000.', 80000),
add_question('If a company has revenues of $100,000 and expenses of $60,000, what is the net income?', 40000),
add_question('Determine the depreciation expense if the asset cost is $10,000 and has a useful life of 5 years.', 2000),
add_question('What is the ending balance of an account with an initial balance of $5,000, additional investments of $2,000, and withdrawals of $1,000?', 6000),
add_question('If a company has current assets of $20,000 and current liabilities of $15,000, calculate the working capital.', 5000),
add_question('Calculate the book value of an asset with a cost of $8,000 and accumulated depreciation of $3,000.', 5000),
add_question('Find the gross profit margin if a company has sales of $80,000 and cost of goods sold of $40,000.', 0.5),
add_question('If a company issues 1,000 shares of common stock at $10 per share, calculate the total common stock value.', 10000),
add_question('Compute the return on equity (ROE) if net income is $15,000 and equity is $75,000.', 0.2),
add_question('What is the acid-test ratio if a company has current assets of $30,000, inventory of $10,000, and current liabilities of $15,000?', 1.33)

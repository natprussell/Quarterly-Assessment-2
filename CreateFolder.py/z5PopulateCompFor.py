import sqlite3
conn= sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

def add_question(question, answer):
    cr.execute('''
        INSERT INTO ComputerForensics(question, answer) 
        VALUES (?,?)''', (question, answer)
        )
    conn.commit()

add_question("What is evidence that helps prove guilt?", "Inculpatory evidence")
add_question("What is evidence that helps prove innocence?", "Exculpatory evidence")
add_question("What is any particular chunk of data?", "Artifact")
add_question("What is data about data?", "Metadata")
add_question("What is a number without intrinsic meaning and is also a 'digital fingerprint' for a hard drive?", "Hash value")
add_question("What is it called when a crime has probably been commited or is about to be commited?", "Probable cause")
add_question("What is it called when a crime has maybe been commited?", "Reasonable suspicion")
add_question("What is necessary to recieve a warrant?", "Affidavit")
add_question("This gives the right for search and seizure: ", "Warrant")
add_question("What is any space that is not being used called?", "Unallocated space")
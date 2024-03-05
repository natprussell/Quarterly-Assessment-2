# Quarterly-Assessment-2

The quizBowlAppFile.py program is a quiz program used for studying different subjects. It defines a set of questions and their correct answers in a database. It will prompt the user to pick a subject to study. The subject options were Accounting, ManagerialFinance, ApplicationsDevelopment, FederalTax, and ComputerForensics. It then quizzes the user, checking their answers and providing feedback. 
    The steps include the following: Establish a connection with database, recieve user's input on prefered subject material, fetch questions and answers from specified table in database, loop through each question-answer pair with user, provide color-coded feedback with correct answers. 


This repository includes many files and folders to help build this application. 

The Create Folder:
    Within this folder there are 6 different files. The file labeled CreateFile.py was used strictly to create the tables only. 
    Each other file was used to populate the different tables with their corresponding questions. 
        z1PopulateAcct.py was used to insert all questions and answers for the subject Accounting.
        z2PopulateManFin.py was used to insert all questions and answers for the subject ManagerialFinance.
        z3PopulateAppDev.py was used to insert all questions and answers for the subject ApplicationsDevelopment.
        z4PopulateFedTax.py was used to insert all questions and answers for the subject FederalTax.
        z5PopulateCompFor.py was used to insert all questions and answers for the subject ComputerForensics.

The Read Folder:
    Within this folder there are 2 files. 
        The file labeled z1ReadFile.py was used to retrieve the questions and answers from each table of data. This file prompts
        the input of the subject/table before retreiving all data within it.
        The file labeled z2ReadFile.py was strictly used to recieved the exact names of the tables found within the created database.

The QuizBowl.db file is the database created that holds the five tables with corresponding questions and answers mentioned above. This database is the foundation to the application. 


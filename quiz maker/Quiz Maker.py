#Name: Saad Zaki
#Date: June 2, 2021
#Descrpition: A program that allows the user to play a 10 question quiz game
#             with all unique questions in a randomized order. 3 files with the
#             questions, choices, and solutions are referenced for this. The
#             second part of this program (create menu) lets the user add and
#             remove questions from the quiz. All inputs have error control.

#Importing libraries and initializing time.sleep's constant variables
import random
import input_utilities
import time
vshort = 0.5
short = 0.75
long = 1

#This function prints the main menu of the game, and 
def main_menu():
    #Visually appealing ASCII graphic used for game title.
    print('''
 ______      _    _   _____                     _____       _      ___  ___      _             
|___  /     | |  (_) /  __ \                   |  _  |     (_)     |  \/  |     | |            
   / /  __ _| | ___  | /  \/ ___  _ __ _ __    | | | |_   _ _ ____ | .  . | __ _| | _____ _ __ 
  / /  / _` | |/ | | | |    / _ \| '__| '_ \   | | | | | | | |_  / | |\/| |/ _` | |/ / _ | '__|
./ /__| (_| |   <| | | \__/| (_) | |  | |_) _  \ \/' | |_| | |/ /  | |  | | (_| |   |  __| |   
\_____/\__,_|_|\_|_|  \____/\___/|_|  | .__(_)  \_/\_\\__,_|_/___| \_|  |_/\__,_|_|\_\___|_|   
                                      | |                                                      
                                      |_|    ''')
    print("     "*7, "1. Play Menu\n")
    time.sleep(short)
    print("     "*7, "2. Create Menu\n")
    time.sleep(short)
    print("     "*7, "3. Exit Game\n")
    time.sleep(short)
    #Uses input utilities module to have the user enter 1,2, or 3 to pick an
    #option for the main menu.
    #This has the acceptable inputs in brackets beacause this is the first
    #numerical input the user sees.
    choice = input_utilities.get_option(3,"Choose an Option (1/2/3):")
    return choice

#Displays the play menu
def play():
    #Visually appealing ASCII graphic used for title.
    print('''
  _____  _               __  __                  
 |  __ \| |             |  \/  |                 
 | |__) | | __ _ _   _  | \  / | ___ _ __  _   _ 
 |  ___/| |/ _` | | | | | |\/| |/ _ | '_ \| | | |
 | |    | | (_| | |_| | | |  | |  __| | | | |_| |
 |_|    |_|\__,_|\__, | |_|  |_|\___|_| |_|\__,_|
                  __/ |                          
                 |___/                           
''')
    print("     "*7, "1. Start a CS Quiz!!\n")
    time.sleep(short)
    print("     "*7, "2. Return to Main Menu\n")
    time.sleep(short)

#Uses input utilities module to have the user enter 1 or 2 to pick an option
#for the play menu.
def play_menu():
    menu = input_utilities.get_option(2,"Choose an Option:")
    time.sleep(short)
    return menu

#Displays the Create menu.
def create():
    #Visually appealing ASCII graphic used for title.
    print('''
   _____                _         __  __                  
  / ____|              | |       |  \/  |                 
 | |     _ __ ___  __ _| |_ ___  | \  / | ___ _ __  _   _ 
 | |    | '__/ _ \/ _` | __/ _ \ | |\/| |/ _ | '_ \| | | |
 | |____| | |  __| (_| | ||  __/ | |  | |  __| | | | |_| |
  \_____|_|  \___|\__,_|\__\___| |_|  |_|\___|_| |_|\__,_|
                                                          
                                                          
''')
    print("     "*7, "1. Add Question\n")
    time.sleep(short)
    print("     "*7, "2. Delete Question\n")
    time.sleep(short)
    print("     "*7, "3. Back to Main Menu\n")
    time.sleep(short)

#Uses input utilities module to have the user enter 1 or 3 to pick an option
#for the create menu.
def create_menu():
    menu = input_utilities.get_option(3,"Pick an option:")
    return menu

#Picks 10 random questions from a set of files predetermined, and then asks the
#player. Gives relevent feedback depending on the player's answers. Finally
#reports the player's score in a percentage.
def do_quiz():
    #Initiallizing variables
    tempList = []
    questionList = []
    correct = 0
    #Gives user feedback for picking to play the CS quiz since that's the main
    #purpose of the program.
    print("Good Choice!\n")
    #Finds out how many lines in the question bank to ensure the every question
    #has the chance to be randomly picked.
    #rqp means reading question bank.
    with open("QuestionBank.txt", "r") as rqb:
        questBank = rqb.readlines()
        length = len(questBank)
    #Informs the user that there are less than 10 questions in the file and
    #returns the user back to the main menu.
    #Although the return function is used, nothing gets returned.
    if length < 10:
        print("There are less than 10 questions, please add additional questions in the CREATE menu")
        return
    #Create a list from 0 to the number of lines in the questionBank file minus 1.
    for x in range (length):
        tempList.append(x)
    #Create a 10 integer list with unique random numbers from the temporary list.
    #The numbers in this list represent the line numbers for the questions in
    #the questionBank file.
    for i in range (10):
        #Picks a random num from temp list
        add = random.choice(tempList)
        #Adds it to question list
        questionList.append(add)
        #Removes it from the reference list so that it doesn't repeat
        tempList.remove(add)
    
    #Loading quiz feature to build up anticipation for the quiz.
    print("Creating your quiz",end = "")
    for dot in range (5):
        #Adds 1 dot each time it loops.
        print(".",end = "")
        time.sleep(vshort)
    print("")
    
    with open("QuestionBank.txt", "r") as rq:
        #Loops through each one of the 10 randomly selected questions
        for i in questionList:
            time.sleep(short)
            #prints a question
            print ("\n",questBank[i])
            #Prints the 4 multiple choice questions associated with the question
            with open ("MCBank.txt", "r") as rmc:
                mChoiceBank = rmc.readlines()
                #The list element number for the 
                mcBankLine = i*4
                for x in range (4):
                    #end="" included because the list elements by default have
                    #\n at the end of them
                    print(mChoiceBank[mcBankLine],end = "")
                    mcBankLine += 1
            
            #Takes input for answer
            validAns = False
            while not validAns:
                try:
                    ans = input("\nAnswer:")
                    if ans == "A" or ans == "B" or ans == "C" or ans == "D":
                        validAns = True
                        #Adds in \n because the list file automatically adds \n.
                        ans += "\n"
                    else:
                        print("Please enter a valid input (A/B/C/D)?")
                except:
                    print("Please enter a valid input (A/B/C/D)?")
            
            #Checks if answer inputed by player is correct
            with open("AnswerBank.txt", "r") as ra:
                ansBank = ra.readlines()
                correctAns = ansBank[i]
            #Or condition ensures that even if the answer's on the last line
            #without \n it still works.
            if correctAns == ans or correctAns+"\n" == ans:
                print("\nCorrect!")
                #Adds to the correct counter up to 10 to determine
                #how many question the user answered correctly.
                correct += 1
            else:
                print("\nIncorrect, The answer was:", correctAns)
    #Calculates the percentage of questions the player got right.
    score = (correct/10)*100
    print("Your score was: ",score,"%",sep = "")
    print("You will now be sent back to the play manu.\n")
    time.sleep(long)

#Prompts player to create a question, and then ask player if they would like
#to add it into the code.
def add_question():
    print ("Add the text for the question you would like to add. Press enter when done.")
    #No error checking necessary because the question can be any string.
    question = input("")
    print("Please fill in the multiple choice form for this question.")
    #Has the player enter the various options for the multiple choice portion.
    aMC = input("(A)")
    bMC = input("(B)")
    cMC = input("(C)")
    dMC = input("(D)")
    
    #Error checking for answer input, since it must be A, B, C, or D.
    validAns = False
    while not validAns:
        try:
            newQuestAns = input("Now enter the answer (A, B, C or D):")
            if (newQuestAns == "A" or newQuestAns == "B" or newQuestAns == "C"
            or newQuestAns == "D"): 
                validAns = True
            else:
                print("Please enter a valid input")
        except:
            print("Please enter a valid input")
    
    #Displays the question the player created
    print("Below is the question you made:\n")
    print(question)
    print("(A)"+aMC)
    print("(B)"+bMC)
    print("(C)"+cMC)
    print("(D)"+dMC)
    print("Answer:"+ newQuestAns)
    
    #Error control to ensure the user either says Yes(Y) or No(N) to adding the
    #question.
    confirmAdd = False
    while not confirmAdd:
        try:
            response = input("Would you like to add this to question"\
                             +" to this quiz? (Y/N):")
            if response == "Y" or response == "N": 
                confirmAdd = True
            else:
                print("Please enter a valid input (Y/N)")        
        except:
            print("Please enter a valid input (Y/N)")
    
    #If the user said yes, the question is added into the code.
    if response == "Y":
        with open("MCBank.txt" , "a") as amcb:
            amcb.write("\n(A)"+aMC)
            amcb.write("\n(B)"+bMC)
            amcb.write("\n(C)"+cMC)
            amcb.write("\n(D)"+dMC)
        with open("QuestionBank.txt" , "a") as aqb:
            aqb.write("\n"+question)
        with open("AnswerBank.txt" , "a") as aab:
            aab.write("\n"+newQuestAns)
        print("Done!")
        print("You will now be sent back to the Create menu.")
        time.sleep(long)
    
    elif response == "N":
        #Makes a remark about the question to make the give the game
        #more fun and give it personality. 
        print("Good idea, something about that question was off.")
        print("You will now be sent back to the Create menu.")
        time.sleep(long)
    else:
        print("Done!")
        print("You will now be sent back to the Create menu.")
        time.sleep(long)
#Searches for a question based of a key phrase inputed by the user, and then
#asks if player wants to delete it.
def delete_question():
    #Initializing variables
    lineNum = 0
    found = False
    lineFound = False
    
    print("To delete a question, you will need to enter a key phrase to search for in the database.")
    #Takes input for the key phrase.
    keyword = input("Key phrase:")
    
    with open ("QuestionBank.txt" , "r") as rqb:
        #Creates list comprised of the question bank file's lines.
        contents = rqb.readlines()
        #Searches for a match of the keyword/key phrase in the question list file.
        #Tests every single element in the contents list for a match
        for line in contents:
            if keyword in line:
                #Records if a match was found
                found = True
                #Records the lineNum or in reality the element number that the
                #match was found.
                lineFound = lineNum
            #Line number counter that effectively counts the element number
            #where the match took place
            lineNum += 1 
        
        if found:
            #Prints the line that a match was found by using the contents list
            print("Match Found:", contents[lineFound])
            #Error control to ensure the player enter Y or N
            validAns = False
            while not validAns:
                try:
                    delQuest = input("Would you like to delete the question?"\
                                     +"(Y/N)")
                    if delQuest == "Y" or delQuest == "N": 
                        validAns = True
                    else:
                        print("Please enter Y or N.")
                except:
                    print("Please enter Y or N.")
            #If the user said yes the program effectively deletes the line.
            if delQuest == "Y":
                #Rather than deleting a specific question, the program rewrites
                #the file without the specific question. 
                with open ("QuestionBank.txt", "w") as wqb:
                    for line in range(len(contents)):
                        if line != lineFound:
                            wqb.write(contents[line])
                
                #Rewrites the answer bank file without the associated answer.
                with open ("AnswerBank.txt","r") as rab:
                    ansContents = rab.readlines()
                with open ("AnswerBank.txt", "w") as wab:
                    for line in range(len(contents)):
                        if line != lineFound:
                            wab.write(ansContents[line])
                
                #Rewrites the multiple choice bank without the associated options.
                with open("MCBank.txt", "r") as rmcb:
                    mChoiceBank = rmcb.readlines()
                with open("MCBank.txt", "w") as wmcb:
                    #Multiplies the line that the match for the question was
                    #found by 4 to find the element where the desired question's
                    #(A) options is at.
                    mcFoundLine = lineFound*4
                    for line in range(len(mChoiceBank)):
                        #In place to create a 4 line buffer where the question's
                        #multiple choice options aren't included.
                        #The elements that the matches took place are not written.
                        #Does not work with != because even if the line does
                        #equal mcFoundLine the other or conditions are still True.
                        if line == mcFoundLine or line == mcFoundLine+1 or line == mcFoundLine+2 or line == mcFoundLine+3:
                            pass
                        else:
                            wmcb.write(mChoiceBank[line])
                print("Done!")
                print("You will now be sent back to the Create menu")
                time.sleep(long)
            else:
                #Adds a remark to give the game personility and make it more fun.
                print("Sounds good, that was a pretty good question.")
                print("You will now be sent back to the create menu")
                time.sleep(long)
        else:
            print("Sorry, no question matching your query was found.")
            print("You will now be sent back to the Create menu")
            time.sleep(long)      

def main():
    #Initializing variables
    playAgain = True
    playPlayAgain = True
    createAgain = True
    #Continues to play again unless the user exits
    while playAgain:
        #Sets the variables below as true so that players return to the
        #play and create menus as expected.
        playPlayAgain = True
        createAgain = True
        #Shows the main menu and asks user to pick an option. That goes to
        #choice variable.
        choice = main_menu()
        #If the user wanted to go to play menu:
        if choice == 1:
            #Enters play menu loop so that player returns to play menu after
            #doing the quiz.
            while playPlayAgain:
                #Displays play menu
                play()
                #Takes input for play menu
                menu = play_menu() 
                if menu == 1:
                    do_quiz()
                elif menu == 2:
                    playPlayAgain = False
        #If the user wanted to go to create menu:
        elif choice == 2:
            #Enters create menu loop so that player returns to play menu after
            #adding or deleting questions.
            while createAgain:
                #Displays create menu
                create()
                #Takes input for create menu
                cmenu=create_menu()
                if cmenu == 1:
                    add_question()
                elif cmenu == 2:
                    delete_question()
                elif cmenu == 3:
                    createAgain = False
        #If the user wanted to exit:
        else:
            print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
''')
            #Exits play Again loop
            playAgain = False
                
                
                
main()
        
    
                
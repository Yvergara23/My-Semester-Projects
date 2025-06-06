#Yareli Vergara


#Initialize
import time
import random
magic8list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it","Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"] #15 responses


#Functions
def Game():
    print ("""



░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ████████╗██╗░░██╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ░░░██║░░░███████║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ░░░██║░░░██║░░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

███╗░░░███╗░█████╗░░██████╗░██╗░█████╗░  ░█████╗░░░░░░░██████╗░░█████╗░██╗░░░░░██╗░░░░░██╗
████╗░████║██╔══██╗██╔════╝░██║██╔══██╗  ██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░░░██║░░░░░██║
██╔████╔██║███████║██║░░██╗░██║██║░░╚═╝  ╚█████╔╝█████╗██████╦╝███████║██║░░░░░██║░░░░░██║
██║╚██╔╝██║██╔══██║██║░░╚██╗██║██║░░██╗  ██╔══██╗╚════╝██╔══██╗██╔══██║██║░░░░░██║░░░░░╚═╝
██║░╚═╝░██║██║░░██║╚██████╔╝██║╚█████╔╝  ╚█████╔╝░░░░░░██████╦╝██║░░██║███████╗███████╗██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░  ░╚════╝░░░░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝""")
    print ("""
        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........""")
    print ("- - - - - - - - - - - - - - -")
    print ("Enter a Yes/No question\n     --> To ensure your question is submitted successfully,\n         use a question mark '?' at the end of your sentence.")
    print ("\n")
    print ("Enter 'n' to quit")
    while True:
        print ("- - - - - - - - - - - - - - -")
        time.sleep(3)
        print ("Would you like to continue?")
        print ("Y or N")
        playerCont = input("Would you like to continue?")
        if playerCont.lower() == ("n"): #This is if the player answers with no, the program will stop/end
            print ("Logging Out...")
            time.sleep(2)
            break
        if playerCont.lower() == ("y"): #This is if the player wishes to continue, will then prompt for a question
            print ("What is your question?")
            Question = input("What is your question?")
            if Question.endswith ("?"): #This is to check if the question is inputted correctly
                print ("- - - - - - - - - - - - - - -")
                print ("Your Question: " + Question)
                response = (random.choice(magic8list))
                print ("- - - - - - - - - - - - - - -")
                print ("""____            _
|  _ \\ ___ _ __ | |_   _ _
| |_) / _ \\ '_ \\| | | | (_)
|  _ <  __/ |_) | | |_| |_
|_| \\_\\___| .__/|_|\\__, (_)
          |_|      |___/
                       """)
                print (response)
            else:
                print ("- - - - - - - - - - - - - - -")
                print ("End Your Question with '?' and Try Again")


Game()

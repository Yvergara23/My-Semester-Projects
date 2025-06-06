#Yareli Vergara


##Initialize
songsToListenTo = []

#Functions
def Intro():
    print ("Welcome to Songs To Listen to Tracker!")
    # print ("- - - - - - - - - - - - - - -")
    print ("Try Adding items to begin:")
    print ("Enter a number 1-7")
    print ("""
           """)
    print ("1.) View Song List\n2.) Add to List\n3.) Remove a Song\n4.) Sort List\n5.) Count and Print # of Songs\n6.) Quit\n7.) View Options List")

def ViewSongList(): #1, view an updates list of what songs you have
    print ("Choice 1 Selected: View Song List")
    print ("""
            """)
    print ("Loading List...")
    print (songsToListenTo)

def AddSong(): #2, add a song to your list
    global addSong
    print ("Choice 2 Selected: Add to List")
    print ("Note: When adding a song, it will be added to the end of list")
    print ("""
           """)
    addSong = str(input("Add a Song Title"))
    songsToListenTo.append(addSong)
    print ("Loading List...")
    print (songsToListenTo)

def RemoveSong(): #3, remove a song from your list
    global removeSong #Variable is lowercase r, function is uppercase R
    print ("Choice 3 Selected: Remove a Song")
    print ("Note: Type song as it was originally entered into the system")
    print ("""
           """)
    removeSong = str(input("Remove a Song Title"))
    songsToListenTo.remove(removeSong)
    print ("Loading List...")
    print (songsToListenTo)

def SortList(): #4, sort in alphabetical order
    print ("Selected: Sort List")
    songsToListenTo.sort()
    print (songsToListenTo)

def CountAndPrint(): #5, count and print the total number of songs you have in your list
    numberofsongs = songsToListenTo.count()
    print (numberofsongs)

def SongsToListenToTracker(): #Entire Function
    Intro()
    while True:
        print ("- - - - - - - - - - - - - - -")
        try:
            choice = int(input("What would you like to do? Enter a number 1-7. Enter 7 for full options list"))
            if choice == 1:
                ViewSongList()
            if choice == 2:
                AddSong()
            if choice == 3:
                RemoveSong()
            if choice == 4:
                SortList()
            if choice == 5: #Not done in a function
                print ("Selected: Count and Print")
                print ("Loading Total Number of Songs...")
                print ("""
                    """)
                print (len(songsToListenTo))
            if choice == 6: #Not done in a function
                print ("Selected: Quit")
                break
            if choice == 7: #Not done in a function
                print ("Choice 7 Selected: View Options List")
                print ("""
                    """)
                print ("1.) View Song List\n2.) Add to List\n3.) Remove a Song\n4.) Sort List\n5.) Count and Print # of Songs\n6.) Quit\n7.) View Options List")
        except ValueError: #If you get an error, do not crash
            print ("ERROR: Must be a number")
#Main
SongsToListenToTracker()

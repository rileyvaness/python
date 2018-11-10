# Python 2.7
#Tutorial provided by the Tech Academy,as a capstone to utilizing the skills learned in their python book.




def start(nice=0,mean=0,name= ""):
    #get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
    check if this is a new game or not,
    If it is new, get the users name.
    If it is not a new game, thank the player for
    playing again and continue with the game

    """

    if name != "":
        print ("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
               if name == "":
                   name = raw_input("\nWhat is your name? ").capitalize()
                   if name != "":
                        print ("\nWelcome, {}!".format(name))
                        print("\nIn this game you will be greeted by different people. \nYou can be nice or mean.")
                        print("At the end of the game your fate will be influenced by your actions.")
                        stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input ("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m").lower()
        if pick == "n":
            print ("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you menacingly and abruptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean, name) 

def show_score(nice,mean,name):
    print("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))

def score(nice,mean,name):
    #score function is being passed the value stored within the 3 variables
    if nice > 5:
        win(nice,mean,name)
    if mean > 5:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice Job{}.you win! \nEveryone loves you and you now live in a palace!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nToo bad, game over! \n{}, you live in a van by the river, wretched and alone!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice =="y":
                stop = False
                reset(nice,mean,name)
        if choice == "n":
            print ("\nSee you later alligator!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")

def reset (nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)

if __name__ == "__main__":
    start()

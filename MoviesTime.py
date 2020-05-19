def welcome():
    name= input("Please enter your name")
    print("Welcome to BeThere airlines," + name + ".We hope you enjoy our complementary on-flight Tv services")
    how_old()
    
def how_old():
    age = int(input("How old are you?"))
    if (age>= 18):
        print("You can watch 18+ movies. But you can watch other movies and series too")
        choices_18andabove()
    elif (age <= 12):
        print("You can watch children's movies and series.But you can't watch 12+,15+ or 18+")
        tv_for_children()
    elif(age>=12 and age<=14):
        print("You can watch 12+ movies and children's movies. But you cannot watch 15+ and 18+")
        choices_12to14()
    elif(age>=15 and age<=17):
        print("You can watch 12+, 15+ and children's movies and Tv series. But you cannot watch 18+")
        choices_15to17()
    else:
    	print("Please enter an acceptable age")
    	how_old()
    	
def choices_12to14():
    choice= input('''What TV series would you like to watch
            1.Children's Tv
            2. Tv for 12 to 14 years old
            ''')
    if choice == "1" :
        print("Here is you children's TV choices")
        tv_for_children()
    elif choice == "2":
        print("Here are you 12 to 14 years old tv choices")
        tv_for_12to14()
    else:
        print("The answer wasn't acceptable please try again")
        choices_12to14()
def choices_15to17():
    choice= input('''What TV series would you like to watch
            1.Children's Tv
            2. Tv for 12 to 14 years old
            3. Tv for 15 to 17 years old
            ''')
    if choice == "1" :
        print("Here are your children's TV choices")
        tv_for_children()
    elif choice == "2":
        print("Here are your 12 to 15 years old tv choices")
        tv_for_12to14()
    elif choice == "3":
        print ("Here are your 15 to 18 tv choices")
        tv_for_15to17()
    else:
        print("The answer wasn't acceptable please try again")
        choices_15to17()

def choices_18andabove():
    choice= input('''What TV series would you like to watch
            1.Children's Tv
            2. Tv for 12 to 14 years old
            3. Tv for 15 to 17 years old
            4.Tv for 18s and above years old
            ''')
    if choice == "1" :
        print("Here are your children's TV choices")
        tv_for_children()
    elif choice == "2":
        print("Here are your 12 to 14 years old tv choices")
        tv_for_12to14()
    elif choice == "3":
        print ("Here are your 15 to 17 tv choices")
        tv_for_15to17()
    elif choice == "4":
        print("Here are your 18s and above tv choices")
        tv_for_18andabove ()
    else:
        print("The answer wasn't acceptable please try again")
        choices_12to14()
    

def tv_for_15to17 ():
    print("Below is a list of all tv series availiable on onboard. You can add an additional series to the list and replace another")
    print("The availaible tv series are:")
    tvShows = ["Designated Survivor","Money Heist","Stranger Things","Line of Duty"]
    addItem = input("Please add your favorite TV Show to the list-you will be able to watch this too")
    tvShows.append (addItem)
    print("This is the list of tv-series you can now watch")
    print(tvShows)
    findItem = input("Please type a show name that's on the list that you would like to replace with another.")
    showsPosition = tvShows.index(findItem)
    print ("The show's position is",showsPosition+1)
    replaceItem = input("Choose something in the list to Replace: ")
    newItem = input ("With: ")
    tvShows[tvShows.index(replaceItem)] = newItem
    print("These are you final tv series choice for the flight. Thanks for flying with BeThere Airlines")
    print(tvShows)
    
def tv_for_children ():
    print("Below is a list of all tv series availiable on onboard. You can add an additional series to the list and replace another")
    print("The availaible tv series are:")
    tvShows = ["Peppa Pig","Mickey Mouse Clubhouse","Daniel Tiger","The investigators"]
    addItem = input("Please add your favorite TV Show to the list-you will be able to watch this too")
    tvShows.append (addItem)
    print("This is the list of tv-series you can now watch")
    print(tvShows)
    findItem = input("Please type a show name that's on the list that you would like to replace with another.")
    showsPosition = tvShows.index(findItem)
    print ("The show's position is",showsPosition+1)
    replaceItem = input("Choose something in the list to Replace: ")
    newItem = input ("With: ")
    tvShows[tvShows.index(replaceItem)] = newItem
    print("These are you final tv series choice for the flight. Thanks for flying with BeThere Airlines")
    print(tvShows)
    
def tv_for_12to14 ():
    print("Below is a list of all tv series availiable on onboard. You can add an additional series to the list and replace another")
    print("The availaible tv series are:")
    tvShows = ["The Big Bang Theory","Friends","How I met your mother","The IT Crowd"]
    addItem = input("Please add your favorite TV Show to the list-you will be able to watch this too")
    tvShows.append (addItem)
    print("This is the list of tv-series you can now watch")
    print(tvShows)
    findItem = input("Please type a show name that's on the list that you would like to replace with another.")
    showsPosition = tvShows.index(findItem)
    print ("The show's position is",showsPosition+1)
    replaceItem = input("Choose something in the list to Replace: ")
    newItem = input ("With: ")
    tvShows[tvShows.index(replaceItem)] = newItem
    print("These are you final tv series choice for the flight. Thanks for flying with BeThere Airlines")
    print(tvShows)
    
def tv_for_18andabove ():
    print("Below is a list of all tv series availiable on onboard. You can add an additional series to the list and replace another")
    print("The availaible tv series are:")
    tvShows = ["Fifty Shades of Grey","Sex Education","Breaking Bad","Orange is the New Black"]
    print(tvShows)
    addItem = input("Please add your favorite TV Show to the list-you will be able to watch this too")
    tvShows.append (addItem)
    print("This is the list of tv-series you can now watch")
    print(tvShows)
    findItem = input("Please type a show name that's on the list that you would like to replace with another.")
    showsPosition = tvShows.index(findItem)
    print ("The show's position is",showsPosition+1)
    replaceItem = input("Choose a series  in the list to Replace: ")
    newItem = input ("What would you like to: ")
    tvShows[tvShows.index(replaceItem)] = newItem
    print("These are you final tv series choice for the flight. Thanks for flying with BeThere Airlines")
    print(tvShows)
    
welcome()

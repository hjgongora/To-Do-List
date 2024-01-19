#Zoe Frankel & Heidi Gongora
#01/10/24
#To Do List

#Initialize
movieList = []
print("Welcome to Movie List!")
print("Menu:")


#Functions
#adds a specific movie to list
def addMovie():
    movie = input("Insert Name of Movie ")
    movieList.append(movie)
    print(movie + " has been added! \n")

#allows the user to view their movie list
def viewList():
    print("Movie List:")
    print(movieList)
    print("")

#marks watched movies as watched
def watched():
    viewList()
    movieWatched = (input("Which movie do you want to mark as watched? "))
    i = movieList.index(movieWatched)
    movieList[i] = movieWatched + " (Watched!)"
    print(movieWatched + " has been marked as watched!\n ")

#Removes specific movies
def remove():
    viewList()
    removeMovie = input("What movie would you like to remove? ")
    i = movieList.index(removeMovie)
    movieList.pop(i)
    print(removeMovie + " has been removed from list!\n ")

#Changes a movie to another movie
def editMovie():
    viewList()
    editMovie = input("What movie would you like to edit? ")
    editedMovie = input("What would you like to change it to? ")
    i = movieList.index(editMovie)
    movieList[i] = editedMovie
    print(editMovie + " has been changed to " + editedMovie + "!\n ")

#Deletes movie list
def removeList():
    i = movieList.clear()
    print(i)

#Orders the list alphabetically
def Alphabetically():
    movieList.sort()
    print(movieList)

#Prints out the number of movies in the list
def numberOfMovies():
    i = movieList.__len__()
    if i >= 2:
        print("There is " + str(i) + " movies in your list!")
    elif i == 1:
        print("There is " + str(i) + " movie in your list!")
    else:
        print("You have no movies in your list!")



#Main
while True:
    print("(1) Add Movie \n(2) View Movie List\n(3) Mark Movie as Watched \n(4) Remove Movie from Watched List \n(5) Edit a Movie \n(6) Remove All Movies  \n(7) Sort List Alphabetically  \n(8) Number of Movies in List  \n(9) Quit \n ")
    #Input Menu
    menu = int(input("What do you want to do? "))
    if menu == 1:
        addMovie()
    elif menu == 2:
        viewList()
    elif menu == 3:
        watched()
    elif menu == 4:
        remove()
    elif menu ==5:
        editMovie()
    elif menu == 6:
        removeList()
    elif menu == 7:
        Alphabetically()
    elif menu == 8:
        numberOfMovies()
    elif menu == 9:
        print("Bye Bye!")
        break
    else:
        print("Uh Oh! Invalid Number Added! Please Try Again!")

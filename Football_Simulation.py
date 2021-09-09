# Mauricio Fortune
# COP2930
# Football Simulation
# 11/29/2020


import random
#--------------------Offensive Menu-------------------------------------
#offensive menu that shows up every offensive play
def offenseMenu():
    print("1. Throw the ball.")
    print("2. Run the ball.")
    print("3. Kick the ball.")
    print("4. Quit")
    ans = int(input(""))
    return ans
#---------------------Throw Options----------------------------
#Throw options that shows up if they select a throw play
def throwOptions():
    print("Which of the following pass (throw) plays do you want")
    print("1. Short throw (1-5 yards)")
    print("2. mid range throw (6-10 yards)")
    print("3. long range throw (10-20 yards)")
    print("4. Hail Mary(30 yards)")
    throwPlay = int(input(""))
    return throwPlay
#----------------Throw Outcomes--------------------------------------
#Outcomes of the possible throw plays
def throwOutcome(throwPlay, down, points, calculatedYardage, totalYardage):
    #Variable in the throw play functions
    oppOdds1 = 0
    oppOdds2 = 0
    playerOdds1 = 0
    playerOdds2 = 0
    newYards = 0
    totalOppOdds = oppOdds1 + oppOdds2
    totalPlayerOdds = playerOdds1 + playerOdds2
    #Short throw
    if throwPlay == 1:
        #Odds for the opponent are between 1 and 3
        oppOdds1 = random.randint(1,3)
        #Odds for the player are between 2 and 8
        playerOdds1 = random.randint(2,6)
        #If the odds of the opponent are greater than the odds of the player
        if oppOdds1 > playerOdds1:
            newYards = oppOdds1-playerOdds1
            return newYards
        #If the odds of the opponent are equal to the odds of the player
        elif oppOdds1 == playerOdds1:
            newYards = 0
            return newYards
        #If the odds of the player are greater than the odds of the opponent
        else:
            #Get the amount of yards gained by subtracting the random numbers they got
            newYards = playerOdds1 - oppOdds1
            return newYards
    #Mid range throw
    elif throwPlay == 2:
        #Variables used in the functions
        oppOdds1 = random.randint(1,6)
        playerOdds1 = random.randint(4,11)
        newYards = 0
        diff = playerOdds1 - oppOdds1
        #If the opponent's odd is larger than the player's odd.
        if oppOdds1 > playerOdds1:
            newYards = diff
            return newYards
        #If the opponent's odd is equal to the player's odd. 
        elif oppOdds1 == playerOdds1:
            newYards = 0
            return newYards
        #If the player's odds is greater than the opponent's odd. 
        else:
            #Gain 6 yards if the difference is between 1 and 3
            if diff <= 3:
                newYards = 6
            #Gain 7 yards if the difference is between 4 and 6
            elif diff <= 6:
                newYards = 7
            #Gain 8 yards is the difference between 7 and 8
            elif diff <= 8:
                newYards = 8
            #Gain 9 or 10 yards depending on the difference. 
            else:
                newYards = diff
            #Return the yards they got from the plays
            return newYards
    #Long Range throw
    elif throwPlay == 3:
        #Variables used in the functions
        oppOdds1 = random.randint(1,8)
        oppOdds2 = random.randint(1,8)
        playerOdds1 = random.randint(1,6)
        playerOdds2 = random.randint(1,6)
        #If the opponents odds are greater than the players
        if totalOppOdds > totalPlayerOdds:
            #If the difference between the opponents odds and players odds are less than or equal to 6.
            if totalOppOdds - totalPlayerOdds <= 6:
                newYards = -1
                return newYards
            #If the difference between the opponents odds and players odds are between 7 and 12
            elif totalOppOdds - totalPlayerOdds > 7 and totalOppOdds - totalPlayerOdds <= 12:
                newYards = -2
                return newYards
            #Any other outcome
            else:
                newYards = -4
                return newYards
        #If the odds of both the players are equal.
        elif totalOppOdds == totalPlayerOdds:
            newYards= 0
            return newYards
        #If the players odds are greater than the opponents odds. 
        else:
            newYards = totalPlayerOdds - totalOppOdds
            newYards = 10 + newYards
            return newYards
    #Throw Play is a hail mary (4)     
    else:
        playerOdds1 = random.randint(1,6)
        playerOdds2 = random.randint(1,6)
        oppOdds1 = random.randint(1,6)
        oppOdds2 = random.randint(1,6)
        totalOppOdds = oppOdds1 + oppOdds2
        totalPlayerOdds = playerOdds1 + playerOdds2
        #The play only works if the sum of players odds are equal to twelve
        if totalPlayerOdds == 12:
            newYards += 30
            return newYards
        #If the sum of the opponents odds are greater than the sum of the players odds. 
        elif totalOppOdds > totalPlayerOdds:
            newYards += -5
            return newYards
        #if the sum of the players odds are greater than the sums of the opponents odds.
        else:
            newYards = 0
            return newYards


#---------------------Run outcomes----------------------------------------------------------------------
#If they choose to run the ball
def runOutcome(down, points, calculatedYardage, totalYardage):
    #Set the values of the variables we will be using to 0
    playerOdds1 = 0
    newYards = 0
    #Get the randomized values
    playerOdds1 = random.randint(1,25)
    #If the players odds are less than or equal to 3. 
    if playerOdds1 <= 3:
        newYards = -playerOdds1*2
        return newYards
    #If the players odds are greater than 3
    else:
        newYards = playerOdds1//2
        return newYards
#-------------------------Kick outcomes-------------------------------------------------
#If thet choose to kick the ball
def kickOutcome(totalYardage, points):
    #set the values equal to 0
    playerOdds1 = 0
    newPoints = 0
    #If they are past the halfway point on the field. 
    if totalYardage > 50:
        playerOdds1 = random.randint(1,5)
        #If the players odds are less than or equal to 4
        if playerOdds1 <= 4:
            newPoints += 3
            return newPoints
        #If the players odds are not less than or equal to 4
        else:
            newPoints = 0
            return newPoints
    #If they have not passed the halfway point on the field
    else:
        playerOdds1 = random.randint(1,17)
        #If the value of the player odds are less than or equal to 2
        if playerOdds1 <= 2:
            newPoints += 3
            return newPoints
        #If its greater than 2
        else:
            newPoints = 0
            return newPoints
#If they choose to kick a field goal.
def fieldGoalOutcome(points):
    #Set the variables used in this function equal to 0
    playerOdds1 = 0
    playerOdds1 = random.randint(1,10)
    #If the players odds are less than or equal to 9
    if playerOdds1 <= 9:
        print("It is good! You have gained an extra point. You finish with 7 points!")
        points += 1
        return points
    #If the players odds are greater than 9
    else:
        print("The field goal was missed. You have gained no points. You finish with 6 points!")
        points += 0
        return points
#---------------------------Main Function----------------------------------------------
#The main function
def main ():
    #Initial Question
    begin = input("Welcome to the football simulation! Would you like to play (yes/no)?\n")
    #All values in the main function and their values. 
    down = 1
    points = 0
    calculatedYardage = 25
    totalYardage = 25
    playYards = 0
    curYard = 0
    newPoints = 0
    kickerfield = 0
    nextFirstDown = 35
    nextFirstDownTotal = 35
    firstDownDistance = 0
    newYards = 0
    #If they want to play
    if begin == "yes" or begin == "Yes" or begin == "YES":
        #Give them the offensive menu. 
        typeofPlay = offenseMenu()
        #If their not over on downs, didnt choose to kick, or don't have more than 0 points. 
        while typeofPlay < 3 and down < 5 and totalYardage < 100 and points == 0:
            #If they choose to throw
            if typeofPlay == 1:
                #Give them their throw options
                throwPlay = throwOptions()
                #Throw choice 1. Short throw
                if throwPlay == 1:
                    newYards = throwOutcome(throwPlay, down, points, calculatedYardage, totalYardage)
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    if newYards < 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        print("You lost", -newYards,"yards.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    elif newYards == 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        print("You gained", newYards,"yards. The play was incomplete.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    else:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        playYards += newYards
                        print("You gained", newYards,"yards!")
                #If they pick choice 2, a mid range throw     
                elif throwPlay == 2:
                    newYards = throwOutcome(throwPlay, down, points, calculatedYardage, totalYardage)
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    if newYards < 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        print("You lost", -newYards,"yards.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    elif newYards == 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        print("You gained", newYards,"yards. The play was incomplete.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    else:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        playYards += newYards
                        print("You gained", newYards,"yards!")
                #If they pick choice 3, a long range throw.   
                elif throwPlay == 3:
                    newYards = throwOutcome(throwPlay, down, points, calculatedYardage, totalYardage)
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    if newYards < 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        print("You lost", -newYards," yards.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    elif newYards == 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        print("You gained", newYards,"yards. The play was incomplete.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    else:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        playYards += newYards
                        print("You gained", newYards,"yards!")
                #If they pick a Hail mary      
                else:
                    newYards = throwOutcome(throwPlay, down, points, calculatedYardage, totalYardage)
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    if newYards < 0:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        newYards= newYards*(-1)
                        print("You lost",newYards," yards.")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    elif newYards > 0:
                        calculatedYardage += 30
                        totalYardage += 30
                        print("IT IS CAUGHT. YOU GAINED 30 YARDS!")
                    #Depending on what the function returns, they will get a certain amount of yardage. 
                    else:
                        calculatedYardage += newYards
                        totalYardage += newYards
                        playYards += newYards
                        print("You gained", newYards,"yards. The play was incomplete.")
                    
            #If they pick to run the ball
            elif typeofPlay == 2:
                newYards = runOutcome(down, points, calculatedYardage, totalYardage)
                #Depending on what the function returns, they will get a certain amount of yardage. 
                if newYards < 0 :
                    calculatedYardage += newYards
                    totalYardage += newYards
                    newYards= newYards*(-1)
                    print("You lost",newYards," yards.")
                #Depending on what the function returns, they will get a certain amount of yardage. 
                else:
                    calculatedYardage += newYards
                    totalYardage += newYards
                    print("You gained", newYards,"yards!")

#--------------- Yardage calculation -------------------------

            #Get the yard of the field they are on.
            #If they are passed 100 total yards, just skip the other "if" functions
            if totalYardage > 100:
                kickerfield = 0
            #If they are passed the halfway line
            elif totalYardage > 50 and totalYardage < 100:
                curYard = totalYardage - 50
                calculatedYardage = 50-curYard
                print("You are down at the", calculatedYardage,"yard line on your opponent's half.")
            #If they have no passed the haldway line
            else:
                print("You are down on your", totalYardage,"yard line.")


            #Calculate the first down
            #If they are passed 100 yards, skip the other "if" functions
            if totalYardage > 100:
                kickerfield = 0
            #If they are passed the halfway line.
            elif totalYardage > 50 and totalYardage < 100:
                #if calculatedYardage <= nextFirstDown:
                if totalYardage >= nextFirstDownTotal:
                    print("You got a first down!")
                    down = 0
                    playYards = 0
                    nextFirstDown = calculatedYardage - 10
                    nextFirstDownTotal = totalYardage + 10
            #If they havent passed the halfway line.
            else:
                #If they get the first down.
                if totalYardage >= nextFirstDownTotal:
                    print("You got a first down!")
                    down = 0
                    playYards = 0
                    nextFirstDown = calculatedYardage + 10
                    nextFirstDownTotal = totalYardage + 10
                
#---------------------Yards till first down-----------------------------
            #Calculate how far they are from a first down.
            #If they gained yardage
            if newYards >= 0:
                #They can't get anymroe first downs if they are passed the 90 yards
                if totalYardage >= 90:
                    print("You cannot get any more first downs, you must score a touchdown or make a field goal!")
                #If they are in between half and the 90 yards
                elif totalYardage > 50 and totalYardage < 90:
                    print("You are",nextFirstDownTotal - totalYardage ," yard(s) away from a first down.")
                #If they haven't passed the halfway line. 
                else:
                    if nextFirstDown > 50:
                        nextFirstDown = nextFirstDown - 50
                        nextFirstDown = 50 - nextFirstDown
                        print("You are", nextFirstDownTotal - totalYardage," yard(s) away from a first down.")
                    else:
                        print("You are", nextFirstDownTotal - totalYardage," yard(s) away from a first down.")
            #If they lost yardage
            else:
                if totalYardage > 50:
                    print("You are", nextFirstDownTotal - totalYardage," yard(s) away from a first down.")
                else:
                    print("You are", nextFirstDownTotal - totalYardage," yard(s) away from a first down.")

#------------------Downs and touchdowns-------------------------------
            #Add one to the downs each time
            down += 1
            #Run it again
            if down < 5:
                print("You are on your", down,"down.")
                print("")
                if totalYardage < 100:
                    typeofPlay = offenseMenu()
            else:
                print("Sorry you lost because you did not get a first down in 4 or less downs!")

            #If they get passed 100 yards, its a touchdown 
            if totalYardage >= 100:
                points += 6
                print("TOUCHDOWN. You now have 6 points.")
                print("Now it is time for the field goal.")
                ans = input("Press enter to continue!")
                print("")
                points = fieldGoalOutcome(points)
        #If they choose to kick, they only get one attempt
        if typeofPlay == 3:
            newPoints = kickOutcome(totalYardage, points)
            if newPoints > 0:
                points+=3
                print("It is good! You have gained 3 points.")
            else:
                points += 0
                print("The field goal was missed. You have gained no points.")
            print("Thank you for trying the football simulator!")
        #If they dont pick 1 or 3
        else:
            print("Thank you for trying the football simulator!")
    #If they choose not to play 
    else:
        print("Have a good one!")
main()

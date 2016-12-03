Clinton = 0
Trump = 0
ClintonTest = 0
need2Vote = True


def Vote():
    global Clinton
    global Trump
    global ClintonTest

    decision = input("Who do you vote for? A = Clinton; B = Trump\n").upper()
    
    if decision == "A":
        Clinton += 1
        ClintonTest += 1
        if ClintonTest%3 == 0:
            Clinton -= 1
            Trump += 1
        else:
            ClintonTest += 0
    elif decision == "B":
        Trump += 1
    else:
        decision = input("Invalid option. Please try again. A = Clinton; B = Trump\n")

    print("Current score: Clinton has %d and Trump has %d" %(Clinton, Trump))




def voting():
    voteNow = True
    Vote()
    
    while voteNow == True:
        stillVoting = input('Would you like to keep voting? Y for yes, N for no.\n').upper()
        if stillVoting == 'Y' or stillVoting == 'N':
            if stillVoting == 'Y':
                Vote()
            elif stillVoting == 'N':
                break
        else:
            print('That is not an option. Please try again.\n')

voting()

# Ryan Lugo: RJL 12/14/21

import random as rand

clones = []

def clone_number(numberClone=0):
    clone_question = input("Name a clone? ")

    if clone_question.lower() == "y":

        current_clone = numberClone

        number = rand.randrange(0,9999)
        if len(str(number)) == 4:
            current_clone = clones.append("CT-"+str(number))
        elif len(str(number)) == 3:
            numb = rand.randrange(0,9)
            current_clone = clones.append("CT-"+str(number)+str(numb))
        elif len(str(number)) == 2:
            numbTwo = rand.randrange(0,99)
            current_clone = clones.append("CT-"+str(number)+str(numbTwo))
        elif len(str(number)) == 1:
            numbThree = rand.randrange(0,999)
            current_clone = clones.append("CT-"+str(number)+str(numbThree))
        
        clone = clones[current_clone]

        current_clone += 1

        print(clone)
        
        clone_number()
    elif clone_question.lower() == "n":
        print(clones)
    else:
        print("Hmm, it seems you didn't put Y or N, try again..")
        clone_number()

clone_number()

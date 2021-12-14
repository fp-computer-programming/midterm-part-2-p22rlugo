# Ryan Lugo: RJL 12/14/21

def avg_acc(init_veloc,final_veloc,time):
    """Getting the Average Acceleration in the object"""

    average = (final_veloc - init_veloc) / time

    return average


init_question = int(input("What is the Initial Velocity?: "))
final_question = int(input("What is the Final Velocity?: "))
time_question = int(input("What is the Time?: "))

print("Here's the Average Acceleration!:",avg_acc(init_question,final_question,time_question))
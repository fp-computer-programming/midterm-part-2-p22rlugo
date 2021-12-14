# Ryan Lugo: RJL 12/14/21

def cost_of_trip(distance,fuel_efficiency,fuel_price):
    """We calculate the trip and print values, you decide the credits worth"""
    mpg = fuel_efficiency * distance
    total_gas_cost = mpg * fuel_price


    return total_gas_cost

question_one = int(input("What is the driving distance?(Miles): "))
question_two = int(input("What is the Fuel Efficiency?(Miles-Per-Gallon?): "))
question_three = int(input("What is the price of fuel?(Credit-per-gallon): "))

print("Here's the total cost of the trip!",cost_of_trip(question_one,question_two,question_three))
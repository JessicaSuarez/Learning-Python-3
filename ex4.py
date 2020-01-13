#Jessica Suarez
#Ex4 Variables and Names
#Here the variables are being defined and given values
#the amount of cars
cars = 100
#the amount of passengers that fit per car
space_in_a_car = 4
#the amount of drivers
drivers = 30
#the amount of passengers
passengers = 90
#cars that do not have drivers are computed Here
cars_not_driven = cars - drivers
#cars with drivers are computed here
cars_driven = drivers
#space in car for carpool is cars * the space in a car
carpool_capacity = cars_driven * space_in_a_car
#average people in a car
average_passengers_per_car = passengers / cars_driven

#The computations above in the variables are simply plugged into the print statements using the variable name defined above.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

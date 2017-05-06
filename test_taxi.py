
from car import Taxi, SilverServiceTaxi




def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4)]
    print("Lets Drive!")
    print("q)uit, c)hoose, d)rive")
    user_input = input()

    if user_input == "c":
        print(taxis)
        taxi_choice = input("Choose taxi: ")
        print("Bill to date: ${:.2f}".format(taxis[taxi_choice].getfare))

    if user_input == "d":
        drive_distance = input("Drive how far? ")
        










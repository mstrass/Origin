import sys

class Train:
    def __init__(self,location,cargo = False):
        self.location = location
        self.cargo = cargo
    def __str__(self):
        return f"Current location:\n     {self.location} \n\nCargo?\n     {self.cargo}"       

class Station:
    def __init__(self,location,cargo = True):
        self.location = location
        self.cargo = cargo
    def __str__(self):
        return f"Location {self.location} Cargo? {self.cargo}"


def motion():
    if train_1.location == 'station_1':
        train_1.location ='station_2'
    elif train_1.location == 'station_2':
        train_1.location = "station_3"
    else:
        train_1.location = 'station_1'

def transfer():
    if train_1.cargo == False and station_1.cargo == True:
        train_1.cargo = True
        station_1.cargo = False
    else:
        train_1.cargo = False
        station_1.cargo = True        

station_1 = Station('station_1', False)
station_2 = Station('station_2', False)
station_3 = Station('station_3', False)
train_1 = Train('station_1',True)


affirmative = ['','y','ye','yes']
end_game = False
while not end_game:
    user_input = input("Travel to the next station?\n")
    print(train_1)
    user_input = user_input.lower()
    if user_input == 'end':
        end_game = True
    elif user_input in affirmative:
         motion()
         transfer()
    else:
        print("I do not understand that input")



sys.exit() 

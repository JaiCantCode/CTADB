from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
connection_url="mongodb+srv://lucuser:csclassluc@luccluster.7jdjevt.mongodb.net/?retryWrites=true&w=majority&appName=LUCcluster"
client = MongoClient(connection_url)
db = client["comp_353"]


#define train class in python with save functions
class Train:
    def __init__(self,tID,tStopNum):
        self.tID = tID
        self.tStopNum = tStopNum
    
    def save(self):
        train_data = {
            "tID": self.tID,
            "tStopNum" : self.tStopNum
        }
        db.train.insert_one(train_data)

# tId, tStopNum
trains = [
    Train("R1",5),
    Train("R2",5),
    Train("B1",4),
    Train("B2",4),
    Train("Y1",3)
]

# saves train insertions
for train in trains:
    train.save()
        

#define station class in python with init and save functions
class Station:
    def __init__(self, sName, sAccessibility, sTransfer):
        self.sName = sName
        self.sAccessibility = sAccessibility
        self.sTransfer = sTransfer

    def save(self):
        station_data = {
            "sName": self.sName,
            "sAccessibility": self.sAccessibility,
            "sTransfer": self.sTransfer
        }
        db.station.insert_one(station_data)

# sName,SAccessability,sTransfer
stations = [
    Station("Howard", True, {"bus": False, "train": True}),
    Station("Loyola", True, {"bus": False, "train": False}),
    Station("Oakton-Skokie", False, {"bus": False, "train": False}),
    Station("Dempster-Skokie", True, {"bus": False, "train": False}),
    Station("O'Hare", False, {"bus": False, "train": False}),
    Station("Wilson", False, {"bus": False, "train": False}),
    Station("Lake", False, {"bus": False, "train": False}),
    Station("Belmont", False, {"bus": False, "train": False}),
    Station("Damen", False, {"bus": False, "train": False}),
    Station("Irving Park", False, {"bus": False, "train": False}),
]

# saves station insertions
for station in stations:
    station.save()


#define train_schedule class in python with init and save function
class train_schedule:
    def __init__(self, tDirection, tColor, tID, tRoute, tArrivalTime, tDepartureTime):
        self.tDirection = tDirection
        self.tColor = tColor
        self.tID = tID
        self.tRoute = tRoute
        self.tArrivalTime = tArrivalTime
        self.tDepartureTime = tDepartureTime

    def save(self):
        schedule_data = {
            "tDirection": self.tDirection,
            "tColor": self.tColor,
            "tID": self.tID,
            "tRoute": self.tRoute,
            "tArrivalTime": self.tArrivalTime,
            "tDepartureTime": self.tDepartureTime
        }
        db.train_schedule.insert_one(schedule_data)

# Define train schedule data
train_schedules = [
    train_schedule(
        "northwest", "yellow", "Y1",
        [{"sName": "Howard"}, {"sName": "Oakton-Skokie"}, {"sName": "Dempster-Skokie"}],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40)],
        [datetime(2025, 4, 14, 12, 15), datetime(2025, 4, 14, 12, 30), datetime(2025, 4, 14, 12, 45)]
    ),
    train_schedule(
        "south", "red", "R1",
        [{"sName": "Howard"}, {"sName": "Loyola"}, {"sName": "Wilson"}, {"sName": "Belmont"}, {"sName": "Lake"}],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40),
         datetime(2025, 4, 14, 12, 55), datetime(2025, 4, 14, 12, 10)],
        [datetime(2025, 4, 14, 12, 15), datetime(2025, 4, 14, 12, 30), datetime(2025, 4, 14, 12, 45),
         datetime(2025, 4, 14, 13, 0), datetime(2025, 4, 14, 13, 15)]
    ),
    train_schedule(
        "north", "red", "R2",
        [{"sName": "Lake"}, {"sName": "Belmont"}, {"sName": "Wilson"}, {"sName": "Loyola"}, {"sName": "Howard"}],
        [datetime(2025, 4, 14, 12, 5), datetime(2025, 4, 14, 12, 20), datetime(2025, 4, 14, 12, 35),
         datetime(2025, 4, 14, 12, 50), datetime(2025, 4, 14, 13, 5)],
        [datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40),
         datetime(2025, 4, 14, 12, 55), datetime(2025, 4, 14, 13, 10)]
    ),
    train_schedule(
        "west", "blue", "B1",
        [{"sName": "Lake"}, {"sName": "Damen"}, {"sName": "Irving Park"}, {"sName": "O'Hare"}],
        [datetime(2025, 4, 14, 12, 30), datetime(2025, 4, 14, 12, 45), datetime(2025, 4, 14, 13, 0), datetime(2025, 4, 14, 13, 15)],
        [datetime(2025, 4, 14, 12, 35), datetime(2025, 4, 14, 12, 50), datetime(2025, 4, 14, 13, 5), datetime(2025, 4, 14, 13, 20)]
    ),
    train_schedule(
        "east", "blue", "B2",
        [{"sName": "O'Hare"}, {"sName": "Irving Park"}, {"sName": "Damen"}, {"sName": "Lake"}],
        [datetime(2025, 4, 14, 11, 50), datetime(2025, 4, 14, 12, 5), datetime(2025, 4, 14, 12, 20), datetime(2025, 4, 14, 12, 35)],
        [datetime(2025, 4, 14, 11, 55), datetime(2025, 4, 14, 12, 10), datetime(2025, 4, 14, 12, 25), datetime(2025, 4, 14, 12, 40)]
    ),
]

# Save train_schedule insertions
for schedule in train_schedules:
    schedule.save()

train_data = db.train_schedule.find_one({"tID": "R1"})
print(train_data)


class Passenger:
    def __init__(self, pID, pName,pBalance ):
        self.pBalance = pBalance
        self.pName = pName
        self.pID = pID

    def save(self):
        passenger_data = {
            "pBalance": self.pBalance,
            "pName": self.pName,
            "pID": self.pID,
        }
        db.passenger.insert_one(passenger_data)

passengers = [
    Passenger(1, "Arthur Morgan", 50),
    Passenger(2, "Mark Zuckerberg", 10),
    Passenger(3, "Charlie Brown", 76),
    Passenger(4, "Jane Doe", 22),
    Passenger(5, "John Smith", 13),
    Passenger(6, "Emma Watson", 31),
    Passenger(7, "Bruce Wayne", 10),
    Passenger(8, "Clark Kent", 6)
]

for passenger in passengers:
    passenger.save()

class Bus:
    def __init__(self, bID, bStopNum):
        self.bID = bID
        self.bStopNum = bStopNum

    def save(self):
        bus_data = {
            "bID": self.bID,
            "bStopNum": self.bStopNum
        }
        db.bus.insert_one(bus_data)

busses = [
    Bus("N8x0", 0),
    Bus("N8x1", 1),
    Bus("N8x2", 2),
    Bus("S8x0", 12),
    Bus("S8x1", 11),
    Bus("S8x2", 10),
    Bus("E51x0", 4),
    Bus("E51x1", 5),
    Bus("E51x2", 6),
    Bus("W51x0", 15),
    Bus("W51x1", 14),
    Bus("W51x2", 13)
]

for bus in busses:
    bus.save()
        
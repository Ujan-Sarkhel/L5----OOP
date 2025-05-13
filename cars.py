class BMW():
    def color(self):
        print("black")
class FERRARI():
    def color(self):
        print("red")
ob1=BMW()
ob2=FERRARI()

for vehicle in (ob1, ob2):
    vehicle.color()
    
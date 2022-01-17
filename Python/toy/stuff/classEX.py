class HousePark:
    
    lastname = "박"
    
    
    def __init__(self,name):
        self.fullname = self.lastname + " " + name
        
    def travel(self, where):
        print(f"{self.fullname}, {where}여행을 가다.")
        
    def love(self, other):
        print(f"{self.fullname}, {other.fullname} 사랑에 빠졌네")
        
    def fight(self, other):
        print(f"{self.fullname}, {other.fullname} 또 싸우네")
        
    def __add__(self, other):
        print(f"{self.fullname}, {other.fullname} 결혼했네")
        
    def __sub__(self, other):
        print(f"{self.fullname}, {other.fullname} 결국 이혼했네")
        
class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print(f"{self.fullname}, {where}여행 {day}일 가네")
        
p2 = HousePark("wuangza")
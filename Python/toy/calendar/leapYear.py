class CalDays:   
    def __init__(self, y, m ,d):
        self.y = y
        self.m = m
        self.d = d
    
    def setYMD(self, y, m, d):
        self.y, self.m, self.d = int(y), int(m), int(d)
    

    def daysCheck(self, day):
        list = ["일", "월", "화", "수", "목", "금", "토"]
        #print(f"{list[(day-1)%7]}요일 입니다.")
        return (day-1)%7

    def yearMonthDay(self):

        totalDay = 0

        #print(f"입력받은 년: {self.y}, 월: {self.m}, 일: {self.d}")
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.yCheck(self.y) == True:
            #윤년일떄
            month[1] = 29
        else:
            #평년일때
            month[1] = 28

        #작년까지 모든 일수를 더한 후
        #올해 월과 일을 더하는 방식으로
        for i in range(1, self.y):
            totalDay += 365

        #전월까지 일수를 모두 더하고
        for i in range(0,(self.m-1)):
            totalDay += month[i]

        #당월은 입력받은 날자만 더합니다.
        list = [self.daysCheck(totalDay + self.d)]
        list.append(month[self.m])
        return list
    
    def yCheck(self, y):
        if y % 400 == 0:
            #print("윤년입니다.")
            return True
        elif y % 100 != 0 and y % 4 == 0:
            #print("윤년입니다.")
            return True
        else:
            #print("평년입니다.")
            return False     


class showCal():
    def __init__(self,list, start):
        self.list = list
        self.start = start
    def printC(self):
        month = self.list
        start = self.start

        days = [0, 1, 2, 3, 4, 5, 6]

        for i in range(1, month[0]+1):
            if i is 1:
                print("   "*start, end = '')
            print(f"{i:3}", end = '')
            
            if start == 0:
                start = 7
            if i % 7 == 7-start:
                print()


cal1 = CalDays(2022, 1, 11)
calRes = cal1.yearMonthDay()
print(calRes[0])
print(calRes[1])


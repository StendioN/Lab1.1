from datetime import time


class TimeIL:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return '{}:{}:{}'.format(self.hours, self.minutes, self.seconds)

    def input_time(self):
        self.hours = int(input())
        self.minutes = int(input())
        self.seconds = int(input())

    def datetime_time(self):
        self.hours = int(input())
        self.minutes = int(input())
        self.seconds = int(input())
        t = time(self.hours, self.minutes, self.seconds)
        return print(t)

    def display_time(self):
        if self.hours > 23 or self.hours < 0 or self.minutes > 59 or self.minutes < 0 or self.seconds > 59 or \
                self.seconds < 0:
            print('Error: Entered time is not correct')
        else:
            if self.hours <= 12:
                print(f'{self.hours}:{self.minutes}:{self.seconds} AM')
            else:
                print(f'{self.hours}:{self.minutes}:{self.seconds} PM')

    def add_time(self, time_1):
        self.hours += time_1.hours
        self.minutes += time_1.minutes
        self.seconds += time_1.seconds
        if self.hours < 0 or self.minutes < 0 or self.seconds < 0:
            return 'Error: Countered time is not correct'
        if self.seconds > 59:
            self.seconds = self.seconds - 60
            self.minutes = self.minutes + 1
        if self.minutes > 59:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1
        if self.hours > 23:
            self.hours = self.hours - 24
        return TimeIL(self.hours, self.minutes, self.seconds)

    def sub_time(self, time_1):
        self.hours -= time_1.hours
        self.minutes -= time_1.minutes
        self.seconds -= time_1.seconds
        if self.seconds < 0:
            self.seconds = self.seconds + 60
            self.minutes = self.minutes - 1
        if self.minutes < 0:
            self.minutes = self.minutes + 60
            self.hours = self.hours - 1
        if self.hours < 0:
            self.hours = self.hours + 24
        return TimeIL(self.hours, self.minutes, self.seconds)


time1 = TimeIL(20, 58, 57)
time1.display_time()
time2 = TimeIL(18, 5, 19)
time2.display_time()
time3 = TimeIL(15, 4, 16)
time3.display_time()
time4 = TimeIL(20, 7, 39)
time4.display_time()
time5 = TimeIL()
time5.input_time()
time5.display_time()
time6 = TimeIL()
time6.datetime_time()
print(f"time1 + time2 = {time1.add_time(time2)}")
print(f"time2 + time6 = {time2.add_time(time6)}")
print(f"time3 - time5 = {time3.sub_time(time5)}")
print(f"time5 - time4 = {time5.sub_time(time4)}")

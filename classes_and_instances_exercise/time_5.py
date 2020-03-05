class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.seconds == self.max_seconds - 1 or self.seconds == self.max_seconds:
            self.seconds = 0
            if self.minutes == self.max_minutes - 1 or self.minutes >= self.max_minutes:
                self.minutes = 0
                self.hours += 1
            else:
                self.minutes += 1
            if self.hours == self.max_hours - 1 or self.hours >= self.max_hours:
                self.hours = 0
            elif self.hours >= self.max_hours:
                self.hours = 1
        return self.get_time()

time: Time = Time(9, 30, 60)
print(time.next_second())
time: Time = Time(10, 59, 59)
print(time.next_second())
time: Time = Time(24, 59, 59)
print(time.next_second())
time: Time = Time(5, 60, 60)
print(time.next_second())
time: Time = Time(23, 59, 59)
print(time.next_second())

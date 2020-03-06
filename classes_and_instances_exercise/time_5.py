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
        if self.seconds == Time.max_seconds - 1 or self.seconds == Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1
        if self.minutes >= Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0
        return self.get_time()


time: Time = Time(9, 30, 60)
print(time.next_second())
time: Time = Time(10, 59, 59)
print(time.next_second())
time: Time = Time(24, 59, 59)
print(time.next_second())
time: Time = Time(5, 60, 60)
print(time.next_second())
time: Time = Time(1, 59, 59)
print(time.next_second())
time: Time = Time(23, 59, 9)
print(time.next_second())
time: Time = Time(24, 59, 59)
print(time.next_second())

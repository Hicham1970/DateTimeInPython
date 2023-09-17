

# python program to convert hours to days


class Time:
    def EnterTime(self):
        self.__h = int(input('Enter Hrs: '))
        self.__m = int(input('Enter Minutes: '))
        self.__s = int(input('Enter Seconds: '))

    def PutResult(self):
        print('{} Days {} Hours {} Minutes {} Seconds'.format(self.__d, self.__h, self.__m, self.__s))

    def __add__(self, Time):
        TimeObj = Time()
        TimeObj.__h = self.h + Time.__h
        TimeObj.__m = self.h + Time.__m
        TimeObj.__s = self.h + Time.__s

        TimeObj.__m = TimeObj.__m + (TimeObj.__s // 60)
        TimeObj.__s = TimeObj.__s % 60

        TimeObj.__h = TimeObj.__h + (TimeObj.__m // 60)
        TimeObj.__m = TimeObj.__m % 60

        TimeObj.__d = TimeObj.__h // 24
        TimeObj.__h = TimeObj.__h % 24

        return TimeObj

    First_time = Time()
    Second_time = Time()

    print('Enter value for the time object 1 : ')
    First_time.EnterTime()

    print('Enter value for the time object 2 : ')
    Second_time.EnterTime()

    print('The total time elapsed is =')
    Ttime = First_time + Second_time
    Ttime.PutResult()






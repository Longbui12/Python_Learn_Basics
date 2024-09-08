class date:
    # Contructor:
    def __init__(self, value_date, value_month, value_year):
        self.date = value_date
        self.month = value_month
        self.year = value_year
    
    # Determine the number of days in the month:
    # static mothod:
    def numberOfDaysTheMonth(month, year):
        if(month in [1,3,5,7,8,10,12]):
          return 31
        elif(month in [4,6,9,11]):
            return 30
        elif(month == 2):
            if(year % 400 == 0 or (year % 4 == 0 and year % 100 !=0)):
                return 29
            else:
                return 28
    
     #ex : 9/9/2924:
     # Jan: 31 days
     # Feb: 29 days
     # Mar: 31 days
     # Apr : 30 days
     # May : 31 days
     # Jun : 30 days
     # Jul : 31 days
     # Aug : 31 days
     # Sep : 30 days
     # Oct : 31 days
     # Nov : 30 days
     # Dec : 31 days
   
    def dayOfTheYear(self):
        dayValueOfTheYear = 0
        # Calculate the total number of days in previous months:
        for x in range(1, self.month):
            #dayValueOfTheYear += self.numberOfDaysTheMonth(x, self.year) false at 'self.'😀😀
            dayValueOfTheYear += date.numberOfDaysTheMonth(x, self.year)
        # Add the number of days in the current month :
        dayValueOfTheYear += self.date
        # Returns results:
        return dayValueOfTheYear
    
dateA = date(9 , 9 , 2024)
print('The ' + str(dateA.dayOfTheYear()) + ' day of the year !👌👌')

dateB = date(15 , 1 , 2024)
print('The ' + str(dateB.dayOfTheYear()) + ' day of the year !👌👌')
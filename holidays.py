#  holidays.py: -*- Python -*-  DESCRIPTIVE TEXT.
#  
#  Author: Phil Schwartz (phil_schwartz@users.sourceforge.net) 
#  Date: Thu Jan  9 20:00:52 2003.
#  More Jewish Holidays added by Jane Kim (janecakemaster@gmail.com)

import time
import calendar
import calendar_util

#############################################################################################

# time tuple/list index
YEAR = 0
MONTH = 1
DAY = 2
WEEKDAY = 6

# weekdays
MON=0
TUE=1
WED=2
THU=3
FRI=4
SAT=5
SUN=6

# months
JAN=1
FEB=2
MAR=3
APR=4
MAY=5
JUN=6
JUL=7
AUG=8
SEP=9
OCT=10
NOV=11
DEC=12

# Hebrew months
Nisan=1
Iyyar=2
Sivan=3
Tammuz=4
Av=5
Elul=6
Tishri=7
Heshvan=8
Kislev=9
Teveth=10
Shevat=11
Adar=12
Veadar=13

HEBREW_YEAR_OFFSET = 3760

HAVE_30_DAYS = (APR,JUN,SEP,NOV)
HAVE_31_DAYS = (JAN,MAR,MAY,JUL,AUG,OCT,DEC)

SECONDS_PER_DAY = 60 * 60 * 24


#############################################################################################

class Holidays:
    def __init__(self, year=None):
        self.time_list = list(time.localtime())
        if year:
            self.set_year(year)
        

    def get_epoch(self):
        t = tuple(self.time_list)
        return time.mktime(t)


    def get_tuple(self):
        secs = self.get_epoch()
        return time.localtime(secs)
        #return tuple(self.time_list)

    
    def set_year(self, year):
        self.time_list[YEAR] = year


    def get_nth_day_of_month(self, n, weekday, month, year=None):
        # doesn't set the time list
        # returns the day of the month 1..31
        if not year:
            year = self.time_list[YEAR]

        firstday, daysinmonth = calendar.monthrange(year, month)

        # firstday is MON, weekday is WED -- start with 3rd day of month
        # firstday is WED, weekday is MON --
        # firstday = weekday
        if firstday < weekday:
            date = weekday - firstday + 1 # 2 - 0 + 1
        elif firstday > weekday:
            date = 7 - (firstday - weekday) + 1
        else:
            date = 1

        if n == 1:
            return date

        for i in range(1, n):
            date += 7
            if month in HAVE_30_DAYS and date > 30:
                raise IndexError
            if month in HAVE_31_DAYS and date > 31:
                raise IndexError
            if month == FEB and date > 28:
                ignore, daysinfeb = calendar.monthrange(year, FEB)
                if date > daysinfeb:
                    raise IndexError

        return date


    def hebrew_to_gregorian(self, year, hebrew_month, hebrew_day, year_is_gregorian=1):
        if year_is_gregorian:
            # gregorian year is either 3760 or 3761 years less than hebrew year
            # we'll first try 3760 if conversion to gregorian isn't the same
            # year that was passed to this method, then it must be 3761.
            for y in (year + HEBREW_YEAR_OFFSET, year + HEBREW_YEAR_OFFSET + 1):
                jd = calendar_util.hebrew_to_jd(y, hebrew_month, hebrew_day)
                gd = calendar_util.jd_to_gregorian(jd)
                if gd[YEAR] == year:
                    break
                else:
                    gd = None
        else:
            jd = calendar_util.hebrew_to_jd(year, hebrew_month, hebrew_day)        
            gd = calendar_util.jd_to_gregorian(jd)

        if not gd: # should never occur, but just incase...
            raise RangeError, "Could not determine gregorian year"
        
        return gd # (tuple:  y. m, d))


    def adjust_date(self):
        # after a date calculation, this method will coerce the list members to ensure
        # that they are within the correct bounds.  That is, a date of Oct 32 becomes Nov 1, etc
        tm = (self.time_list[YEAR], self.time_list[MONTH], self.time_list[DAY], 0,0,0,0,0,-1)
        e = time.mktime(tm)
        tm = time.localtime(e)        
        self.time_list[MONTH] = tm[MONTH]
        self.time_list[DAY] = tm[DAY]

        

    ###### Jewish holidays begin the evening before the first day of the holiday
    ###### therefor each function, set_holiday() returns the first day
    ###### and the function set_holiday_eve() returns the prior day.

    def set_hanukkah(self, year=None):
        # need an algorithm to comute gregorian first day...
        if year:
            self.set_year(year)
            
        gd = self.hebrew_to_gregorian(self.time_list[YEAR], Kislev, 25)
        self.time_list[MONTH] = gd[MONTH]
        self.time_list[DAY] = gd[DAY]

    def set_hanukkah(self, year=None):
        # need an algorithm to comute gregorian first day...
        if year:
            self.set_year(year)
            
        gd = self.hebrew_to_gregorian(self.time_list[YEAR], Kislev, 25)
        self.time_list[MONTH] = gd[MONTH]
        self.time_list[DAY] = gd[DAY]
        
    
    def set_hanukkah_eve(self, year=None):
        self.set_hanukkah(year)
        self.time_list[DAY] -= 1
        self.adjust_date()


    def set_hanukkah_end(self, year=None):
        self.set_hanukkah_eve(year)
        self.time_list[DAY] += 8
        self.adjust_date()


    def set_rosh_hashanah(self, year=None):
        if year:
            self.set_year(year)

        gd = self.hebrew_to_gregorian(self.time_list[YEAR], Tishri, 1)
        self.time_list[MONTH] = gd[MONTH]
        self.time_list[DAY] = gd[DAY]


    def set_rosh_hashanah_eve(self, year=None):
        self.set_rosh_hashanah(year)
        self.time_list[DAY] -= 1
        self.adjust_date()


    def set_rosh_hashanah_end(self, year=None):
        self.set_rosh_hashanah(year)
        self.time_list[DAY] += 1
        self.adjust_date()

    def set_yom_kippur(self, year=None):
        if year:
            self.set_year(year)

        gd = self.hebrew_to_gregorian(self.time_list[YEAR], Tishri, 10)
        self.time_list[MONTH] = gd[MONTH]
        self.time_list[DAY] = gd[DAY]
        return gd


    def set_yom_kippur_eve(self, year=None):
        self.set_rosh_hashanah(year)
        self.time_list[DAY] += 8
        self.adjust_date()

       
    def set_passover(self, year=None):
        if year:
            self.set_year(year)

        gd = self.hebrew_to_gregorian(self.time_list[YEAR], Nisan, 15)
        self.time_list[MONTH] = gd[MONTH]
        self.time_list[DAY] = gd[DAY]


    def set_passover_eve(self, year=None):
        self.set_passover(year)
        self.time_list[DAY] -= 1
        self.adjust_date()

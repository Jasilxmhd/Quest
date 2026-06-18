'Date and Time Module'


from datetime import *

# print("Current date and time : ",datetime.now())   # Current date and time :  2026-05-07 11:29:22.957850
# print(date.today())                                # 2026-05-07
# print("current year :",datetime.now().year)        # current year : 2026
# print(datetime.now().month)                        # 5
# print(datetime.now().day)                          # 7
# print(datetime.now().time())                       # 11:32:33.053018
# print(datetime.now().hour)                         # 11
# print(datetime.now().minute)                       # 33
# print(datetime.now().second)                       # 49
# print(datetime.now().microsecond)                  # 441407







dt = datetime.now()
# print(dt)

# print('%Y  ->',dt.strftime('%Y'))   # Year , full                      2026
# print('%y  ->',dt.strftime('%y'))   # Year , short                       26
# print('%m  ->',dt.strftime('%m'))   # month number                       05
# print('%B  ->',dt.strftime('%B'))   # month name (full)                 May
# print('%b  ->',dt.strftime('%b'))   # month name (short)                May
# print('%d  ->',dt.strftime('%d'))   # day of month                       07
# print('%A  ->',dt.strftime('%A'))   # week day (full)              Thursday
# print('%a  ->',dt.strftime('%a'))   # week day (short)                  Thu
# print('%H  ->',dt.strftime('%H'))   # Hour (24 - hour)                   12
# print('%I  ->',dt.strftime('%I'))   # Hour (12 - hour)                   12
# print('%p  ->',dt.strftime('%p'))   # AM / PM                            PM
# print('%M  ->',dt.strftime('%M'))   # Minute                             02
# print('%S  ->',dt.strftime('%S'))   # Second                             13
# print('%f  ->',dt.strftime('%f'))   # Micro second                   449816
# print('%z  ->',dt.strftime('%z'))   # UTC offset
# print('%Z  ->',dt.strftime('%Z'))   # Timezone name
# print('%j  ->',dt.strftime('%j'))   # Day of year                       127
# print('%U  ->',dt.strftime('%U'))   # week number (sunday first)         18
# print('%W  ->',dt.strftime('%W'))   # week number (Monday first)         18
# print('%c  ->',dt.strftime('%c'))   # Local's date and time              Thu May  7 12:02:13 2026
# print('%x  ->',dt.strftime('%x'))   # Local's date                  05/07/26
# print('%X  ->',dt.strftime('%X'))   # Local's time                  12:02:13
















# data = datetime(2004, 9, 7)
# print(data.day)              # 7
# print(data.month)            # 9
# print(data.year)             # 2004





























# today = datetime.today()
# print(today)                                    # 2026-05-07 12:08:51.093004

# after_7_days = today + timedelta(days=7)
# print(after_7_days)                             # 2026-05-14 12:08:51.093004



























'Age calculate'

# data = datetime(2004, 9, 7)
# now = datetime.today()

# result = now - data

# print(result.days/365)

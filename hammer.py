# Breakfast: 7AM - 9AM
#Lunch: 12PM - 2PM
#Dinner: 7PM - 9PM
#Hammer: 10PM - 4AM

time = input(str("Tell me the time: "))
# Split the input at the space between time and am/pm.
meridian = time[-2:]
hour = int(time[:-2])
# # Check that that works
# print(hour)
# print(meridean)
# try isnumeric(hour):
#     pass
# except Exception as e:
#     raise
# Set up the conditionals
if meridian.lower() == 'am':
    if 7 <= hour <= 9:
        print(f"{time} is breakfast time!")
    elif hour == 12 or hour <= 4:
        print(f"{time} is hammer time!")

elif meridian.lower() == 'pm':
    if 7 <= hour <= 9:
        print(f"{time} is dinner time!")
    if hour == 12 or hour >= 2:
        print(f"{time} is lunch time!")
else:
    print("Are you sure you should be eating right now?")

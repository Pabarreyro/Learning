# def unit_convert(): # Distance conversion function assignment.
#     while True:
#         orig_value = float(input("Enter a distance: "))
#         input_unit = str(input("What unit are you starting with (mi, km, m, or ft)? "))
#         output_unit = str(input("What would you like to convert to (mi, km, m, or ft)? "))
#         # Create conditions for input and output for all scenarios
#         if input_unit == 'mi':
#             if output_unit == 'km': #miles to kilometers
#                 conv_fac = 1.609344 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print (f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'm': #miles to meters
#                 conv_fac = 0.000621371192 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'ft': #miles to feet
#                 conv_fac = 5280 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#         elif input_unit == 'km':
#             if output_unit == 'mi': #kilometers to miles
#                 conv_fac = .621371 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'm': #kilometers to meters
#                 conv_fac = 1000 #conversion factor
#                 output_uvalue = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'ft': #kilometers to feet
#                 conv_fac = 3280.84 #conversion factor
#                 output_value = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#         elif input_unit == 'm':
#             if output_unit == 'km': #meters to kilometers
#                 conv_fac = .001 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'mi': #meters to miles
#                 conv_fac = .000621371 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'ft': #meters to feet
#                 conv_fac = 3.28084 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#         elif input_unit == 'ft':
#             if output_unit == 'km': #feet to kilometers
#                 conv_fac = .0003048000097536 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'mi': #feet to miles
#                 conv_fac = 0.00018939394545454545809 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#
#             elif output_unit == 'm': #feet to meters
#                 conv_fac = 0.3048000097535999986 #conversion factor
#                 output_unit = float(orig_value) * conv_fac
#                 print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
#         else:
#             print("Something went wrong. Shall we try again?")

meters_per_kilometer = 1000
meters_per_foot = 1 / 3.2808398950131
feet_per_mile = 5280

input_amount = float(input('Amount: '))
input_units = input('Starting units: ')
output_units = input('Requested units: ')

if input_units == 'm':
    meter_amount = input_amount
elif input_units == 'km':
    meter_amount = input_amount * meters_per_kilometer
elif input_units == 'ft':
    meter_amount = input_amount * meters_per_foot
elif input_units == 'mi':
    meter_amount = input_amount * feet_per_mile * meters_per_foot

if output_units == 'm':
    output_amount = meter_amount
elif output_units == 'km':
    output_amount = meter_amount / meters_per_kilometer
elif output_units == 'ft':
    output_amount = meter_amount / meters_per_foot
elif output_units == 'mi':
    output_amount = meter_amount / feet_per_mile / meters_per_foot

print(input_amount + ' ' + input_units + ' is ' + output_amount + ' ' +
      output_units)

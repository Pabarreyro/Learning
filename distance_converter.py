def unit_convert(): # Distance conversion function assignment.
    while True:
        orig_value = float(input("Enter a distance: "))
        input_unit = str(input("What unit are you starting with (mi, km, m, or ft)? "))
        output_unit = str(input("What would you like to convert to (mi, km, m, or ft)? "))
        # Create conditions for input and output for all scenarios
        if input_unit == 'mi':
            if output_unit == 'km': #miles to kilometers
                conv_fac = 1.609344 #conversion factor
                output_value = float(orig_value) * conv_fac
                print (f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'm': #miles to meters
                conv_fac = 0.000621371192 #conversion factor
                output_value = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'ft': #miles to feet
                conv_fac = 5280 #conversion factor
                output_value = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

        elif input_unit == 'km':
            if output_unit == 'mi': #kilometers to miles
                conv_fac = .621371 #conversion factor
                output_value = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'm': #kilometers to meters
                conv_fac = 1000 #conversion factor
                output_uvalue = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'ft': #kilometers to feet
                conv_fac = 3280.84 #conversion factor
                output_value = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

        elif input_unit == 'm':
            if output_unit == 'km': #meters to kilometers
                conv_fac = .001 #conversion factor
                output_unit = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'mi': #meters to miles
                conv_fac = .000621371 #conversion factor
                output_unit = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'ft': #meters to feet
                conv_fac = 3.28084 #conversion factor
                output_unit = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

        elif input_unit == 'ft':
            if output_unit == 'km': #feet to kilometers
                conv_fac = .0003048000097536 #conversion factor
                output_unit = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'mi': #feet to miles
                conv_fac = 0.00018939394545454545809 #conversion factor
                output_unit = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")

            elif output_unit == 'm': #feet to meters
                conv_fac = 0.3048000097535999986 #conversion factor
                output_unit = float(orig_value) * conv_fac
                print(f"{orig_value} {input_unit} = {output_value} {output_unit}")
        else:
            print("Something went wrong. Shall we try again?")

# def conver_distance(dis, convert_from, convert_to):
#     if c_from.lower() == 'mi':
#         if c_to.lower() == 'km':
#             pass
#         elif c_to.lower() == 'ft':
#             pass
#         elif c_to.lower() == 'm':
#             pass
#     elif c_from.lower() == 'km':
#         if c_to.lower() == 'mi':
#             pass
#         elif c_to.lower() == 'ft':
#             pass
#         elif c_to.lower() == 'mi':
#             pass
#     elif c_from.lower() == 'm':
#         if c_to.lower() == 'mi':
#             pass
#         elif c_to.lower() == 'ft':
#             pass
#         elif c_to.lower() == 'km':
#             pass
#     elif c_from.lower() == 'ft':
#         if c_to.lower() == 'mi':
#             pass
#         elif c_to.lower() == 'km':
#             pass
#         elif c_to.lower() == 'm':
#             pass

# distance = int(input("What is the number you are trying to convert? "))
# convert_from = int(input("What unit are you converting from? "))
# convert_to = int(input("What unit are you converting from? "))
#
# convert_distance(distance, convert_from, convert_to)
unit_convert()
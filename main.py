
# unit converter introduction
print('Welcome to the unit converter!')

option = -1

while True:
    try:
        option = float(input('[1] Inches to Centimeters  [2] Yards to Meters   [0] Leave\n ->> '))

        # stop the code if the user press 0
        if option == 0:
            break
        
        # inches to centimeters
        if option == 1:
            inch = float(input('Type the inches: '))
            cm = inch * 2.54
            print(f'{inch:.2f} inches is equal to {cm:.2f}cm')

        # yards to meters
        if option == 2:
            yard = float(input('Type the yards: '))
            m = yard / 1.094
            print(f'{yard:.2f} yards is equal to {m:.2f}m')
        
    except ValueError:
        print('That is not an option, try again.')

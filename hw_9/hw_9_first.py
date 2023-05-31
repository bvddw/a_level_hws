def entrance_floor_flat(flat, floor, amount):
    if not flat % (floor * amount):
        needed_floor = floor
    else:
        needed_floor = (flat % (floor * amount)) // amount if not (flat % (floor * amount)) % amount else (flat % (floor * amount)) // amount + 1
    # entrance: we need just flat // (floor * amount) and add 1 if have remainder when flat % (floor * amount)
    print(f'''
Entrance: {flat // (floor * amount) if not flat % (floor * amount) else flat // (floor * amount) + 1}
Floor: {needed_floor}''')


flat_number = int(input('Enter a flat number: '))
number_of_floor = int(input('Enter a number of floors: '))
flat_amount = int(input('Enter a number of flats on one floor: '))
entrance_floor_flat(flat_number, number_of_floor, flat_amount)
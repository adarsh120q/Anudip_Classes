def bill(load, units):
    total_units = 0
    if units>0 and units<51:
        total_units = units*4.75
    elif units>50 and units<101:
        total_units = units*5.75
    elif units>100 and units<201:
        total_units = units*7
    elif units>200:
        total_units= units*8

    return f"The fixed charges on your sanctioned load({load}KW) :₹{load*60} \nCharges on total units used({units}KWh): ₹{total_units} \nYour total Bill Amount is: ₹{(load*60)+total_units} "

load = int(input("Enter the sanctioned load (should be less than 10KW): "))
if load<0 and load>10:
    print("Invalid input")
else:
    units = int(input("Enter the total units used: "))
    print(bill(load,units))
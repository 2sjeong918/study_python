from Car import Car


my_car = Car(0xFFFFFF, 20, 3000)
my_car.print()
my_car.change_color(0xefefef)
my_car.print()

your_car = Car(0x0000FF, 10, 1500)
your_car.print()

her_car = Car()
her_car.print()

this_car = Car(displacement=5000)
this_car.print()

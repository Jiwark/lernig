weghte = float(input(" inter your weghte"))
height = float(input(" inter your height cm "))
height /= 100

bmi = weghte/height**2

if bmi < 18.5:
    print("under weghte")
elif 18.5 <= bmi < 25:
    print(" normal")
else:
    print(" over weghte")

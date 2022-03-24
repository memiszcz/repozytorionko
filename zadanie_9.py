masa=float(input("Podaj swoja mase: "))
wzrost=float(input("Podaj swoj wzrost (w metrach): "))

bmi=masa/wzrost**2

print ("Twoje BMI wynosi: ", bmi)

if bmi<20:
    print ("Masz niedowage.")
elif 20<bmi<25:
    print ("Prawidlowa waga.")
elif  25<bmi<30:
    print ("Masz nadwage.")
else:
    print ("Jestes otyly :/ .")

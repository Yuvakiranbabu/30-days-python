#°F = (°C × 9/5) + 32
temperature=input("type C for celsius or F for fahrenheit:")
temperature=temperature.upper()
if temperature=="C":
    celsius=int(input("enter your temperature: "))
    celsius_in_fahrenheit=(celsius*9/5)+32
    print("fahrenheit = ",celsius_in_fahrenheit)

if temperature=="F":
    fahrenheit=int(input("enter your temprature: "))
    print("fahrenheit = ",fahrenheit)

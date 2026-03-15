unit=input("Enter your electicity unit")
unit=int(unit)
bill=0
if unit>0:
    if unit>=1 and unit<=90:
        bill=unit*7
    elif unit>=91 and unit<=150:
        bill=(unit-90)*10 + (90*7)
    elif unit>=151 and unit<=300:
        bill=(unit-150)*18+ (60*10)+ (90*7)
    else: 
        unit>300
        bill=(unit-300)*18+ (150*18)+ (60*10)+ (90*7)
        bill=(bill+(bill*0.03))
    print(f"your unit is: {unit} \nyour electicity bill is: {bill}") 

else:
    print("invalid Unit")

print()
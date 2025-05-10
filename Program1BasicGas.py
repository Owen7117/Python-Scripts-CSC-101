#Owen O'Neil
#1/28/24
#Program 1 Basic: Gasoline



answer=float(input("How many gallons of gasoline?"))
print("{} gallon(s) of gasoline is equivalent to {:.3f} liters" .format(answer,answer*3.78541))
print("{} gallon(s) of gasoline requires {:.3f} barrels of oil" .format(answer,answer/19.5))
print("{} gallon(s) of gasoline produces {:.3f} pounds of Co2" .format(answer, answer*20))
print("{} gallon(s) of gasoline is energy equivalent to {:.2f} gallons of ethanol" .format(answer,answer*1.51915456))
print("{} gallon(s) of gasoline will cost you ${:.2f} at $2.90 per gallon" .format(answer,answer*2.90))
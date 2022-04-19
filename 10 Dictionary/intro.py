from turtle import st
from xml.dom.pulldom import START_ELEMENT


states_capital = {"Rajasthan":"japur","Hariana":"Chandigarh",19:20,"rajasthan":"raj"}
states_capital[19]="rj"
print(states_capital[19])
print(states_capital)
states_capital.pop(19)
print(states_capital)
print(states_capital.keys())
print(states_capital.values())
print(len(states_capital))

# looping in dictionaries......................
for i in states_capital.keys():
    print("in" ,i,"key, value is = ",states_capital[i])
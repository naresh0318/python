x = 50
def func(x):
    print("x is",x)
    x = 2
    print("changes local x to ",x)

func(x)
x=34
print("x is now",x)
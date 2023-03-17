# Local variable
def car():
    x = "volvo"
    print(x)


car()

# Global variables
y = "phone"

def device():
    global y
    print(y)

device()
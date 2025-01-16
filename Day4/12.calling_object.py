
class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name}"
    def __call__(self, *args, **kwds):
        print("Yes, I am here master")

    def call_me(self, *args, **kwds):
        print("Yes, I am here master")
    

rino = Cat("Rino")
print(rino)

value = 10

rino()
rino.call_me()


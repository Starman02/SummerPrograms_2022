from threading import Timer
print("hello")

def hello():
    print('ziinberg')



t = Timer(interval=5.0, function=hello)




t.start()

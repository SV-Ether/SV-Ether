import pickle
import functools

def createFile():
    sport = input('Enter Sport name: ')
    name = input('Enter Athelete: ')
    data = [sport, name]
    with open('sports.dat', 'ab') as file:
        pickle.dump(data, file)

def convert():
    data = []
    with open('sports.dat', 'rb') as file:
        while True:
            try: 
                dumped = pickle.load(file)
                data.append(dumped)
                if dumped is None:
                    break
            except:
                break
    dat = filter(lambda x: x[0].lower() == 'athletics', data)
    with open('athletics.dat', 'wb') as file:
        for i in dat:
            pickle.dump(i, file)
def display():
    data = []
    with open('athletics.dat', 'rb') as file:
        while True:
            try: 
                dumped = pickle.load(file)
                data.append(dumped)
                if dumped is None:
                    break
            except:
                break
    print(data)
ans = 'y'
while ans == 'y':
    createFile()
    ans = input('continue? (y/n)')

convert()
display()

import pickle
import functools

def createFile():
    act_no = input('Enter Emp Id.: ')
    acc_type = input('Enter Emp Salary: ')
    acc_name = input('Enter Emp name: ')
    acc_bal = input('Enter Emp mobile: ')
    data = [act_no, acc_type, acc_name, acc_bal ]
    with open('Account.dat', 'ab') as file:
        pickle.dump(data, file)

def balance(bal):
    data = []
    with open('emp.dat', 'rb') as file:
        while True:
            try: 
                dumped = pickle.load(file)
                data.append(dumped)
                if dumped is None:
                    break
            except:
                break
        print(data)
        s = sum(map(lambda x: int(x[1]), data))
        print(s)

createFile()
balance(0)

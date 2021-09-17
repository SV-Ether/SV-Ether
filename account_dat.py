import pickle

def createFile():
    act_no = input('Enter account No.: ')
    acc_type = input('Enter account type: ')
    acc_name = input('Enter account name: ')
    acc_bal = input('Enter account bal: ')
    data = { 'act_no': act_no, 'acc_type': acc_type, 'acc_name': acc_name, 'acc_bal': acc_bal }
    with open('Account.dat', 'ab') as file:
        pickle.dump(data, file)

def balance(bal):
    data = []
    with open('Account.dat', 'rb') as file:
        while True:
            try: 
                dumped = pickle.load(file)
                data.append(dumped)
                if dumped is None:
                    break
            except:
                break
        print(data)
        print('Accounts: ', ",\n".join(list(map(str, filter(lambda x: int(x['acc_bal']) > bal, data)))))
createFile()
balance(0)

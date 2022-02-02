import pickle

def createFile():
    act_no = input('Enter Phone No.: ')
    acc_name = input('Enter Phone name: ')
    data = [act_no, acc_name ]
    with open('pb.dat', 'ab') as file:
        pickle.dump(data, file)
        
createFile()

import pickle
import functools

def createFile():
    act_no = input('Enter Phone No.: ')
    acc_namee = input('Enter Phone name: ')
    data = [act_no, acc_name ]
    with open('pb.dat', 'ab') as file:
        pickle.dump(data, file)
        
createFile()

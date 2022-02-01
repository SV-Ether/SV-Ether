#WAP To create a stack list which contains tuples of names and age of vaccinated ppl 
# Check if stack is empty
# Add items to the stack
# Remove Item from stack who has duplicate
stack = []

def is_empty():
    return len(stack) == 0

def add_item(name, age):
    stack.append(tuple([name, age]))

def add_items():
    add_item('Essay', 18)
    add_item('Ben Dover', 17)
    add_item('Mike Hunt', 20)
    add_item('Essay', 19)

def remove_dupes():
    keys = {}
    for item in stack:
        if item[0] in keys.keys():
            print('Found Duplicate! ', item)
            stack.remove(item)
        keys[item[0]] = item[1]

add_items()
remove_dupes()
print(stack)
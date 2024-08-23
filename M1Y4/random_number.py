import random  

def randnum(max):
    result = ""
    num_list = []
    for i in range(1, max):
        num_list.append(i)
    result = random.choice(num_list)

    return result

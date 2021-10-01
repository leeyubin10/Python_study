import random

def lotto():
    ret_val = ''
    for i in range(6):
        random_number = random.randint(1,100)
        ret_val = ret_val + ' ' + str(random_number)
    return ret_val

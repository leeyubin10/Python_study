def bin2dec(bin_number):
    bin_str = str(bin_number)
    size = len(bin_str)
    sum = 0
    i = 0
    while size > 0:
        if(bin_str[i] == '1'):
            sum = sum + pow(2, size-1)
        size =  size - 1
        i = i + 1
    return sum
        

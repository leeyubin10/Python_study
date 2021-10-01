filename = input('파일명: ')

afile = open(filename, 'r')

lines = afile.readlines()

i=1

for line in lines:
    print(i, ':', line, end='')
    i = i + 1

afile.close()

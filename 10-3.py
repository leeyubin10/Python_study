filename = input('파일명: ')

aFile = open(filename, 'r')

lines = aFile.readlines()

i = 1

for line in lines:
    print(i, ':', line)
    i = i - 1

aFile.close()

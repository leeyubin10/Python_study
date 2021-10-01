filename = input('파일명:')

infile = open(filename, 'r')

s = infile.read()

print(str(len(s)) + "개의 문자")

print(str(len(s.split())) + "개의 단어")

print(str(len(s.split('\n'))) + "개의 줄")

infile.close()

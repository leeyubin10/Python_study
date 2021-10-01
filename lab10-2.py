infilename = input('입력 파일 이름:')
outfilename = input('출력 파일 이름:')

infile = open(infilename, 'r')
outfile = open(outfilename, 'w')

s = infile.read()

outfile.write(s)

infile.close()
outfile.close()

import random

turns=10
guesses=''

inflie = open('words.txt', 'r')
lines = inflie.readlines()
word = random.choice(lines)

while turns > 0:
    remaining=0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_',end='')
            remaining += 1
    if remaining == 0:
        print('사용자 승리')
        break
    print('')
    
    guess = input('단어를 추측하시오: ')
    guesses += guess
    if guess not in word:
        turns-=1
        print('틀렸음!')
        print(str(turns)+'기회가 남았음!')
        if turns==0:
            print('사용자 패배 정답은' + word)

infile.close()

import random
answer = random.randint(1,100)
while True:
    guess = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    if guess == answer:
        print("정답!")
        break
    elif guess > answer:
        print("너무 커요")
    else:
        print("너무 작아요")
        

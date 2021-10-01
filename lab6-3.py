items = {"커피":7,"볼펜":3,"종이컵":2, "우유":1, "콜라":4, "책":5}

while True:
    answer = ""
    item = input("물건의 이름을 입력하세요: ")
    if item in items:
        print("재고 보기는 1, 증가는 2, 감소는 3, 종료는 q")
        answer =  input("")
        if answer == '1':
            print(item,"재고:", items[item])
        elif answer == '2':
            items[item] = items[item]+1
        elif answer == '3':
            items[item] = items[item]-1
        elif answer == "q":
            quit()
        
        
    else:
        print(item,"는 없습니다.")

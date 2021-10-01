contacts = {}

while True:
    name=input("(입력모드)이름을 입력하세요: ")
    if not name:
        break;
    tel = input("전화번호를 입력하세요:")
    contacts[name] = tel

while True:
    name = input("(검색모드)이름을 입력하세요: ")
    if not name:
        break;
    if name in contacts:
        print(name,"의 전화번호는",contacts[name], "입니다")
    else:
        print(name, "은 없습니다.")

        

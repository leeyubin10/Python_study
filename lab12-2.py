class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "가 야옹합니다.")

    def drink(self):
        print(self.name, "가 우유를 마셔요.")
        print(self.name, "가 낮잠을 잡니다.")

cloe = Cat("클로이")
rocky = Cat("로키")

cloe.speak()
cloe.drink()

rocky.speak()
rocky.drink()

class human:

    age = 0
    height = 0
    weight = 0

    def __init__(self, age = 0, height = 0, weight = 0):
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return human(str(self.age) + "," + str(self.height) + "," + str(self.weight)
    def __add__(self, other: human) -> human:
        return human(self.age + other.age, self.height + other.height, self.weight + other.weight )
    def __sub__(self, other):
        return human(self.age - other.age, self.height - other.height, self.weight - other.weight)
    def __mul__(self, other:human)-> int:
        return human(self.age * other.age + self.height * other.height + self.weight * other.weight )
    def __truediv__(self, other: human)-> str:
        return "Bu islem tanimsiz"



from human import human
human_1 = human(24, 175, 72)
human_2 = human(27, 177, 75)
print(human_1)

human_1 = human()
human_2 = human(26,166,67)

result = human_1 + human_2
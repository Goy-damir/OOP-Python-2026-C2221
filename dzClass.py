import time
class Student:
    def __init__(self, name, age, money, knowledge, energy, happiness):
        self.name = name
        self.age = age
        self.money = money
        self.knowledge = knowledge
        self.energy = energy
        self.happiness = happiness

    def Life(self):

        print("ви - звичайний студент на ім'я ", (self.name), "ваші параметри:")
        print("ваш вік - ", (self.age))
        print("ваш банківський рахунок- ", (self.money), " $")
        print("ваші знання- ", (self.knowledge))
        print("ваша енергія - ", (self.energy))
        print("рівень вашого щастя - ", (self.happiness))
        print("день вашого шалопая цe 48 ділянок по пів години" \
        "ваша задача - протягом дня встигати спати, вчитися, гратися й працювати, аби підтримувати всі показники в нормі")

        print("ви маєте вчасно вписувати всі команди:")
        print("work -  дає гроші")
        print("study -  дає знання")
        print("sleep -  дає енергію")
        print("love -  дає щастя")
        print(f"""{self.money} {self.knowledge} {self.energy} {self.happiness}""")
        print("якщо готові, то напишіть yes")
        day = 0


        if input() == str("yes"):
            while True:
                print(f"\n--- День {day + 1} ---")
                time_spent = 0

                while time_spent < 48:
                    command = input(">>> ")
                    if command == "work":
                        self.money += 100
                        time_spent += 5
                        print("ваш статок = ", (self.money))
                        self.energy -= 20
                        print("лишилося часу на сьогодні", (48 - time_spent))

                    elif command == "sleep":
                        self.energy += 10
                        time_spent += 18
                        print("ви поспали, ваша енергія = ", (self.energy))
                        self.knowledge -= 1
                        print("лишилося часу на сьогодні", (48 - time_spent))

                    elif command == "study":
                        self.knowledge += 2
                        time_spent += 18
                        print("ваші знання = ", (self.knowledge))
                        self.happiness -= 15
                        print("лишилося часу на сьогодні", (48 - time_spent))

                    elif command == "love":
                        self.happiness += 10
                        time_spent += 4
                        print("ваш рівень щастя = ", (self.happiness))
                        self.money -= 100
                        print("лишилося часу на сьогодні", (48 - time_spent))
                
                if self.money < 200:
                    print("у вас закінчилися гроші. вас вигнали з гуртожитку, ви бомж. на вулиці вас з'їв інший голодний студент")
                    return
                elif self.knowledge < 40:
                    print("ви завалили курсову. вас виперли з шараги, ви тепер таджикський дворнік за фахом. вас спіймали і з'їли скінхеди")
                    return
                elif self.energy < 60:
                    print("ви вигоріли і кинули навчанн. ви лох")
                    return
                elif self.happiness < 50:
                    print("ви стали нещасним, вас кинула дівчина, ви засумували і умєрлі")
                    return

                else:
                    print("день закінчено! ви вижили")
                    day += 1
                    print("ви прожили", (day), "днів")
            
nm = str(input("і як тебе звати, шалопай? калісь -"))
std = Student(nm, 19, 200, 60, 90, 80)
std.Life()
import random

print ("Вы попали в генератор яоя")
while True:
    a = input ("Если вы хотите выбрать случайного прогера, введите слово Случайный. Если вы хотите выбрать конкретного прогера, введите слово Конкретный ")
    if a == "Случайный":
        list = ["Роберт Фрипп", "Билл Бруфорд", "Роджер Уотерс", "Дэвид Гилмор", "Джон Уэттон", "Мэл Коллинз", "Питер Гэбриел", "Эдди Джобсон", "Кит Эмерсон",
            "Карл Палмер", "Грег Лэйк", "Брайан Ино", "Брайан Ферри", "Энди Маккей", "Фил Манзанера", "Пол Томпсон", "Рик Кентон", "Фил Коллинз", "Тони Бэнкс", "Майк Разерфорд",
            "Стив Хаккетт", "Эдриан Бэлью", "Тони Левин", "Кристиан Вандер", "Питер Барденс", "Эндрю Латимер", "Энди Уорд", "Ричард Синклэр", "Пай Гастингс", "Берлинчик"]
        print(random.choice(list))
        list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
        print(random.choice(list))
        list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Роберта Фриппа", "Билла Бруфорда", "Дэвида Гилмора",
            "Кита Эмерсона", "Карла Палмера", "Грега Лэйка", "Брайана Ино", "Брайана Ферри", "Энди Маккея", "Фила Манзанеры", "Пола Томпсона", "Рика Кентона", "Фила Коллинза", "Тони Бэнкса",
            "Майка Разерфорда", "Стива Хаккетта", "Эдриана Бэлью", "Тони Левина", "Кристиана Вандера", "Берлинчика", "Питера Барденса", "Эндрю Латимера", "Энди Уорда", "Ричарда Синклэра", "Пая Гастингса"]
        print(random.choice(list))
    elif a == "Конкретный":
        b = input ("Введите имя прогера ")
        if b == "Роберт Фрипп":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Ксеша":
            print (b)
            list = ["Трахнула в жопу", "Отстрапонила", "Выебала в очко", "Размозжила череп", "Облизнула два сосочка", "Откусила соски", "Засунула бутылку в жопу"]
            (random.choice(list))
            if (random.choice(list)) == "Размозжила череп":
                print ("Размозжила череп")
                print ("Стивену Уилсону")
            else:
                list = ["Трахнула в жопу", "Отстрапонила", "Выебала в очко"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
        elif b == "Джон Уэттон":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Билл Бруфорд":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Роджер Уотерс":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Дэвида Гилмора"]
            print(random.choice(list))
        elif b == "Дэвид Гилмор":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Мэл Коллинз":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
                "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Питер Гэбриел":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Эдди Джобсон":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Кит Эмерсон":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Карл Палмер":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Грег Лэйк":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Брайан Ино":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Брайан Ферри":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
                "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у" ]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Брайана Ино"]
            print(random.choice(list))
        elif b == "Энди Маккей":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Фил Манзанера":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Пол Томпсон":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Рик Кентон":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Фил Коллинз":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Тони Бэнкс":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Майк Разерфорд":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Стив Хаккетт":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Эдриан Бэлью":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Тони Левин":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Кристиан Вандер":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Питер Барденс":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Эндрю Латимер":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Энди Уорд":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Ричард Синклэр":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Пай Гастингс":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
            print(random.choice(list))
        elif b == "Берлинчик":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Билла Бруфорда", "Аллана Холдсуорта"]
            print(random.choice(list))
        elif b == "Аллан Холдсуорт":
            print (b)
            list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Билла Бруфорда", "Берлинчика", "Аллана Холдсуорта"]
            print(random.choice(list))
        elif b == "Аннетт":
            print (b)
            list = ["Трахнула в жопу", "Отстрапонила", "Выебала в очко"]
            print(random.choice(list))
            list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Билла Бруфорда", "Берлинчика", "Аллана Холдсуорта", "Ксешу"]
            print(random.choice(list))
        else:
            print ("Такого прогера нет в базе")
            b = input ("Введите имя прогера ")
            if b == "Роберт Фрипп":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Джон Уэттон":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Билл Бруфорд":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Роджер Уотерс":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Дэвид Гилмор":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Мэл Коллинз":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Питер Гэбриел":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Эдди Джобсон":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Кит Эмерсон":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Карл Палмер":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Грег Лэйк":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Брайан Ино":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Брайан Ферри":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Энди Маккей":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Фил Манзанера":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Пол Томпсон":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Рик Кентон":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Фил Коллинз":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Тони Бэнкс":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Майк Разерфорд":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Стив Хаккетт":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Эдриан Бэлью":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Тони Левин":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Кристиан Вандер":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Питер Барденс":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Эндрю Латимер":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Энди Уорд":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Ричард Синклэр":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Пай Хастингс":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона"]
                print(random.choice(list))
            elif b == "Берлинчик":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Билла Бруфорда", "Аллана Холдсуорта"]
                print(random.choice(list))
            elif b == "Аллан Холдсуорт":
                print (b)
                list = ["Трахнул в жопу", "Отстрапонил", "Выебал в очко", "Кончил на лицо", "Обосрался во время анала на", "Сожрал головку члена", "Засунул бутылку в жопу",
            "Зондировал струной от гитары член", "Откусил сосок", "Облизнул два сосочка", "Занюхался волосами в жопе у"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Билла Бруфорда", "Берлинчика", "Аллана Холдсуорта"]
                print(random.choice(list))
            elif b == "Аннетт":
                print (b)
                list = ["Трахнула в жопу", "Отстрапонила", "Выебала в очко"]
                print(random.choice(list))
                list = ["Джона Уэттона", "Мэла Коллинза", "Питера Гэбриела", "Роджера Уотерса", "Эдди Джобсона", "Билла Бруфорда", "Берлинчика", "Аллана Холдсуорта", "Ксешу"]
                print(random.choice(list))
    else:
        print ("Такого варианта нет")


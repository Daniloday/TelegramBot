class Lesson():
    def __init__(self, name, week, day, time, zoom):
        self.name = name
        self.week = week # 0 - second, 1 - first , 2 - whatever
        self.day = day
        self.time = time
        self.zoom = zoom

def create_schedule():
    schedule = (
        Lesson( name = 'СРОМ 2 (практика) | Черный Олег', week = 0, day = '1', time = "8:20", zoom = "https://us04web.zoom.us/j/2625120734?pwd=K0QrcXN4ekcrbDZKRW15Z1NVUSs3UT09"), 
        Lesson( name = 'Теор.вер (лекция) | Дор А.А', week = 3, day = '1', time = "10:15", zoom = "https://us02web.zoom.us/j/82324302808?pwd=M2x0emhVdldBV2F4MnhqWjRCWHBRQT09"), 
        Lesson( name = 'Мат.мод (лекция) | Смирнов С.А', week = 3, day = '1', time = "12:10", zoom = "https://meet.google.com/lookup/asny3chck7?authuser=1&hs=179"), 
        Lesson( name = 'English | Синекоп', week = 3, day = '1', time = "14:05", zoom = "https://us04web.zoom.us/j/9822532040?pwd=c21vVFBxbDcyNldYYmxBK3c0ckZXdz09"),

        Lesson( name = 'Методы оптимизаций (лекция) | Дед Данилов В.Я', week = 3, day = '2', time = "10:15", zoom = "https://us04web.zoom.us/j/73389991708?pwd=aDZ2YmNqRG9rb2dQdW4zcWdERDhVZz09"), 
        Lesson( name = 'Мат.мод (лабы) | Кириенко О.В', week = 3, day = '2', time = "14:05", zoom = "Наверное не придет"),

        Lesson( name = 'Теория сложности (практика) | Фес Андрей', week = 0, day = '3', time = "8:20", zoom = "https://us04web.zoom.us/j/3033669459?pwd=N0ovVUV3dTQ4N2xmaDBpTTdCQ3BBUT09"), 
        Lesson( name = 'Методы оптимизаций (практика) | Дед Данилов В.Я', week = 3, day = '3', time = "10:15", zoom = "https://us04web.zoom.us/j/77043249383?pwd=ZkN5amE3RFFPT3IyalZENTQ3QVl2dz09"), 
        Lesson( name = 'QAQC (лекция) | Ткач В.М', week = 1, day = '3', time = "12:10", zoom = "https://bth.zoom.us/j/62733592448"), 
        Lesson( name = 'Мат.прога | Хмельницкий', week = 3, day = '3', time = "14:05", zoom = "Пару я дал, а ссылку я не дам \n В группе мат.прога (там даже ссылки на группу нет)"),

        Lesson( name = 'Теория сложности (лекция) | Фес Андрей', week = 3, day = '4', time = "8:20", zoom = "https://us04web.zoom.us/j/3033669459?pwd=N0ovVUV3dTQ4N2xmaDBpTTdCQ3BBUT09"), 
        Lesson( name = 'Теор.вер (практика) | Нищенко И.И', week = 3, day = '4', time = "10:15", zoom = "https://meet.google.com/vpz-fcaf-wtt"), 
        Lesson( name = 'СРОМ 1 (лекция) | Завадская Л.О.', week = 3, day = '4', time = "12:10", zoom = "https://us04web.zoom.us/j/3908947683?pwd=UWhmb1B0NDZSU3dZc3ZVL0RaSUJqdz09"), 

        Lesson( name = 'СРОМ 1 (лабы) | Пекарчук Нина', week = 0, day = '5', time = "8:20", zoom = "https://us04web.zoom.us/j/8397990765?pwd=dUMzWk1hSWx2RWtrTTRHalNObXhWUT09 но это не точно"), 
        Lesson( name = 'СРОМ 2 (ОАОАОАААО) (лекция) | Сенсей', week = 3, day = '5', time = "10:15", zoom = "https://us04web.zoom.us/j/71468510955?pwd=N3NuVm9vMThUVzluSTlCdXF0YW5mUT09"), 
        Lesson( name = 'СРОМ 1 (практика) | Завадская Л.О.', week = 0, day = '5', time = "12:10", zoom = "https://us04web.zoom.us/j/3908947683?pwd=UWhmb1B0NDZSU3dZc3ZVL0RaSUJqdz09"), 
        )
    return schedule
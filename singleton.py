# Реализация паттерна Singleton (Одиночка) в Python
# Учебное задание


class Singleton:
    """Класс-одиночка: можно создать только один его экземпляр."""

    _instance = None  # здесь хранится единственный экземпляр класса

    def __new__(cls):
        # __new__ вызывается каждый раз при создании объекта: Singleton()
        # если экземпляр ещё не создан - создаём его
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        # если уже создан - возвращаем старый, новый объект не создаётся
        return cls._instance

    def __init__(self):
        # __init__ запускается при КАЖДОМ вызове Singleton(),
        # поэтому проверяем: если атрибуты уже есть, не создаём их заново
        if not hasattr(self, "name"):
            self.name = "Единственный экземпляр"
            self.counter = 0

    @classmethod
    def getInstance(cls):
        # глобальная точка доступа: всегда возвращает один и тот же объект
        if cls._instance is None:
            cls._instance = Singleton()
        return cls._instance

    def printInfo(self):
        # выводим информацию об экземпляре
        print("Имя:", self.name)
        print("id объекта в памяти:", id(self))
        print("Счётчик:", self.counter)


if __name__ == "__main__":
    # получаем экземпляр несколько раз через getInstance()
    first = Singleton.getInstance()
    second = Singleton.getInstance()
    third = Singleton.getInstance()

    # проверяем, что все переменные указывают на один и тот же объект
    print("first is second:", first is second)
    print("second is third:", second is third)
    print("id первого:", id(first))
    print("id второго:", id(second))
    print("id третьего:", id(third))
    print()

    # меняем данные через одну переменную -
    # у остальных они тоже меняются, потому что объект один
    first.counter = first.counter + 5
    first.printInfo()
    print()

    # даже прямой вызов Singleton() не создаст новый объект
    direct = Singleton()
    print("direct is first:", direct is first)
    direct.printInfo()

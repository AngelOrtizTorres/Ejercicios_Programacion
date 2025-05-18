class Menu:

    def __init__(self, *options, title="Menú de opciones"):
        self.__options = list(options)
        self.__title = title

    @property
    def last_option(self):
        return len(self.__options)

    def choose(self):
        self.__print_menu()
        return self.__chosen_option()

    def __print_menu(self):
        print(self.__title)
        print("-" * len(self.__title))
        for n in range(len(self.__options)):
            print(f"{n + 1}. {self.__options[n]}")

    def __chosen_option(self):
        while True:
            option = int(input(f"\nIntroduce una opción (1 - {len(self.__options)}): "))
            if 1 <= option <= len(self.__options):
                return option
            print("Has introducido una opción incorrecta.")

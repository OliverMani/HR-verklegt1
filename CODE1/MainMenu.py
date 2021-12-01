

class Main_menu:
    def __init__(self) -> None:
        self.menu = """
        (P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn \t <(T)il baka>   <(Q) Hætta>
        -----------------------------------------------------------------------------------------"""
    def render(self):
        print(self.menu)

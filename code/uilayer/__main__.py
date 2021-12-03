class ExampleScreen:
    def __init__(self):
        self.parts = [[TextComponent('texti'), TextComponent('annar texti')], [SpaceComponent(3), TextComponent('hello world')], []]

    def render(self):
        for line in self.parts:
            for part in line:
                print(part, end='')
            print()

"""Skjár:
textiannar texti
   hello world





"""

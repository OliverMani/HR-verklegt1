class UIMenuScreen:
    '''displays UI menu screen'''
    def __init__(self):
        self.options = """
    Main Menu

1 for employees
2 for destinations
3 for bla
"""

    def render(self):
        print(self.options)
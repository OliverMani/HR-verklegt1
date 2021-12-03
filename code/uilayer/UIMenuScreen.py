from uilayer.UIScreen import UIScreen

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
        UIScreen.render_header()
        print("\nPrófíll\n")
        print(self.options)
        UIScreen.render_footer()
        return input("Slá inn aðgerð: ")

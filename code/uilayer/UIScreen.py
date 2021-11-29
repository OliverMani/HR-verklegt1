class UIScreen:
    '''displays UI screen'''
    def __init__(self, components):
        self.components = components
    
    def render_header():
        header = "  (P)rófíll    (V)erkefni    (F)asteignir    (S)tarfsmenn "
        print(header,"\n","_"*len(header))
    
    def render_footer():
        footer = "<(T)il baka>                                  <(Q) Hætta>"
        print(footer,"\n","_"*len(footer))





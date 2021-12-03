class TextComponent:
    """Þetta er basically texti, þannig að þegar
    forritið býr til tilvik (instance) af klasanum
    og eina sem það skilar er textinn"""
    def __init__(self, text):
        self.text = text

    """Skilar textanum fyrir print"""
    def __str__(self):
        return self.text

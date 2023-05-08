class Alligner:

    def __init__(self):
        pass

    def format(self, txt: str, width=80, filler='-', align='c'):
        assert align in 'lcr'
        return {'l': txt.ljust, 'c': txt.center, 'r': txt.rjust}[align](width, filler)
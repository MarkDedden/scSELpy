class Verbose(object):
    def __init__(self):
        self._verbosity = 2


    @property
    def verbosity(self):
        return self._verbosity

    @verbosity.setter
    def verbosity(self, value):
        if value in range(6) :
            self._verbosity = value
        else:
            raise AttributeError("Please specify an integer between 0 and 5.")
    


settings = Verbose()


"""
class verbose:
    def __init__(self,value):
        self.verbosity_value = value
    def set_value(self,new_value):
        self.verbosity_value = new_value
    def get_value(self):
        return(self.verbosity_value)
    
verbosity = verbose(2)

def set_verbosity(value,verbosity_init_class = verbosity):
    verbosity.set_value(value)
    
def get_verbosity(verbosity_init_class = verbosity):
    return(verbosity.get_value())
"""


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

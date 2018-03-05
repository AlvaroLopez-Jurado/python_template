class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def concat_strings(string1, string2):
        if (type(string1) is not str or type(string2) is not str):
            raise TypeError("Solo concatena strings")
        if(string1.isdigit() or string2.isdigit()):
            raise TypeError("Solo concatena strings")
        if(len(string1) >10 or len(string2)>10):
            raise TypeError("El tamano maximo de un string es 10")
            
        return string1+string2

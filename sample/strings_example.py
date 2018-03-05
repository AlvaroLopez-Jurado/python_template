class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def concat_strings(string1, string2):
        if (type(string1) is not str or type(string2) is not str):
            raise TypeError
        if(string1.isdigit() or string2.isdigit()):
            raise TypeError

        return string1+string2

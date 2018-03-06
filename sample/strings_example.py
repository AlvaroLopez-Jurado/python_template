class StringsExamples(object):
    """A class to play with the strings"""

    @staticmethod
    def concat_strings(strings):

        if(len(strings)<2 or len(strings)>10 ):
            raise TypeError("Maximo numero de strings 10 y minimo 2")

        for x in range(len(strings)):
            if(type(strings[x]) is not str):
                raise TypeError("Solo concatena strings")
            if(strings[x].isdigit()):
                raise TypeError("Solo concatena strings")
            if(len(strings[x])>10):
                raise TypeError("El tamano maximo de un string es 10")

        finalString = ""
        for x in range(len(strings)):
            finalString += strings[x]

        return finalString

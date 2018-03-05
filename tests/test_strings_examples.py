import unittest
from sample.strings_example import StringsExamples


class TestStringsExamples(unittest.TestCase):
    def test_concat_strings(self):
        string1 = "hola"
        string2 = "adios"
        result = StringsExamples.concat_strings(string1, string2)
        assert result == "holaadios"

    def test_concat_number_string(self):
        string1 = 123
        string2 = "adios"
        resutl = self.assertRaises(Exception ,StringsExamples.concat_strings(string1,string2))

    def test_concat_string_number(self):
        string1 = 123
        string2 = "adios"
        resutl = self.assertRaises(Exception ,StringsExamples.concat_strings(string1,string2))



if __name__ == '__main__':
    unittest.main()

import unittest
from sample.strings_example import StringsExamples


class TestStringsExamples(unittest.TestCase):
    def test_concat_strings(self):
        string1 = "hola"
        string2 = "adios"
        result = StringsExamples.concat_strings(string1, string2)
        assert result == "holaadios"

    def test_concat_numbers(self):
        string1 = 123
        string2 = 123
        self.assertRaises(TypeError, StringsExamples.concat_strings,string1,string2)

    def test_concat_number_string(self):
        string1 = 123
        string2 = "adios"
        self.assertRaises(TypeError ,StringsExamples.concat_strings,string1,string2)

    def test_concat_string_number(self):
        string1 = "adios"
        string2 = 123
        self.assertRaises(TypeError ,StringsExamples.concat_strings,string1,string2)

    def test_concat_numbers2(self):
        string1 = "123"
        string2 = "123"
        self.assertRaises(TypeError, StringsExamples.concat_strings,string1,string2)

    def test_concat_number_string2(self):
        string1 = "123"
        string2 = "adios"
        self.assertRaises(TypeError ,StringsExamples.concat_strings,string1,string2)

    def test_concat_string_number2(self):
        string1 = "adios"
        string2 = "123"
        self.assertRaises(TypeError ,StringsExamples.concat_strings,string1,string2)

    def test_concant_bigstring1(self):
        string1 = "MasDe10Caracteres"
        string2 = "adios"
        self.assertRaises(TypeError, StringsExamples.concat_strings,string1,string2)

    def test_concant_bigstring2(self):
        string1 = "MasDe10Caracteres"
        string2 = "adios"
        self.assertRaises(TypeError, StringsExamples.concat_strings,string1,string2)

    def test_concant_bigstring_both(self):
        string1 = "MasDe10Caracteres"
        string2 = "MasDe10Caracteres"
        self.assertRaises(TypeError, StringsExamples.concat_strings,string1,string2)


if __name__ == '__main__':
    unittest.main()

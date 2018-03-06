import unittest
from sample.strings_example import StringsExamples


class TestStringsExamples(unittest.TestCase):
    def test_concat_2strings(self):
        strings = []
        strings.append("hola")
        strings.append("adios")
        result = StringsExamples.concat_strings(strings)
        assert result == "holaadios"

    def test_concat_3strings(self):
        strings = []
        strings.append("hola")
        strings.append("adios")
        strings.append("hola")
        result = StringsExamples.concat_strings(strings)
        assert result == "holaadioshola"

    def test_concat_4strings(self):
        strings = []
        strings.append("hola")
        strings.append("adios")
        strings.append("hola")
        strings.append("adios")
        result = StringsExamples.concat_strings(strings)
        assert result == "holaadiosholaadios"

    def test_concat_5strings(self):
        strings = []
        strings.append("hola")
        strings.append("adios")
        strings.append("hola")
        strings.append("adios")
        strings.append("hola")
        result = StringsExamples.concat_strings(strings)
        assert result == "holaadiosholaadioshola"

    def test_concat_2numbers(self):
        strings = []
        strings.append(123)
        strings.append(456)
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_3numbers(self):
        strings = []
        strings.append(123)
        strings.append(456)
        strings.append(789)
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_4numbers(self):
        strings = []
        strings.append(123)
        strings.append(456)
        strings.append(789)
        strings.append(123)
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_number_string(self):
        strings = []
        strings.append(123)
        strings.append("adios")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_string_number(self):
        strings = []
        strings.append("adios")
        strings.append(123)
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_2numbers_string(self):
        strings = []
        strings.append(123)
        strings.append("adios")
        strings.append(123)
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_number_2strings(self):
        strings = []
        strings.append("adios")
        strings.append(123)
        strings.append("adios")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_numbers_v2(self):
        strings = []
        strings.append("123")
        strings.append("123")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_number_string2_v2(self):
        strings = []
        strings.append("123")
        strings.append("adios")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_string_number_v2(self):
        strings = []
        strings.append("adios")
        strings.append("123")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_2numbers_string_v2(self):
        strings = []
        strings.append("123")
        strings.append("adios")
        strings.append("123")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concat_number_2strings_v2(self):
        strings = []
        strings.append("adios")
        strings.append("123")
        strings.append("adios")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concant_bigstring1(self):
        strings = []
        strings.append("MasDe10Caracteres")
        strings.append("adios")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concant_bigstring2(self):
        strings = []
        strings.append("adios")
        strings.append("MasDe10Caracteres")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concant_bigstring_both(self):
        strings = []
        strings.append("MasDe10Caracteres")
        strings.append("MasDe10Caracteres")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_one_string(self):
        strings = []
        strings.append("hola")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_concant_more_than_10_strings(self):
        strings = []
        for x in range(15):
            strings.append("hola")
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)

    def test_null_string(self):
        strings = []
        self.assertRaises(TypeError, StringsExamples.concat_strings,strings)


if __name__ == '__main__':
    unittest.main()

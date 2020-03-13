import unittest
from Program_for_Testing import Testing

class TestStringMethods(unittest.TestCase):

    def test_Number_2855(self):
        Dictionary = Testing(2855)
        banknotes = list(Dictionary.keys())
        print(Dictionary)
        result = 0
        for notes in banknotes:
            result += notes * Dictionary[notes]
        self.assertEqual(result, 2855)

    def test_Number_35(self):
        Dictionary = Testing(35)
        banknotes = list(Dictionary.keys())
        print(Dictionary)
        result = 0
        for notes in banknotes:
            result += notes * Dictionary[notes]
        self.assertEqual(result, 35)

    def test_Number_12780(self):
        Dictionary = Testing(12780)
        banknotes = list(Dictionary.keys())
        print(Dictionary)
        result = 0
        for notes in banknotes:
            result += notes * Dictionary[notes]
        self.assertEqual(result, 12780)

    def test_Wrong_Value(self):
        Dictionary = Testing(47)
        banknotes = list(Dictionary.keys())
        print(Dictionary)
        result = 0
        for notes in banknotes:
            result += notes * Dictionary[notes]
        self.assertEqual(result, 0)

    def test_Wrong_Result(self):
        Dictionary = Testing(55)
        banknotes = list(Dictionary.keys())
        print(Dictionary)
        result = 0
        for notes in banknotes:
            result += notes * Dictionary[notes]
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()
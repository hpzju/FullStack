import unittest
from unittestDemo import adder, adder10, Pet


class unittestDemoTester(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(adder(1, 5), 6)
        self.assertNotEqual(adder(10, 10), 10)

    def test_adder10(self):
        self.assertEqual(adder10(5), 15)
        self.assertEqual(adder10(5), adder(5, 10))
        self.assertNotEqual(adder10(20), 15)

    def test_Pet(self):
        cat = Pet("cat")
        dog = Pet("dog")
        self.assertEqual(cat.name, "cat")
        self.assertNotEqual(dog.name, "cat")
        self.assertEqual(Pet.counts(), 2)


if __name__ == "__main__":
    print(f"Run {__file__} : ")
    unittest.main()

import unittest
from unittest_demo import adder, adder10, Pet


class TestunittestDemo(unittest.TestCase):
    def test_adder(self):
        """testing adder()"""
        self.assertEqual(adder(1, 5), 6)
        self.assertNotEqual(adder(10, 10), 10)

    def test_adder10(self):
        """testing adder10()"""
        self.assertEqual(adder10(5), 15)
        self.assertEqual(adder10(5), adder(5, 10))
        self.assertNotEqual(adder10(20), 15)

    def test_Pet(self):
        """testing Pet Class"""
        cat = Pet("cat")
        dog = Pet("dog")
        self.assertEqual(cat.name, "cat")
        self.assertEqual(dog.name, "dog")
        dog.name = "DDDDog"
        self.assertEqual(dog.name, "DDDDog")
        self.assertEqual(Pet.counts(), 2)


if __name__ == "__main__":
    print(f"Run {__file__} : ")
    unittest.main()

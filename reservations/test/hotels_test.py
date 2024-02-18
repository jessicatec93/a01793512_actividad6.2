"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

CRUD unit tests of operations in the hotel entity
"""

import json
import random
import unittest

from faker import Faker

from reservations.hotels import Hotels


class TestCalculate(unittest.TestCase):
    """
        Class that applies unit tests on the hotel entity
    """

    def setUp(self):
        """
            Variable initialization function
        """
        self.path_file = "./reservations/database/hotels.txt"
        self.hotels = {}
        self.status_ok = {"status": "ok"}
        with open(self.path_file, 'r', encoding="utf-8") as file:
            self.hotels = json.load(file)
        self.hotel = Hotels()
        self.fake = Faker()

    def test_add_method_returns_correct_result(self):
        """
            Unit test on creating a record in the correct hotel entity
        """
        init = 50
        end = 500
        body = {
            'name': self.fake.name(),
            'address': self.fake.address(),
            'rooms': random.randint(init, end)
        }
        self.assertEqual(self.status_ok, self.hotel.create(body))

    def test_add_method_returns_incorrect_result(self):
        """
            Incorrect unit test when sending wrong payload when creating a hotel record
        """
        self.assertRaises(TypeError, self.hotel.create, {})

    def test_update_method_returns_correct_result(self):
        """
            Unit test on updating a record in the correct hotel entity
        """
        if   len(self.hotels) > 0:
            index = random.choice(list(self.hotels.keys()))
            init = 50
            end = 500
            body = {
                'name': self.fake.name(),
                'address': self.fake.address(),
                'rooms': random.randint(init, end)
            }
            self.assertEqual(self.status_ok, self.hotel.update(index, body))

    def test_update_method_returns_not_found(self):
        """
            Unit test updating a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.hotel.update, index, {})

    def test_update_method_returns_incorrect_result(self):
        """
            Incorrect unit test when sending wrong payload when updating a hotel record
        """
        if  len(self.hotels) > 0:
            index = random.choice(list(self.hotels.keys()))
            self.assertRaises(TypeError, self.hotel.update, index, {})

    def test_get_by_id_method_returns_correct_result(self):
        """
            Unit test on getting a record in the correct hotel entity
        """
        if  len(self.hotels) > 0:
            index = random.choice(list(self.hotels.keys()))
            response = self.hotels[str(index)]
            self.assertEqual(response, self.hotel.get(index))

    def test_get_by_id_method_returns_not_found(self):
        """
            Unit test getting a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.hotel.get, index)

    def test_delete_by_id_method_returns_correct_result(self):
        """
            Unit test on deleting a record in the correct hotel entity
        """
        if  len(self.hotels) > 0:
            index = random.choice(list(self.hotels.keys()))
            self.assertEqual(self.status_ok, self.hotel.delete(index))

    def test_delete_by_id_method_returns_not_found(self):
        """
            Unit test deleting a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.hotel.delete, index)

if __name__ == '__main__':
    unittest.main()

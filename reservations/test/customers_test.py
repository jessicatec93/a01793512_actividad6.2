"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

CRUD unit tests of operations in the customer entity
"""

import json
import random
import unittest

from faker import Faker

from reservations.customers import Customer


class Testcustomers(unittest.TestCase):
    """
        Class that applies unit tests on the customer entity
    """

    def setUp(self):
        """
            Variable initialization function
        """
        self.path_file = "./reservations/database/customers.txt"
        self.customers = {}
        self.status_ok = {"status": "ok"}
        with open(self.path_file, 'r', encoding="utf-8") as file:
            self.customers = json.load(file)
        self.customer = Customer()
        self.fake = Faker()

    def test_add_method_returns_correct_result(self):
        """
            Unit test on creating a record in the correct customer entity
        """
        init = 18
        end = 70
        body = {
            'name': self.fake.name(),
            'address': self.fake.address(),
            'age': random.randint(init, end)
        }
        self.assertEqual(self.status_ok, self.customer.create(body))

    def test_add_method_returns_incorrect_result(self):
        """
            Incorrect unit test when sending wrong payload
        """
        self.assertRaises(TypeError, self.customer.create, {})

    def test_update_method_returns_correct_result(self):
        """
            Unit test on updating a record in the correct customer entity
        """
        if len(self.customers) > 0:
            index = random.choice(list(self.customers.keys()))
            init = 18
            end = 70
            body = {
                'name': self.fake.name(),
                'address': self.fake.address(),
                'age': random.randint(init, end)
            }
            self.assertEqual(self.status_ok, self.customer.update(index, body))

    def test_update_method_returns_not_found(self):
        """
            Unit test updating a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.customer.update, index, {})

    def test_update_method_returns_incorrect_result(self):
        """
            Incorrect unit test when sending wrong payload
        """
        if len(self.customers) > 0:
            index = random.choice(list(self.customers.keys()))
            self.assertRaises(TypeError, self.customer.update, index, {})

    def test_get_by_id_method_returns_correct_result(self):
        """
            Unit test on getting a record in the correct customer entity
        """
        if len(self.customers) > 0:
            index = random.choice(list(self.customers.keys()))
            response = self.customers[str(index)]
            self.assertEqual(response, self.customer.get(index))

    def test_get_by_id_method_returns_not_found(self):
        """
            Unit test getting a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.customer.get, index)

    def test_delete_by_id_method_returns_correct_result(self):
        """
            Unit test on deleting a record in the correct customer entity
        """
        if len(self.customers) > 0:
            index = random.choice(list(self.customers.keys()))
            self.assertEqual(self.status_ok, self.customer.delete(index))

    def test_delete_by_id_method_returns_not_found(self):
        """
            Unit test deleting a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.customer.delete, index)


if __name__ == '__main__':
    unittest.main()

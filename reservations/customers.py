"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

CRUD operations on the customer entity
"""

import json


class Customer():
    """
    Class that carries out operations on the customer entity.
    """

    def __init__(self) -> None:
        self.path_file = "reservations/database/customers.txt"
        self.customers = {}
        self.response_ok = {"status": "ok"}
        with open(self.path_file, 'r', encoding="utf-8") as file:
            self.customers = json.load(file)

    def __del__(self):
        with open(self.path_file, 'w', encoding="utf-8") as file:
            json.dump(self.customers, file)

    def create(self, data):
        """
            Creation of a new record in the customer entity
        """
        try:
            index = str(len(self.customers) + 1)
            customer = {
                'name': data["name"],
                'address': data["address"],
                'age': data["age"],
            }
            self.customers[index] = customer
            return self.response_ok
        except Exception as e:
            raise TypeError("The payload is incorrect") from e

    def update(self, index, data):
        """
            Updating an existing record in the customer entity
        """
        try:
            index = str(index)
            if index not in self.customers:
                raise TypeError(f"The customer with id was not found: {index}")
            customer = {
                'name': data["name"],
                'address': data["address"],
                'age': data["age"],
            }
            self.customers[index] = customer
            return self.response_ok
        except Exception as e:
            raise TypeError("The payload is incorrect") from e

    def get(self, index):
        """
            Viewing an existing record in the customer entity
        """
        try:
            index = str(index)
            if index not in self.customers:
                raise TypeError(f"The customer with id was not found: {index}")
            return self.customers[index]
        except Exception as e:
            raise TypeError(
                f"I found an error when getting the customer with Id {index}"
            ) from e

    def delete(self, index):
        """
            Deletion of an existing record in the customer entity
        """
        try:
            index = str(index)
            if index not in self.customers:
                raise TypeError(f"The customer with id was not found: {index}")
            self.customers.pop(index, None)
            return self.response_ok
        except Exception as e:
            raise TypeError(
                f"I found an error when deleting the customer with Id {index}"
            ) from e


if __name__ == '__main__':
    calc = Customer()

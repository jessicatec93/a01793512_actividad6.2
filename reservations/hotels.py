"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

CRUD operations on the hotel entity
"""

import json


class Hotels():
    """
    Class that carries out operations on the hotel entity.
    """

    def __init__(self) -> None:
        self.path_file = "reservations/database/hotels.txt"
        self.hotels = {}
        self.response_ok = {"status": "ok"}
        with open(self.path_file, 'r', encoding="utf-8") as file:
            self.hotels = json.load(file)

    def __del__(self):
        with open(self.path_file, 'w', encoding="utf-8") as file:
            json.dump(self.hotels, file)

    def create(self, data):
        """
            Creation of a new record in the hotel entity
        """
        try:
            index = str(len(self.hotels) + 1)
            hotel = {
                'name': data["name"],
                'address': data["address"],
                'rooms': data["rooms"],
            }
            self.hotels[index] = hotel
            return self.response_ok
        except Exception as e:
            raise TypeError("The payload is incorrect") from e

    def update(self, index, data):
        """
            Updating an existing record in the hotel entity
        """
        try:
            index = str(index)
            if index not in self.hotels:
                raise TypeError(f"The hotel with id was not found: {index}")
            hotel = {
                'name': data["name"],
                'address': data["address"],
                'rooms': data["rooms"],
            }
            self.hotels[index] = hotel
            return self.response_ok
        except Exception as e:
            raise TypeError("The payload is incorrect") from e

    def get(self, index):
        """
            Viewing an existing record in the hotel entity
        """
        try:
            index = str(index)
            if index not in self.hotels:
                raise TypeError(f"The hotel with id was not found: {index}")
            return self.hotels[index]
        except Exception as e:
            raise TypeError(
                f"I found an error when getting the hotel with Id {index}"
            ) from e

    def delete(self, index):
        """
            Deletion of an existing record in the hotel entity
        """
        try:
            index = str(index)
            if index not in self.hotels:
                raise TypeError(f"The hotel with id was not found: {index}")
            self.hotels.pop(index, None)
            return self.response_ok
        except Exception as e:
            raise TypeError(
                f"I found an error when deleting the hotel with Id {index}"
            ) from e


if __name__ == '__main__':
    calc = Hotels()

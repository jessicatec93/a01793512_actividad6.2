"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

Reservation creation
"""

from datetime import datetime
import json


class Reservation():
    """
    Class that is responsible for managing hotel reservations.
    """

    def __init__(self) -> None:
        self.hotel_path_file = "reservations/database/hotels.txt"
        self.costumer_path_file = "./reservations/database/customers.txt"
        self.reservation_path_file = "reservations/database/reservations.txt"
        self.hotels = {}
        self.customers = {}
        self.reservations = {}
        self.response_ok = {"status": "ok"}
        with open(self.hotel_path_file, 'r', encoding="utf-8") as file:
            self.hotels = json.load(file)
        with open(self.costumer_path_file, 'r', encoding="utf-8") as file:
            self.customers = json.load(file)
        with open(self.reservation_path_file, 'r', encoding="utf-8") as file:
            self.reservations = json.load(file)

    def __del__(self):
        with open(self.reservation_path_file, 'w', encoding="utf-8") as file:
            json.dump(self.reservations, file)

    def create(self, data):
        """
            Creation of a new record in the reservation entity
        """
        try:
            costumer_id = str(data["costumer_id"])
            hotel_id = str(data["hotel_id"])
            reservation_date = data["reservation_date"].date()
            date = datetime.now().date()
            if reservation_date < date:
                raise TypeError("Invalid reservation date")
            if hotel_id not in self.hotels:
                raise TypeError(f"The hotel with id was not found: {hotel_id}")
            if costumer_id not in self.customers:
                raise TypeError(
                    f"The customer with id was not found: {costumer_id}"
                )
            index = str(len(self.reservations) + 1)
            reservation = {
                'date': datetime.now().strftime("%d/%m/%Y"),
                'costumer_id': costumer_id,
                'hotel_id': hotel_id,
                'enabled': True,
                'reservation_date': reservation_date.strftime("%d/%m/%Y")
            }
            self.reservations[index] = reservation
            return self.response_ok
        except Exception as e:
            raise TypeError("The payload is incorrect") from e

    def cancel(self, index):
        """
            Canceling reservation
        """
        try:
            index = str(index)
            if index not in self.reservations:
                raise TypeError(
                    f"The reservation with id was not found: {index}"
                )
            self.reservations[index]['enabled'] = False
            return self.response_ok
        except Exception as e:
            raise TypeError(
                "An error occurred while trying to cancel the reservation"
            ) from e


if __name__ == '__main__':
    calc = Reservation()

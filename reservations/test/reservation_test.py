"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

Management of hotel reservations
"""

import json
import random
import unittest

from datetime import datetime
from faker import Faker

from reservations.reservation import Reservation


class TestReservation(unittest.TestCase):
    """
        Class that applies unit tests on the reservation entity
    """

    def setUp(self):
        """
            Variable initialization function
        """
        self.path = "./reservations/database/"
        self.hotels = {}
        self.customers = {}
        self.reservations = {}
        self.status_ok = {"status": "ok"}
        with open(self.path + "hotels.txt", 'r', encoding="utf-8") as file:
            self.hotels = json.load(file)
        with open(self.path + "customers.txt", 'r', encoding="utf-8") as file:
            self.customers = json.load(file)
        with open(
            self.path + "reservations.txt", 'r', encoding="utf-8"
        ) as file:
            self.reservations = json.load(file)
        self.reservation = Reservation()
        self.fake = Faker()

    def test_add_method_returns_correct_result(self):
        """
            Unit test on creating a record in the correct reservation entity
        """
        if len(self.customers) > 0 and len(self.hotels) > 0:
            costumer_id = random.choice(list(self.customers.keys()))
            hotel_id = random.choice(list(self.hotels.keys()))
            date = datetime.now()
            final_date = datetime.strptime('31/12/2030', '%d/%m/%Y')
            body = {
                'costumer_id': costumer_id,
                'hotel_id': hotel_id,
                'reservation_date': self.fake.date_time_between_dates(
                    datetime_start=date, datetime_end=final_date
                )
            }
            self.assertEqual(self.status_ok, self.reservation.create(body))

    def test_add_method_returns_incorrect_result(self):
        """
            Incorrect unit test when sending wrong payload
        """
        self.assertRaises(TypeError, self.reservation.create, {})

    def test_add_method_returns_incorrect_customer(self):
        """
            Incorrect unit test when sending wrong curtomer id
        """
        if len(self.hotels) > 0:
            costumer_id = 4653456
            hotel_id = random.choice(list(self.hotels.keys()))
            date = datetime.now()
            final_date = datetime.strptime('31/12/2030', '%d/%m/%Y')
            body = {
                'costumer_id': costumer_id,
                'hotel_id': hotel_id,
                'reservation_date': self.fake.date_time_between_dates(
                    datetime_start=date, datetime_end=final_date
                )
            }
            self.assertRaises(TypeError, self.reservation.create, body)

    def test_add_method_returns_incorrect_hotel(self):
        """
            Incorrect unit test when sending wrong hotel id
        """
        if len(self.customers) > 0:
            costumer_id = random.choice(list(self.customers.keys()))
            hotel_id = 34567
            date = datetime.now()
            final_date = datetime.strptime('31/12/2030', '%d/%m/%Y')
            body = {
                'costumer_id': costumer_id,
                'hotel_id': hotel_id,
                'reservation_date': self.fake.date_time_between_dates(
                    datetime_start=date, datetime_end=final_date
                )
            }
            self.assertRaises(TypeError, self.reservation.create, body)

    def test_add_method_returns_incorrect_reservation_date(self):
        """
            Incorrect unit test when sending wrong reservation date
        """
        if len(self.customers) > 0 and len(self.hotels) > 0:
            costumer_id = random.choice(list(self.customers.keys()))
            hotel_id = random.choice(list(self.hotels.keys()))
            body = {
                'costumer_id': costumer_id,
                'hotel_id': hotel_id,
                'reservation_date': datetime.strptime('31/12/2000', '%d/%m/%Y')
            }
            self.assertRaises(TypeError, self.reservation.create, body)

    def test_delete_by_id_method_returns_correct_result(self):
        """
            Unit test on canceling a record in the correct reservation entity
        """
        if len(self.reservations) > 0:
            index = random.choice(list(self.reservations.keys()))
            self.assertEqual(self.status_ok, self.reservation.cancel(index))

    def test_cancel_by_id_method_returns_not_found(self):
        """
            Unit test canceling a record that doesn't exist
        """
        index = 702545
        self.assertRaises(TypeError, self.reservation.cancel, index)


if __name__ == '__main__':
    unittest.main()

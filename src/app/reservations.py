import datetime
import system
from booking_factory import BookingFactory


class Reservation:
    __bookingFactory = BookingFactory()

    def calculate_cost(self, reservation_period, room_cost, dining_option_cost, payment_method_discount):
        return (reservation_period * room_cost + dining_option_cost) * payment_method_discount

    def check_date_format(self, date_string, date_format):
        while True:
            try:
                datetime.datetime.strptime(date_string, date_format)
                print("This is the correct date format.")
            except ValueError:
                date_string = input("This is the incorrect date format. It should be YYYY-MM-DD: ")
                continue
            else:
                break
        return datetime.datetime.strptime(date_string, date_format), date_string

    def choose_start_date(self, date_format):
        first_day = input("Enter first day of your reservation 'RRRR-MM-DD': ")
        first_day_obj, first_day = self.check_date_format(first_day, date_format)
        while True:
            if first_day_obj < datetime.datetime.now():
                first_day = input("The reservation may start at the earliest today 'RRRR-MM-DD': ")
                first_day_obj, first_day = self.check_date_format(first_day, date_format)
            else:
                break
        return first_day_obj

    def choose_end_date(self, date_format, first_day_obj):
        last_day = input("Enter the last day of your reservation 'RRRR-MM-DD': ")
        last_day_obj, last_day = self.check_date_format(last_day, date_format)
        while True:
            if last_day_obj < first_day_obj:
                last_day = input("Reservation can not end before the first day 'RRRR-MM-DD': ")
                last_day_obj, last_day = self.check_date_format(last_day, date_format)
            else:
                break
        return last_day_obj

    def choose_room(self, hotel_id):
        self.__bookingFactory.get_booking_info("Hotel").list_all_rooms(hotel_id)
        #room_id = int(input("Enter the room number from a list above you want to book: "))
        room_id = system.System.check_if_correct_value(self,'room', 'int')
        rooms = self.__bookingFactory.get_booking_info("Database").get_all_rooms(hotel_id)
        room_cost = 0
        searching = True
        while searching:
            for room in rooms:
                if room['room_ID'] == room_id:
                    searching = False
                    room_cost = room['room_type_price']
                    break
            if searching:
                self.__bookingFactory.get_booking_info("Hotel").list_all_rooms(hotel_id)
                #room_id = int(input("Enter the proper room number from a list above you want to book: "))
                room_id = system.System.check_if_correct_value(self, 'room', 'int')
        return room_id, room_cost

    def choose_dining_option(self):
        self.__bookingFactory.get_booking_info("Hotel").list_dining_options()
        #dining_option_id = int(input("Enter dining option number from a list above: "))
        dining_option_id = system.System.check_if_correct_value(self,'dining option', 'int')

        dining_options = self.__bookingFactory.get_booking_info("Database").get_dining_options()
        dining_option_cost = 0
        searching = True
        while searching:
            for dining_option in dining_options:
                if dining_option['dining_option_ID'] == dining_option_id:
                    searching = False
                    dining_option_cost = dining_option['dining_option_cost']
                    break
            if searching:
                self.__bookingFactory.get_booking_info("Hotel").list_dining_options()
                #dining_option_id = int(input("Enter proper dining option number from a list above: "))
                dining_option_id = system.System.check_if_correct_value(self, 'dining option', 'int')
        return dining_option_id, dining_option_cost

    def choose_payment_method(self):
        self.__bookingFactory.get_booking_info("Hotel").list_payment_methods()
        payment_method_id = int(input("Enter payment method number from a list above: "))
        #payment_method_id = system.System.check_if_correct_value(self,'payment method', 'int')
        payment_methods = self.__bookingFactory.get_booking_info("Database").get_payment_methods()
        payment_method_discount = 0
        searching = True
        while searching:
            for payment_method in payment_methods:
                if payment_method['payment_method_ID'] == payment_method_id:
                    searching = False
                    payment_method_discount = payment_method['payment_method_discount']
                    break
            if searching:
                self.__bookingFactory.get_booking_info("Hotel").list_payment_methods()
                payment_method_id = int(input("Enter proper payment method number from a list above: "))
                #payment_method_id = system.System.check_if_correct_value(self,'payment method','int')
        return payment_method_id, payment_method_discount

    def choose_reservation(self, user_id, action_name):
        self.list_my_reservations_info(user_id)
        #reservation_id = int(input(f"Enter the reservation number from a list above, you want to {action_name}: "))
        reservations = self.__bookingFactory.get_booking_info("Database").get_my_reservations_info(user_id)
        reservation_obj = None
        if (len(reservations) == 0):
            print("You don't have any reservations")

        else:
            reservation_id =  system.System.check_if_correct_value(self,'reservation', 'int')
            searching = True
            while searching:
                for reservation in reservations:
                    if reservation['reservation_ID'] == reservation_id:
                        reservation_obj = self.__bookingFactory.get_booking_info("Database").get_my_reservation(reservation_id)
                        searching = False
                        break
                if searching:
                    self.list_my_reservations_info(user_id)
                    #reservation_id = int(
                     #   input(f"Enter the proper reservation number from a list above, you want to {action_name}: "))
                    reservation_id = system.System.check_if_correct_value(self, 'reservation', 'int')
        return reservation_obj

    def list_all_reservations(self):
        reservation_list = self.__bookingFactory.get_booking_info("Database").get_all_reservations_info()
        for reservation in reservation_list:
            print(f"Reservation number: {reservation['reservation_ID']}\n"
                  f"\tClient: {reservation['user_name']} {reservation['user_surname']}\n"
                  f"\tHotel: {reservation['hotel_name']}\n"
                  f"\tDate: {reservation['first_day']} - {reservation['last_day']}\n"
                  f"\tRoom: {reservation['room_ID']} {reservation['room_type']}\n"
                  f"\tDining option: {reservation['dining_option_type']}\n"
                  f"\tPayment: {reservation['payment_method']} - {reservation['cost']} PLN")

    def list_my_reservations_info(self, user_id):
        reservation_list = self.__bookingFactory.get_booking_info("Database").get_my_reservations_info(user_id)
        for reservation in reservation_list:
            print(f"Reservation number: {reservation['reservation_ID']}\n"
                  f"\tClient: {reservation['user_name']} {reservation['user_surname']}\n"
                  f"\tHotel: {reservation['hotel_name']}\n"
                  f"\tDate: {reservation['first_day']} - {reservation['last_day']}\n"
                  f"\tRoom: {reservation['room_ID']} {reservation['room_type']}\n"
                  f"\tDining option: {reservation['dining_option_type']}\n"
                  f"\tPayment: {reservation['payment_method']} - {reservation['cost']} PLN")
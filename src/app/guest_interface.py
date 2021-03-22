from booking_factory import BookingFactory


class GuestInterface():
    __bookingFactory = BookingFactory()

    def GI_list_hotels(self):
        self.__bookingFactory.get_booking_info("Hotel").list_hotels()

    def GI_hotel_info(self):
        self.__bookingFactory.get_booking_info("Hotel").hotel_info()

    def GI_list_my_reservations_info(self, user_id):
        self.__bookingFactory.get_booking_info("Reservation").list_my_reservations_info(user_id)

    def GI_choose_hotel(self):
        return self.__bookingFactory.get_booking_info("Hotel").choose_hotel()

    def GI_choose_start_date(self, date_format):
        return self.__bookingFactory.get_booking_info("Reservation").choose_start_date(date_format)

    def GI_choose_end_date(self, date_format, first_day_obj):
        return self.__bookingFactory.get_booking_info("Reservation").choose_end_date(date_format, first_day_obj)

    def GI_choose_room(self, hotel_id):
        return self.__bookingFactory.get_booking_info("Reservation").choose_room(hotel_id)

    def GI_choose_dining_option(self):
        return self.__bookingFactory.get_booking_info("Reservation").choose_dining_option()

    def GI_choose_payment_method(self):
        return self.__bookingFactory.get_booking_info("Reservation").choose_payment_method()

    def GI_calculate_cost(self, reservation_period, room_cost, dining_option_cost, payment_method_discount):
        return self.__bookingFactory.get_booking_info("Reservation").calculate_cost(reservation_period,
                                                                 room_cost, dining_option_cost, payment_method_discount)

    def GI_choose_reservation(self, user_id, action_name):
        return self.__bookingFactory.get_booking_info("Reservation").choose_reservation(user_id, action_name)

    def GI_add_reservation(self, user_id, hotel_id, first_day_obj, last_day_obj, room_id, dining_option_id, payment_method_id, reservation_cost):
        self.__bookingFactory.get_booking_info("Database").add_reservation(user_id, hotel_id, first_day_obj, last_day_obj, room_id, dining_option_id,
                                      payment_method_id, reservation_cost)

    def GI_update_my_reservation(self, hotel_id, first_day, last_day, room_id, dining_option_id, payment_method_id, cost, reservation_id):
        self.__bookingFactory.get_booking_info("Database").update_my_reservation(hotel_id, first_day, last_day, room_id, dining_option_id,
                                              payment_method_id, cost, reservation_id)

    def GI_delete_reservation(self, reservation_id):
        self.__bookingFactory.get_booking_info("Database").delete_reservation(reservation_id)

    def GI_delete_all_my_reservation(self, user_id):
        self.__bookingFactory.get_booking_info("Database").delete_all_my_reservation(user_id)
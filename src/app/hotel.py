from booking_factory import BookingFactory


class Hotel:
    __bookingFactory = BookingFactory()

    def list_hotels(self):
        print("List of all available hotels:")
        for hotel in self.__bookingFactory.get_booking_info("Database").get_all_hotels():
            print(
                f"\t{hotel['country_ID']} {hotel['location_city']} Hotel number: {hotel['hotel_ID']} Hotel name: {hotel['hotel_name']} ")

    def list_hotel_room_types(self, hotel_id):
        room_types = self.__bookingFactory.get_booking_info("Database").get_hotel_room_types(hotel_id)
        print("\tTypes of rooms available in this hotel:")
        for room_type in room_types:
            print(
                f"\t - {room_type['room_type_ID']} '{room_type['room_type']}' - cost of a night: {room_type['room_type_price']}")

    def list_room_types(self):
        room_types = self.__bookingFactory.get_booking_info("Database").get_room_types()
        print("\tAvailable types of rooms in offer:")
        for room_type in room_types:
            print(
                f"\t - {room_type['room_type_ID']} '{room_type['room_type']}' - cost of a night: {room_type['room_type_price']}")

    def list_all_rooms(self, hotel_id):
        rooms = self.__bookingFactory.get_booking_info("Database").get_all_rooms(hotel_id)
        print("\tList of rooms available in this hotel: ")
        for room in rooms:
            print(
                f"\t - Room number: {room['room_ID']} '{room['room_type']}' - cost of a night: {room['room_type_price']}")

    def list_dining_options(self):
        dining_options = self.__bookingFactory.get_booking_info("Database").get_dining_options()
        print("\tDining options available in this hotel:")
        for dining_option in dining_options:
            print(
                f"\t - {dining_option['dining_option_ID']} {dining_option['dining_option_type']} - cost of service: {dining_option['dining_option_cost']}")

    def list_payment_methods(self):
        payment_methods = self.__bookingFactory.get_booking_info("Database").get_payment_methods()
        print("\tPayment options available in this hotel:")
        for payment_method in payment_methods:
            discount = round((1 - payment_method['payment_method_discount']) * 100)
            print(
                f"\t - {payment_method['payment_method_ID']} {payment_method['payment_method']} - amount of discount: {discount}%")

    def hotel_info(self):
        hotel_id = self.choose_hotel()
        print("Here is more information about the hotel you chose:")
        hotel = self.__bookingFactory.get_booking_info("Database").get_hotel_address(hotel_id)
        print(f"\tHotel number: {hotel[0]['hotel_ID']}")
        print(f"\tName: {hotel[0]['hotel_name']}")
        print(f"\tCountry: {hotel[0]['country_name']}")
        print(f"\tCity: {hotel[0]['location_city']}")
        print(f"\tAddress: {hotel[0]['street_address']}")
        self.list_hotel_room_types(hotel_id)
        self.list_dining_options()
        self.list_payment_methods()

    def choose_hotel(self):
        self.list_hotels()
        hotel_id = int(input("Enter the number of hotel from list above: "))
        #hotel_id = system.System.check_if_correct_value(self, 'hotel', 'int')

        hotels = self.__bookingFactory.get_booking_info("Database").get_all_hotels()
        searching = True
        while searching:
            for hotel in hotels:
                if hotel['hotel_ID'] == hotel_id:
                    searching = False
                    break
            if searching:
                self.list_hotels()
                hotel_id = int(input("Enter the proper hotel number from list above: "))
                #hotel_id = system.System.check_if_correct_value(self, 'hotel', 'int')
        return hotel_id

    def cost_statistics(self):
        costs = self.__bookingFactory.get_booking_info("Database").get_min_max_avg_cost()
        print("Reservation costs statistics:")
        print(f" - Lowest booking value: {costs[0]['minimum']} PLN")
        print(f" - Average booking value: {costs[0]['average']} PLN")
        print(f" - Highest booking value: {costs[0]['maximum']} PLN")

    def list_hotels_by_popularity(self):
        print("List of hotels by number of reservations:")
        hotels = self.__bookingFactory.get_booking_info("Database").get_hotels_popularity()
        for hotel in hotels:
            if hotel['bookings'] == 1:
                print(f"Hotel: {hotel['hotel_name']} in {hotel['location_city']} has {hotel['bookings']} booking.")
            else:
                print(f"Hotel: {hotel['hotel_name']} in {hotel['location_city']} has {hotel['bookings']} bookings.")

    def list_room_types_by_popularity(self):
        print("List of room types by number of bookings:")
        room_types = self.__bookingFactory.get_booking_info("Database").get_room_types_popularity()
        for room_type in room_types:
            if room_type['bookings'] == 1:
                print(f"The '{room_type['room_type']}' type was chosen {room_type['bookings']} time.")
            else:
                print(f"The '{room_type['room_type']}' type was chosen {room_type['bookings']} times.")

    def list_dining_options_by_popularity(self):
        print("List of dining options by number of orders:")
        dining_options = self.__bookingFactory.get_booking_info("Database").get_dining_options_popularity()
        for dining_option in dining_options:
            if dining_option['orders'] == 1:
                print(f"The '{dining_option['dining_option_type']}' option was chosen {dining_option['orders']} time.")
            else:
                print(f"The '{dining_option['dining_option_type']}' option was chosen {dining_option['orders']} times.")

    def list_payment_methods_by_popularity(self):
        print("List of payment methods by number of orders:")
        payment_methods = self.__bookingFactory.get_booking_info("Database").get_payment_methods_popularity()
        for payment_method in payment_methods:
            if payment_method['orders'] == 1:
                print(f"The '{payment_method['payment_method']}' method was chosen {payment_method['orders']} time.")
            else:
                print(f"The '{payment_method['payment_method']}' method was chosen {payment_method['orders']} times.")
import system
from booking_factory import BookingFactory


class Worker:
    __bookingFactory = BookingFactory()

    def worker_menu(self, user_id):
        user_input = input(system.WORKER_MENU)
        while True:
            if user_input == 'hotels':
                self.__bookingFactory.get_booking_info("Hotel").list_hotels()
            elif user_input == 'list res':
                self.__bookingFactory.get_booking_info("Reservation").list_all_reservations()
            elif user_input == 'stat':
                self.statistic_menu()
            elif user_input == 'moderate':
                self.moderate_menu()
            elif user_input == 'log out':
                system.System().menu()
            else:
                print("Unknown command! try again.")

            user_input = input(system.WORKER_MENU)

    def statistic_menu(self):
        user_input = input(system.STATISTICS_MENU)
        while user_input != 'back':
            if user_input == 'booking price':
                self.__bookingFactory.get_booking_info("Hotel").cost_statistics()
            elif user_input == 'pop hotels':
                self.__bookingFactory.get_booking_info("Hotel").list_hotels_by_popularity()
            elif user_input == 'pop rooms':
                self.__bookingFactory.get_booking_info("Hotel").list_room_types_by_popularity()
            elif user_input == 'pop dining':
                self.__bookingFactory.get_booking_info("Hotel").list_dining_options_by_popularity()
            elif user_input == 'pop payment':
                self.__bookingFactory.get_booking_info("Hotel").list_payment_methods_by_popularity()
            elif user_input == 'best clients':
                self.list_clients_with_multiple_reservations()
            else:
                print("Unknown command! Try again.")

            user_input = input(system.STATISTICS_MENU)

    def list_clients_with_multiple_reservations(self):
        print("List of clients with multiple reservations:")
        clients = self.__bookingFactory.get_booking_info("Database").get_clients_with_multiple_reservations()
        for client in clients:
            print(f"{client['user_name']} {client['user_surname']} has {client['reservations']} reservations.")

    def adding_hotel_process(self):
        hotel_name = input("Enter the name of the new hotel: ")
        country_id = input("Enter the country code 'PL': ")
        country_name = input("Enter country name: ")
        location_city = input("Enter the name of the city in which the hotel is located: ")
        street_address = input("Enter hotel address: ")
        decision = input(system.ADD_HOTEL_DECISION_INTERFACE)
        if decision == 'yes':
            self.__bookingFactory.get_booking_info("Database").add_country(country_id, country_name)
            self.__bookingFactory.get_booking_info("Database").add_location(location_city, street_address, country_id)
            location_id = self.__bookingFactory.get_booking_info("Database").get_latest_location_id()
            self.__bookingFactory.get_booking_info("Database").add_hotel(hotel_name, location_id[0]['location_id'])
            print("New hotel has been added to the offer.")
        elif decision == 'no':
            pass
        else:
            print("Unknown command! Try again.")

    def adding_room_process(self):
        hotel_id = self.__bookingFactory.get_booking_info("Hotel").choose_hotel()
        self.__bookingFactory.get_booking_info("Hotel").list_room_types()
        room_type_id = int(input("Enter the number of room type you want to create: "))
        decision = input(system.ADD_ROOM_DECISION_INTERFACE)
        if decision == 'yes':
            self.__bookingFactory.get_booking_info("Database").add_room(hotel_id, room_type_id)
            print("New room has been added to the offer.")
        elif decision == 'no':
            pass
        else:
            print("Unknown command! Try again.")

    def deleting_hotel_process(self):
        hotel_id = self.__bookingFactory.get_booking_info("Hotel").choose_hotel()
        decision = input(system.DELETE_HOTEL_DECISION_INTERFACE)
        if decision == 'yes':
            self.__bookingFactory.get_booking_info("Database").delete_hotel(hotel_id)
            print("Hotel has been removed from the offer.")
        elif decision == 'no':
            pass
        else:
            print("Unknown command! Try again.")

    def deleting_room_process(self):
        hotel_id = self.__bookingFactory.get_booking_info("Hotel").choose_hotel()
        room_id, room_cost = self.__bookingFactory.get_booking_info("Reservation").choose_room(hotel_id)
        print(room_id)
        decision = input(system.DELETE_ROOM_DECISION_INTERFACE)
        if decision == 'yes':
            self.__bookingFactory.get_booking_info("Database").delete_room(room_id)
            print("Room has been removed from the offer.")
        elif decision == 'no':
            pass
        else:
            print("Unknown command! Try again.")

    def changing_cost_process(self):
        user_input = input(system.CHANGE_COSTS_MENU)
        while user_input != 'back':
            if user_input == 'room cost':
                self.__bookingFactory.get_booking_info("Hotel").list_room_types()
                room_type_id = int(input("Enter the number of room type you want to change cost: "))
                room_type_price = int(input("Enter a new price for this room type: "))
                self.__bookingFactory.get_booking_info("Database").change_room_type_cost(room_type_id, room_type_price)
                print("This room type cost has been changed.")
            elif user_input == 'dining cost':
                self.__bookingFactory.get_booking_info("Hotel").list_dining_options()
                dining_option_id = int(input("Enter the number of dining option you want to change cost: "))
                dining_option_cost = int(input("Enter a new price for this room dining option: "))
                self.__bookingFactory.get_booking_info("Database").change_dining_option_cost(dining_option_id, dining_option_cost)
                print("This dining option cost has been changed.")
            else:
                print("Unknown command! Try again.")

            user_input = input(system.CHANGE_COSTS_MENU)

    def moderate_menu(self):
        user_input = input(system.MODERATE_MENU)
        while user_input != 'back':
            if user_input == 'add hotel':
                self.adding_hotel_process()
            elif user_input == 'add room':
                self.adding_room_process()
            elif user_input == 'del hotel':
                self.deleting_hotel_process()
            elif user_input == 'del room':
                self.deleting_room_process()
            elif user_input == 'change costs':
                self.changing_cost_process()
            else:
                print("Unknown command! Try again.")

            user_input = input(system.MODERATE_MENU)

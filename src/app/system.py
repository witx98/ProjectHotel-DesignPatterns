import sys
from booking_factory import BookingFactory


class System:
    __bookingFactory = BookingFactory()

    def menu(self):
        user_input = input(START_MENU_INTERFACE)
        user_id = 0
        user_type = 0
        if user_input == 'log':
            user_id, user_type = self.log_in()
        elif user_input == 'reg':
            self.register_user()
            self.menu()
        elif user_input == 'exit':
            self.__bookingFactory.get_booking_info("Database").close_database()
            sys.exit(0)
        else:
            print("Unknown command! Please try again.")

        if user_id != 0:
            if user_type == 0:
                print("Logged in as a client!")
                self.__bookingFactory.get_booking_info("Guest").client_menu(user_id)
            else:
                print("Logged in as a administrator!")
                self.__bookingFactory.get_booking_info("Worker").worker_menu(user_id)
        else:
            self.menu()

    def log_in(self):
        login = input("Enter your nickname: ")
        password = input("Enter your password: ")
        user_id = 0
        user_type = 0
        for user in self.__bookingFactory.get_booking_info("Database").get_log_info():
            if login == user['user_login'] and password == user['user_password']:
                user_id = user['user_ID']
                user_type = user['user_type']

        if user_id != 0:
            print("Login was successful")
            return user_id, user_type
        else:
            print("Error, login failed")
            return user_id, user_type

    def check_if_correct_number(self, name, length):
        while True:
            user_input = input(f"Enter your {name}: ")
            if len(user_input) != length:
                print(f"Wrong length of {name}: {len(user_input)}, should be {length}. Try again!")
                continue
            try:
                n = int(user_input)
            except ValueError:
                print("Entered value is not a number. Try again!")
                continue
            else:
                break
        return user_input

    def check_if_correct_value(self, name, type):
        if type == 'int':
            while True:
                user_input = input(f"Enter the proper {name} number from a list above: ")
                try:
                    n = int(user_input)
                except ValueError:
                    print("Entered value is not a number. Try again!")
                    continue
                else:
                    break
        return n

    def register_user(self):
        user_name = input("Enter your name: ")
        user_surname = input("Enter your surname: ")
        user_email = input("Enter your email 'user@email.com': ")
        user_telephone = self.check_if_correct_number("phone number", 9)
        user_PESEL = self.check_if_correct_number("PESEL", 11)
        user_login = input("Enter your user name: ")
        user_password = input("Enter your password: ")
        user_type = 0

        self.__bookingFactory.get_booking_info("Database").add_user(user_name, user_surname, user_email, user_telephone, user_PESEL, user_login, user_password,
                          user_type)


DECISION_INTERFACE = """
You have reached to the end of reservation form. 

Please decide what you want to do:
- 'cancel' to discard the reservation. 
- 'save' to finalize the reservation. 
YOUR CHOICE: """

CLIENT_PICK_TO_EDIT_RESERVATION_MENU = """
You are in reservation editing menu. 

Please decide what you want to do:
- 'pick' to choose specific reservation to change.
- 'back' to back to the previous menu.
YOUR CHOICE: """

CLIENT_EDIT_RESERVATION_MENU = """

Please decide what you want to change:
- 'hotel' to change hotel.
- 'date' to change starting and ending date.
- 'room' to change room.
- 'dining' to change dining options.
- 'payment' to change payment method.
- 'save' to save changes.
- 'cancel' to cancel changes.
YOUR CHOICE:  """

EDIT_DECISION_INTERFACE = """

Are you sure you want to save the changes:
- 'yes' 
- 'no' 
YOUR CHOICE: """

CLIENT_PICK_TO_DELETE_RESERVATION_MENU = """
You are in reservation deleting menu. 

Please decide what you want to do:
- 'pick' to choose specific reservation to delete.
- 'delete all' to delete all your reservations.
- 'back' to back to the previous menu.
YOUR CHOICE: """

DELETE_DECISION_INTERFACE = """

Are you sure you want to delete:
- 'yes' 
- 'no' 
YOUR CHOICE: """

STATISTICS_MENU = """
You are in statistics menu. 

Please decide what you want to see:
- 'booking price' to see minimum, maximum and average price of booking.
- 'pop hotels' to see hotels by popularity.
- 'pop rooms' to see room types by popularity.
- 'pop dining' to see dining options by popularity.
- 'pop payment' to see payment methods by popularity.
- 'best clients' to see client that have more than one reservation' 
- 'back' to back to the previous menu.
YOUR CHOICE: """

START_MENU_INTERFACE = """
Hello and welcome to Hotel Application. 

Please decide and type what you want to do:
- 'log' to sing in .
- 'reg' to sing up your account .
- 'exit' to turn off the application.
YOUR CHOICE: """

CLIENT_MENU = """
Enter:
- 'hotels' to list all available hotels.
- 'more' to get more information about specific hotel
- 'res' to make reservation.
- 'my res' to see the list of all your reservations.
- 'log out' to log off and go to previous menu.
YOUR CHOICE: """

WORKER_MENU = """
Enter:
- 'hotels' to list all available hotels.
- 'list res' to see the list of all reservations in the system.
- 'stat' to view different booking statistics. 
- 'moderate' to change the application offer.
- 'log out' to log off and go to previous menu.
YOUR CHOICE: """

CLIENT_RESERVATIONS_MENU = """
Reservations menu. Enter: 
- 'list res' to see detailed information about all your reservations.
- 'edit' to change your reservations.
- 'del' to remove one of your reservations.
- 'back' to back to the previous menu
YOUR CHOICE: """

MODERATE_MENU = """
You are in moderation menu. 

Please decide what you want to do:
- 'add hotel' to add new hotel to the offer.
- 'add room' to add new room to the hotel.
- 'del hotel' to remove hotel from the offer.
- 'del room' to remove room in the hotel from the offer.
- 'change costs' to change costs in the offer.
- 'back' to back to the previous menu.
YOUR CHOICE: """

ADD_HOTEL_DECISION_INTERFACE = """

Are you sure you want to add new hotel:
- 'yes' 
- 'no' 
YOUR CHOICE: """

ADD_ROOM_DECISION_INTERFACE = """

Are you sure you want to add new room:
- 'yes' 
- 'no' 
YOUR CHOICE: """

DELETE_HOTEL_DECISION_INTERFACE = """

Are you sure you want to remove this hotel:
- 'yes' 
- 'no' 
YOUR CHOICE: """

DELETE_ROOM_DECISION_INTERFACE = """

Are you sure you want to remove this room:
- 'yes' 
- 'no' 
YOUR CHOICE: """

RESERVATION_MENU_INTERFACE = """
You are in reservation menu. 

Please decide what you want to do:
- 'fill' to start filling the reservation form.
- 'back' to back to the previous menu.
YOUR CHOICE: """

CHANGE_COSTS_MENU = """
You are in costs menu. 

Please decide what you want to do:
- 'room cost' top change room  cost.
- 'dining cost' to add new room to the hotel.
- 'back' to back to the previous menu.
YOUR CHOICE: """

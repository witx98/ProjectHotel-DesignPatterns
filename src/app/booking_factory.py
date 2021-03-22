class BookingFactory:

    _isSingleton = None

    def __new__(self):
        if self._isSingleton is None:
            self._isSingleton = super(BookingFactory, self).__new__(self)
        return self._isSingleton

    @staticmethod
    def get_booking_info(type):
        from database import Database
        from guest import Guest
        from reservations import Reservation
        from worker import Worker
        from hotel import Hotel

        try:
            if type == "Guest":
                return Guest()
            elif type == "Worker":
                return Worker()
            elif type == "Reservation":
                return Reservation()
            elif type == "Database":
                return Database()
            elif type == "Hotel":
                return Hotel()
            raise AssertionError("Part not found")
        except AssertionError as _e:
            print(_e)
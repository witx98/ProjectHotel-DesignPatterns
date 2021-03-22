import pymysql


class Database:

    _isSingleton = None

    # Singleton design pattern
    def __new__(self):
        if self._isSingleton is None:
            self._isSingleton = super(Database, self).__new__(self)
        return self._isSingleton

    connection = pymysql.Connection(
        host='localhost',
        user='root',
        #password='zaq1@WSX',
        db='hotel',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


    def close_database(self):
        with self.connection.cursor():
            print("Database status: 'Closed'")
            self.connection.close()


    def get_log_info(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT user_login, user_password, user_ID, user_type FROM `users`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def add_user(self, user_name, user_surname, user_email, user_telephone, user_PESEL, user_login, user_password, user_type):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO users (user_name, user_surname, user_email, user_telephone, user_PESEL, " \
                  "user_login, user_password, user_type)" \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_name, user_surname, user_email, user_telephone, user_PESEL, user_login, user_password, user_type))
            self.connection.commit()


    def get_all_hotels(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT hotels.hotel_ID, hotels.hotel_name, countries.country_ID, locations.location_city " \
                  "FROM `hotels` " \
                  "INNER JOIN `locations` on locations.location_ID=hotels.location_id " \
                  "INNER JOIN `countries` on countries.country_ID=locations.country_id ORDER by locations.country_id"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_hotel_address(self, hotel_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT hotels.hotel_ID, hotels.hotel_name, countries.country_name, " \
                  "locations.location_city, locations.street_address " \
                  "FROM `hotels` " \
                  "INNER JOIN `locations` on locations.location_ID=hotels.location_id " \
                  "INNER JOIN `countries` on countries.country_ID=locations.country_id " \
                  "WHERE hotels.hotel_ID = %s"
            cursor.execute(sql, hotel_id)
            result = cursor.fetchall()
            return result


    def get_hotel_room_types(self, hotel_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT room_types.room_type_ID, room_types.room_type, room_types.room_type_price " \
                  "FROM `room_types` " \
                  "INNER JOIN `rooms` ON room_types.room_type_ID=rooms.room_type_id " \
                  "WHERE rooms.hotel_id = %s " \
                  "GROUP by room_types.room_type " \
                  "ORDER by room_types.room_type_ID"
            cursor.execute(sql, hotel_id)
            result = cursor.fetchall()
            return result


    def get_room_types(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT room_types.room_type_ID, room_types.room_type, room_types.room_type_price " \
                  "FROM `room_types` " \
                  "ORDER by room_types.room_type_ID"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_all_rooms(self, hotel_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT rooms.room_ID, room_types.room_type, room_types.room_type_price " \
                  "FROM `room_types` " \
                  "INNER JOIN `rooms` ON room_types.room_type_ID=rooms.room_type_id " \
                  "WHERE rooms.hotel_id = %s " \
                  "ORDER by room_types.room_type_ID"
            cursor.execute(sql, hotel_id)
            result = cursor.fetchall()
            return result


    def get_dining_options(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT dining_option_ID, dining_option_type, dining_option_cost " \
                  "FROM `dining_options` " \
                  "ORDER BY dining_option_ID"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_payment_methods(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT payment_method_ID, payment_method, payment_method_discount " \
                  "FROM `payment_methods`" \
                  "ORDER BY payment_method_ID"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def add_reservation(self, user_id, hotel_id, first_day_obj, last_day_obj, room_id, dining_option_id, payment_method_id, reservation_cost):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO reservations (client_id, hotel_id, first_day, last_day, room_id, dining_option_id, " \
                  "payment_method_id, cost) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user_id, hotel_id, first_day_obj, last_day_obj, room_id, dining_option_id, payment_method_id, reservation_cost))
            self.connection.commit()


    def get_all_reservations_info(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT reservations.reservation_ID, users.user_name, users.user_surname, hotels.hotel_name, " \
                  "reservations.first_day, reservations.last_day, rooms.room_ID, room_types.room_type, " \
                  "dining_options.dining_option_type, payment_methods.payment_method, reservations.cost " \
                  "FROM `reservations` " \
                  "INNER JOIN `users` ON reservations.client_id=users.user_ID " \
                  "INNER JOIN `hotels` ON reservations.hotel_id=hotels.hotel_ID " \
                  "INNER JOIN `rooms` ON reservations.room_id=rooms.room_ID " \
                  "INNER JOIN `room_types` ON rooms.room_type_id=room_types.room_type_ID " \
                  "INNER JOIN `dining_options` ON reservations.dining_option_id=dining_options.dining_option_ID " \
                  "INNER JOIN `payment_methods` ON reservations.payment_method_id=payment_methods.payment_method_ID " \
                  "ORDER BY reservations.reservation_ID"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_my_reservations_info(self, user_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT reservations.reservation_ID, users.user_name, users.user_surname, hotels.hotel_name, " \
                  "reservations.first_day, reservations.last_day, rooms.room_ID, room_types.room_type, " \
                  "dining_options.dining_option_type, payment_methods.payment_method, reservations.cost " \
                  "FROM `reservations` " \
                  "INNER JOIN `users` ON reservations.client_id=users.user_ID " \
                  "INNER JOIN `hotels` ON reservations.hotel_id=hotels.hotel_ID " \
                  "INNER JOIN `rooms` ON reservations.room_id=rooms.room_ID " \
                  "INNER JOIN `room_types` ON rooms.room_type_id=room_types.room_type_ID " \
                  "INNER JOIN `dining_options` ON reservations.dining_option_id=dining_options.dining_option_ID " \
                  "INNER JOIN `payment_methods` ON reservations.payment_method_id=payment_methods.payment_method_ID " \
                  "WHERE users.user_ID = %s " \
                  "ORDER BY reservations.reservation_ID"
            cursor.execute(sql, user_id)
            result = cursor.fetchall()
            return result


    def get_my_reservation(self, reservation_id):
        with self.connection.cursor() as cursor:
            sql = "SELECT reservations.reservation_ID, reservations.client_id, reservations.hotel_id, " \
                  "reservations.first_day, reservations.last_day, reservations.room_id, reservations.dining_option_id, " \
                  "reservations.payment_method_id, reservations.cost, room_types.room_type_price, " \
                  "dining_options.dining_option_cost, payment_methods.payment_method_discount " \
                  "FROM `reservations` " \
                  "INNER JOIN `rooms` ON reservations.room_id = rooms.room_ID " \
                  "INNER JOIN `room_types` ON rooms.room_type_id = room_types.room_type_ID " \
                  "INNER JOIN `dining_options` ON reservations.dining_option_id = dining_options.dining_option_ID " \
                  "INNER JOIN `payment_methods` ON reservations.payment_method_id = payment_methods.payment_method_ID " \
                  "WHERE reservation_ID = %s"
            cursor.execute(sql, reservation_id)
            result = cursor.fetchall()
            return result


    def update_my_reservation(self, hotel_id, first_day, last_day, room_id, dining_option_id, payment_method_id, cost, reservation_id):
        with self.connection.cursor() as cursor:
            sql = "UPDATE `reservations` SET hotel_id = %s, first_day = %s, last_day = %s, " \
                  "room_id = %s, dining_option_id = %s, payment_method_id = %s, cost = %s " \
                  "WHERE reservation_ID = %s"
            cursor.execute(sql, (hotel_id, first_day, last_day, room_id, dining_option_id, payment_method_id, cost, reservation_id))
            self.connection.commit()


    def delete_reservation(self, reservation_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `reservations` WHERE reservations.reservation_ID = %s"
            cursor.execute(sql, reservation_id)
            self.connection.commit()


    def delete_all_my_reservation(self, user_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `reservations` WHERE reservations.client_id = %s"
            cursor.execute(sql, user_id)
            self.connection.commit()


    def get_min_max_avg_cost(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT MIN(cost) as 'minimum', MAX(cost) as 'maximum', AVG(cost) as 'average' FROM `reservations`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_hotels_popularity(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT hotels.hotel_name, locations.location_city, " \
                  "COUNT(reservations.hotel_id) as 'bookings' " \
                  "FROM reservations " \
                  "INNER JOIN hotels ON reservations.hotel_id = hotels.hotel_ID " \
                  "INNER JOIN locations ON hotels.location_id = locations.location_ID " \
                  "GROUP BY hotels.hotel_ID " \
                  "ORDER BY COUNT(reservations.hotel_id) DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_room_types_popularity(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT room_types.room_type, COUNT(reservations.room_id) as 'bookings' " \
                  "FROM reservations " \
                  "INNER JOIN rooms ON reservations.room_id = rooms.room_ID " \
                  "INNER JOIN room_types ON rooms.room_type_id = room_types.room_type_ID " \
                  "GROUP BY room_types.room_type_ID " \
                  "ORDER BY COUNT(reservations.room_id) DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_dining_options_popularity(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT dining_options.dining_option_type, COUNT(reservations.dining_option_id) as 'orders' " \
                  "FROM reservations " \
                  "INNER JOIN dining_options ON reservations.dining_option_id = dining_options.dining_option_ID " \
                  "GROUP BY reservations.dining_option_id " \
                  "ORDER BY COUNT(reservations.dining_option_id) DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_payment_methods_popularity(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT payment_methods.payment_method, COUNT(reservations.payment_method_id) as 'orders' " \
                  "FROM reservations " \
                  "INNER JOIN payment_methods ON reservations.payment_method_id = payment_methods.payment_method_ID " \
                  "GROUP BY reservations.payment_method_id " \
                  "ORDER BY COUNT(reservations.payment_method_id) DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def get_clients_with_multiple_reservations(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT users.user_name, users.user_surname, COUNT(reservations.client_id) as 'reservations' " \
                  "FROM reservations " \
                  "INNER JOIN users ON reservations.client_id = users.user_ID " \
                  "GROUP BY reservations.client_id " \
                  "HAVING COUNT(reservations.client_id) > 1 " \
                  "ORDER BY COUNT(reservations.client_id) DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def add_country(self, country_id, country_name):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `countries` (countries.country_ID, countries.country_name) " \
                  "SELECT * FROM (SELECT %s AS country_ID, %s AS country_name) AS tmp " \
                  "WHERE NOT EXISTS ( SELECT country_ID FROM countries WHERE country_ID = %s ) LIMIT 1"
            cursor.execute(sql, (country_id, country_name, country_id))
            self.connection.commit()


    def add_location(self, location_city, street_address, country_id):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `locations` (locations.location_city, locations.street_address, locations.country_id) " \
                  "VALUES(%s, %s, %s) "
            cursor.execute(sql, (location_city, street_address, country_id))
            self.connection.commit()


    def get_latest_location_id(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT MAX(locations.location_ID) AS 'location_id' FROM locations"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def add_hotel(self, hotel_name, location_id):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `hotels` (hotels.hotel_name, hotels.location_id) VALUES (%s,%s)"
            cursor.execute(sql, (hotel_name, location_id))
            self.connection.commit()


    def add_room(self, hotel_id, room_type_id):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `rooms` (rooms.hotel_id, rooms.room_type_id) VALUES (%s,%s)"
            cursor.execute(sql, (hotel_id, room_type_id))
            self.connection.commit()


    def change_room_type_cost(self, room_type_id, room_type_price):
        with self.connection.cursor() as cursor:
            sql = "UPDATE `room_types` SET room_types.room_type_price = %s WHERE room_types.room_type_ID = %s"
            cursor.execute(sql, (room_type_price, room_type_id))
            self.connection.commit()


    def change_dining_option_cost(self, dining_option_id, dining_option_cost):
        with self.connection.cursor() as cursor:
            sql = "UPDATE `dining_options` SET dining_options.dining_option_cost = %s " \
                  "WHERE dining_options.dining_option_ID = %s"
            cursor.execute(sql, (dining_option_cost, dining_option_id))
            self.connection.commit()


    def delete_hotel(self, hotel_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE `reservations`, `rooms`, `hotels` " \
                  "FROM `hotels` " \
                  "INNER JOIN `reservations` ON reservations.hotel_id = hotels.hotel_ID " \
                  "INNER JOIN `rooms` ON rooms.hotel_id = hotels.hotel_ID " \
                  "WHERE hotels.hotel_ID = %s"
            cursor.execute(sql, hotel_id)
            self.connection.commit()


    def delete_room(self, room_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE `reservations`, `rooms`" \
                  "FROM `rooms`" \
                  "INNER JOIN `reservations` ON reservations.room_id = rooms.room_ID " \
                  "WHERE rooms.room_ID = %s"
            cursor.execute(sql, room_id)
            self.connection.commit()




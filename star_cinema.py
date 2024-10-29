class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, hall):
        self.hall_list.append(hall)

    @classmethod    
    def hall_list_show(cls):
        return cls.hall_list

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        showInfo = (show_id, movie_name, time)
        self.show_list.append(showInfo)
        all_seats = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = all_seats
    
    def book_seats(self, show_id, seat_book_list):
        if show_id not in self.seats:
            print(f"Error: Show ID '{show_id}' not found.")
            return
        
        for i, j in seat_book_list:
            if i >= self.rows or j >= self.cols or i < 0 or j < 0:
                print(f"Error: Seat at row {i}, column {j} is invalid. Please enter a valid seat number.")
                continue
            if self.seats[show_id][i][j] == '0':
                self.seats[show_id][i][j] = '1'
                print(f'Success: Your seat at row {i}, column {j} has been booked successfully.')
            else:
                print(f'Notice: The seat at row {i}, column {j} is already booked by someone else. Please select another seat.')
    
    def view_show_list(self):
        print("\nToday's Show List:")
        print("=" * 40)
        for show_id, movie_name, time in self.show_list:
            print(f"Show ID   : {show_id}")
            print(f"Movie Name: {movie_name}")
            print(f"Time      : {time}")
            print("-" * 40)

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f'Error: The show with ID "{show_id}" was not found.')
            return
        
        print(f"\nAvailable Seats for Show ID {show_id}:")
        print("=" * 40)
        for i in range(self.rows):
            for j in range(self.cols):
                print('1' if self.seats[show_id][i][j] == '1' else '0', end=" ")
            print()
        print("-" * 40)

    def check_show_id(self, show_id):
        if show_id not in self.seats:
            print(f'Error: The show with ID "{show_id}" was not found.')
            return False
        return True

    @property
    def hall_no(self):
        return self.__hall_no

Phitron = Star_Cinema()
hall_1 = Hall(10, 10, "Hall 1")

hall_1.entry_show('S1', "Shawshank Redemption", "10:00")
hall_1.entry_show('S2', "Life is Beautiful", "12:00")
hall_1.entry_show('S3', "The Godfather", "14:00")
hall_1.entry_show('S4', "The Matrix", "20:00")
hall_1.entry_show('S5', "Inception", "18:00")

while True:
    print("\nMenu Options:")
    print("1. View all shows today")
    print("2. View available seats in show")
    print("3. Book tickets")
    print("4. Exit")

    query = input("Enter your option (1-4): ")

    if query == '1':
        print("\nAvailable Shows Today:")
        print("=" * 40)
        for hall in Star_Cinema.hall_list_show():
            print(f"Hall No: {hall.hall_no}")
            hall.view_show_list()
            print("-" * 40)
    
    elif query == '2':
        show_id = input("Enter the show ID: ")
        hall_1.view_available_seats(show_id)

    elif query == '3':
        show_id = input("Enter the show ID to book seats: ")
        if not hall_1.check_show_id(show_id):
            continue

        seats_to_book = []
        n = int(input('Enter the number of seats you want to book: '))
        for _ in range(n):
            while True:
                try:
                    row = int(input("Enter row: "))
                    col = int(input("Enter column: "))
                    if (row < 0 or row >= hall_1.rows) or (col < 0 or col >= hall_1.cols):
                        print("Invalid seat number. Please enter again.")
                        continue
                    seats_to_book.append((row, col))
                    break
                except ValueError:
                    print("Please enter valid integers for row and column.")
        
        hall_1.book_seats(show_id, seats_to_book)

    elif query == '4':
        print("Exiting the system. Thank you!")
        break
    
    else:
        print("Invalid option. Please try again.")

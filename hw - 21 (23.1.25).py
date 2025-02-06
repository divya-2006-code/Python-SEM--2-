class HotelRoom:
    def __init__(self):
        self.__room_num=None
        self.__is_occupied=False
        self.__rate_per_night=None

    def get_room_num(self):
        return self.__room_num
    def set_room_num(self,room_num):
        if isinstance(room_num,int) and room_num>0:
            self.__room_num=room_num
        else:
            raise ValueError("Room number must be a positive integer.")

    def get_rate_per_night(self):
        return self.__rate_per_night
    def set_rate_per_night(self,rate_per_night):
        if isinstance(rate_per_night,(int,float)) and rate_per_night>0:
            self.__rate_per_night=rate_per_night
        else:
            raise ValueError("Rate per night must be greater than zero.")

    def check_in(self):
        if self.__is_occupied:
            raise Exception("The room is already occupied.")
        self.__is_occupied=True

    def check_out(self):
        if not self.__is_occupied:
            raise Exception("The room is already vacant.")
        self.__is_occupied=False

    def display_details(self):
        print(f"Room Number:{self.__room_num}")
        print(f"Rate per Night:$ {self.__rate_per_night:.2f}")
        print(f"Occupied:{'Yes' if self.__is_occupied else 'No'}")

room=HotelRoom()
room.set_room_num(101)
room.set_rate_per_night(200.50)
room.display_details()
        

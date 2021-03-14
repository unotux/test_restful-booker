from model.booking import BookingData


class BookingApi:
    def __init__(self, client):
        self.client = client

    def get_booking_ids(self, uid: int):
        """Returns the ids of all the bookings that exist within the API"""
        return self.client.request.get(self.client.url + f"/booking/")

    def get_booking(self, uid: int):
        """Returns a specific booking based upon the booking id provided"""
        return self.client.request.get(self.client.url + f"/booking/{uid}")

    def create_booking(self, data: BookingData):
        """Creates a new booking in the API"""
        data = data.object_to_dict()
        return self.client.request.post(self.client.url + "/booking", json=data)

    def update_booking(self, uid: int, data: BookingData):
        """Updates a current booking"""
        data = data.object_to_dict()
        return self.client.request.put(self.client.url + f"/booking/{uid}", json=data)

    def update_booking_partial(self, uid: int, data: BookingData):
        """Updates current booking with a partial payload"""
        data = data.object_to_dict()
        return self.client.request.patch(self.client.url + f"/booking/{uid}", json=data)

    def delete_booking(self, uid: int, data: BookingData):
        """Returns the ids of all the bookings that exist within the API"""
        data = data.object_to_dict()
        return self.client.request.delete(self.client.url + f"/booking/{uid}", json=data)

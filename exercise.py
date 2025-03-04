from abc import *



class Ticket:

    def __init__(self,ticket_id, ticket_type, price):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.price = price

    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @ticket_id.setter
    def ticket_id(self, value):
        if not Ticket.validate_ticket_id(value):
            raise ValueError("Invalid Ticket ID")
        else:
            self.__ticket_id = value

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Type: {self.ticket_type}, price: {self.price}."
    

    @staticmethod
    def validate_ticket_id(ticket_id):
        if len(ticket_id) != 8:
            return False
        if ticket_id[:3] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
        if not ticket_id[3:].isdigit():
            return False
        return True

class Event(ABC):

    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.dict = {}

    def add_ticket(self, ticket):
        if self.total_tickets == self.max_capacity:
            raise ValueError("max capacity reached")
        self.__tickets(ticket.ticket_id) = ticket

    def remove_ticket(ticket_id):
        if ticket_id not in self.tickets:
            raise ValueError("Ticket not found!")
        del self.__tickets(ticket_id)

    @property
    def total_tickets(self):
        return len(self.__tickets)

    @abstractmethod
    def generate_event_summary(self):
        pass

class Concert(Event):

    
    def __init__(self, name, max_capacity,artists):
        super().__init__(name, max_capacity)
        self.artists = artists

    def generate_event_summary(self):
        summary = f" Name: {self.name}\n Total ticket:{self.total_tickets}\nArtists:"

        for artist in self.artists:
            summary += f"\n    -{artist}"

        return summary
    

class PrivateEvent(Event):

    
    def __init__(self, name,artists):
        super().__init__(name, 50)
        self.artists = artists

    def generate_event_summary(self):
        summary = f" Name: {self.name}\n Total ticket:{self.total_tickets}\nArtists: {self.artists}"

        return summary

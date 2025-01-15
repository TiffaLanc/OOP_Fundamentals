# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner


class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner

        def update_owner(self):
              new_owner = input("Enter the new owner's name: ")
              self.owner = new_owner
              print(f"The new owner of the {self.type} with registraion number {self.registration_number} is {self.owner}")

        

class Event:
      def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participants = 0

      def add_participant(self):
            self.participants += 1

      def participant_count(self):
            return f" Event: {self.name}, has {self.participants} participants."
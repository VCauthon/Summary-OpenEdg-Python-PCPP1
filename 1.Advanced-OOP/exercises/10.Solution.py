import time
from datetime import datetime


# Metaclass
class AddTimeStamp(type):

    instance = []

    def get_instantation_time(self):
        return self.instantation_time
    
    def __new__(cmt, name, base, attributes):

        # Append into the class the timestamp attributes
        attributes['instantation_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attributes['get_instantation_time'] = AddTimeStamp.get_instantation_time

        # Add the instance class into the logging list
        AddTimeStamp.instance.append(f"{name} at > {attributes['instantation_time']}")

        # Add a second to see the difference in timestamp
        time.sleep(1)

        # Define the class
        return super().__new__(cmt, name, base, attributes)


# Creating legacy classes that will inherits one from another
class Legacy1(metaclass=AddTimeStamp):
    pass

class Legacy2(Legacy1, metaclass=AddTimeStamp):
    pass

class Legacy3(Legacy2, metaclass=AddTimeStamp):
    pass


# Instantiating the classes
obj_legacy3 = Legacy3()

# Looking at the timestamp
print(AddTimeStamp.instance)
print(obj_legacy3.get_instantation_time())
import json
import math

class Agent:
    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.latitude_degrees = latitude_degrees
        self.longitude_degrees = longitude_degrees

    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degrees * math.pi / 180

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        longitude = agent_attributes.pop("longitude")
        latitude = agent_attributes.pop("latitude")
        position = Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)
        # print(agent.agreeableness)
        print(agent.position.longitude)


main()

from weather import data

class SunPhase:
    def __init__(self, data):
        self.sunrise = data['sunrise']
        self.sunset = data['sunset']

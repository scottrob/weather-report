from weather import data

class CurrentObservation:
    def __init__(self, data):
        self.location = data['display_location']['full']
        self.time = data['observation_time']
        self.weather = data['weather']
        self.temp = data['temp_f']
        self.humidity = data['relative_humidity']
        self.wind_spd = data['wind_mph']
        self.pressure = data['pressure_mb']
        self.pressure_trend = data['pressure_trend']
        self.precip = data['precip_1hr_string']
        self.precip_today = data['precip_today_string']

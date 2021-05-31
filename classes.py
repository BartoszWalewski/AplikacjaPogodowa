'''
Created on 2021-05-31

@author: Bartosz Walewski
'''
import datetime


class Localization:
    def __init__(self, data_dictionary):
        date_time_ob = datetime.datetime.strptime(data_dictionary["location"]["localtime"], "%Y-%m-%d %H:%M")
        self.__details = {
            "city": data_dictionary["location"]["name"],
            "country": data_dictionary["location"]["country"],
            "time": date_time_ob.time(),
            "date": date_time_ob.strftime("%d.%m.%Y"),
            "last_update": data_dictionary["current"]["last_updated"],
            "current_temperature": data_dictionary["current"]["temp_c"],
            "min_temperature": data_dictionary["forecast"]["forecastday"][0]["day"]["mintemp_c"],
            "max_temperature": data_dictionary["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
            "icon": data_dictionary["current"]["condition"]["icon"],
            "wind_speed": data_dictionary["current"]["wind_kph"],
            "wind_dir": data_dictionary["current"]["wind_dir"]
        }
        self.__weather = []
        for i in range(0, 3):
            self.__weather.append(DayWeather(data_dictionary["forecast"]["forecastday"][i]))

    # Funkcja sluzaca do aktualizacji prognozy
    def update_info(self, data_dictionary):
        if self.__details["last_update"] == data_dictionary["current"]["last_updated"]:
            self.__details["date_time"] = data_dictionary["location"]["localtime"]
            return
        date_time_ob = datetime.datetime.strptime(data_dictionary["location"]["localtime"], "%Y-%m-%d %H:%M")
        self.__details["date"] = date_time_ob.strftime("%d.%m.%Y")
        self.__details["time"] = date_time_ob.time()
        self.__details["last_update"] = data_dictionary["current"]["last_updated"]
        self.__details["current_temperature"] = data_dictionary["current"]["temp_c"]
        self.__details["min_temperature"] = data_dictionary["forecast"]["forecastday"][0]["day"]["mintemp_c"]
        self.__details["max_temperature"] = data_dictionary["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
        self.__details["icon"] = data_dictionary["current"]["condition"]["icon"]
        self.__details["wind_speed"] = data_dictionary["current"]["wind_kph"]
        self.__details["wind_dir"] = data_dictionary["current"]["wind_dir"]
        for i in range(0, 3):
            self.__weather[i] = DayWeather(data_dictionary["forecast"]["forecastday"][i])

    def city(self):
        return self.__details["city"]

    def country(self):
        return self.__details["country"]

    def date(self):
        return self.__details["date"]

    def time(self):
        return self.__details["time"]

    def last_update(self):
        return self.__details["last_update"]

    def current_temperature(self):
        return round(self.__details["current_temperature"])

    def min_temperature(self):
        return round(self.__details["min_temperature"])

    def max_temperature(self):
        return round(self.__details["max_temperature"])

    def weather_icon(self):
        return "http:"+self.__details["icon"]

    def wind_speed(self):
        return round(self.__details["wind_speed"])

    def wind_direction(self):
        return self.__details["wind_dir"]

    def weather_today(self):
        return self.__weather[0]

    def weather_tomorrow(self):
        return self.__weather[1]

    def weather_day_after_tomorrow(self):
        return self.__weather[2]


class DayWeather:
    def __init__(self, forecast_hourly_dictionary):
        self.__all_day = {
            "min_temperature": forecast_hourly_dictionary["day"]["mintemp_c"],
            "max_temperature": forecast_hourly_dictionary["day"]["maxtemp_c"],
            "wind_speed": forecast_hourly_dictionary["day"]["maxwind_kph"],
            "icon": forecast_hourly_dictionary["day"]["condition"]["icon"]
        }
        self.__hourly = []
        for i in range(0, 24):
            self.__hourly.append({
                "temperature": forecast_hourly_dictionary["hour"][i]["temp_c"],
                "icon": forecast_hourly_dictionary["hour"][i]["condition"]["icon"]
            })

    def min_temperature(self):
        if self.__all_day["min_temperature"] % 1 == 0:
            return int(self.__all_day["min_temperature"])
        return round(self.__all_day["min_temperature"])

    def max_temperature(self):
        return round(self.__all_day["max_temperature"])

    def weather_icon(self):
        return "http:"+self.__all_day["icon"]

    def wind_speed(self):
        return round(self.__all_day["wind_speed"])

    def hour_icon(self, hour):
        return "http:" + self.__hourly[hour]["icon"]

    def hour_temp(self, hour):
        return round(self.__hourly[hour]["temperature"])


class HistoryLocalization:
    def __init__(self, data_dictionary):
        date_time_ob = datetime.datetime.strptime(data_dictionary["forecast"]["forecastday"][0]["date"], "%Y-%m-%d")
        self.__details = {
            "city": data_dictionary["location"]["name"],
            "country": data_dictionary["location"]["country"],
            "date": date_time_ob.strftime("%d.%m.%Y"),
            "avg_temperature": data_dictionary["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
            "min_temperature": data_dictionary["forecast"]["forecastday"][0]["day"]["mintemp_c"],
            "max_temperature": data_dictionary["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
            "icon": data_dictionary["forecast"]["forecastday"][0]["day"]["condition"]["icon"],
            "max_wind_speed": data_dictionary["forecast"]["forecastday"][0]["day"]["maxwind_kph"]
        }
        self.__weather = DayWeather(data_dictionary["forecast"]["forecastday"][0])

    def city(self):
        return self.__details["city"]

    def country(self):
        return self.__details["country"]

    def date(self):
        return self.__details["date"]

    def avarag_temperature(self):
        return round(self.__details["avg_temperature"])

    def min_temperature(self):
        return round(self.__details["min_temperature"])

    def max_temperature(self):
        return round(self.__details["max_temperature"])

    def weather_icon(self):
        return "http:"+self.__details["icon"]

    def max_wind_speed(self):
        return round(self.__details["max_wind_speed"])

    def weather_that_day(self):
        return self.__weather

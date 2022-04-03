from datetime import datetime
import requests


class TemperatureService:
    @staticmethod
    # get the average temperature of the selected holiday of the year
    def get_holiday_temperature(date):
        dateConverted = datetime.strptime(date, "%Y-%m-%d")
        result = requests.get(
            f"https://www.metaweather.com/api/location/523920/{dateConverted.year}/{dateConverted.month}/{dateConverted.day}/").json()

        temperatures = []

        for x in result:
            if x['created'].startswith(date):
                temperatures.append(x["the_temp"])

        return sum(temperatures) / len(temperatures)

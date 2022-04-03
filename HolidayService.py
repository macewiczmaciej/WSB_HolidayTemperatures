import requests


class HolidayService:
    # get all PL holiday names
    @staticmethod
    def get_holidays():
        holidays = []
        result = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/2017/PL").json()

        for x in result:
            holidays.append(x['localName'])

        holidays.sort()
        return holidays

    # look for date of given holiday
    @staticmethod
    def get_holiday_date(holiday_name, year):
        result = requests.get(
            f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()

        for x in result:
            if x['localName'] == holiday_name:
                return x['date']

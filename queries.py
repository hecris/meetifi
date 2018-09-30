
add_meetup_query = """
INSERT INTO meetups(user, name, address, meetup_date, meetup_time, invites)
VALUES (?, ?, ?, ?, ?, ?)"""

get_all_meetups_query = """
SELECT * FROM meetups
WHERE user = ? OR invites LIKE ?"""

get_meetup_query = """
SELECT * FROM meetups
WHERE name = ?"""


geocoder_url = "https://geocoder.api.here.com/6.2/geocode.json?app_id=uhIYrWPnuNlLk1tUWsfd&app_code=4DxLDAVJdKZy6uLvWof3jA&searchtext="
weather_url = "https://weather.api.here.com/weather/1.0/report.json?app_id=uhIYrWPnuNlLk1tUWsfd&app_code=4DxLDAVJdKZy6uLvWof3jA&product=forecast_hourly&"
position_url = "https://pos.api.here.com/positioning/v1/locate?app_id=uhIYrWPnuNlLk1tUWsfd&app_code=4DxLDAVJdKZy6uLvWof3jA"
position_data = {
  "wlan": [
  {"mac": "F4-55-95-11-2C-C1"}
  ]
}

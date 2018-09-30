
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

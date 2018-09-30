
add_meetup_query = """
INSERT INTO meetups(user, name, address, meetup_date, meetup_time, invites)
VALUES (?, ?, ?, ?, ?, ?)"""

get_meetups_query = """
SELECT * FROM meetups
WHERE user = ?"""

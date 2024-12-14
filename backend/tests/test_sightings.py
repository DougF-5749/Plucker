from datetime import datetime
from lib.models.sightings import Sighting

"""
Sighting constructs with a bird name,  and password
"""
def test_sightings_constructs():
    user = Sighting(1, "eagle", "2024-03-22", "London", 1)
    assert user.id == 1
    assert user.bird_name == "eagle"
    assert user.date_spotted.isoformat() == "2024-03-22"
    assert user.location == "London"
    assert user.user_id == 1

"""
We can format users to strings nicely
"""
def test_sighting_format_nicely():
    sightings = Sighting(1, "eagle", "2024-03-22", "London", 1)
    assert str(sightings) == "User(1, eagle, 2024-03-22, London, 1)"


"""
We can compare two identical users
And have them be equal
"""
def test_sightings_are_equal():
    Sightings1 = Sighting(1, "eagle", "2024-03-22", "London", 1)
    Sightings2 = Sighting(1, "eagle", "2024-03-22", "London", 1)
    assert Sightings1 == Sightings2
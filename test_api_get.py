import requests

var_people_id = "1"
var_vehicles_count = 2
var_height = 100
var_films_id = "3"

base_url = "https://swapi.dev"
people_path = "/api/people/" + var_people_id
people_response = requests.get(url=base_url + people_path,verify=False)
people_response_json = people_response.json()
people_status_code = people_response.status_code

# API 1
class TestPeopleClass:
    def test_people_get(self):
        assert people_status_code == 200
    def test_people_height(self):
        assert int(people_response_json['height']) > var_height
    def test_people_vehicles(self):
        assert len(people_response_json['vehicles']) == var_vehicles_count

films_path = "/api/films/" + var_films_id
films_response = requests.get(url=base_url + films_path,verify=False)
films_response_json = films_response.json()
films_status_code = films_response.status_code

# API 2
class TestFilmsClass:
    def test_films_get(self):
        assert films_status_code == 200
    def test_films_starship(self):
        assert len(films_response_json['starships']) > len(people_response_json['starships'])
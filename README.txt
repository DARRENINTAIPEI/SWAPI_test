# SWAPI_test
 This "test_api_get.py" is used to test http://swapi.dev/api
 Refer to https://swapi.dev/documentation#intro to know about resources
 Issue "python test_api_get.py" directly in Linux CLI to perform the test
 
   #For API test 1 People
   Change variable "var_people_id" to retrieve relevant api response.
   Change variable "var_height" to verify if the person taller than specific height.
   Change variable "var_vehicles_count" to verify if the person own specific count of vehicles.
 
   #For API test 2 Films
   Change variable "var_films_id" to verify if the starships of specific films outnumber the film of person from API test 1.

 
 
# Locust_test
This "locust.py" is used to stress https://swapi.dev/api/people/1/
Issue "apt install locust" to install locust beforehand.
After installation. Issue "locust -f locustfile.py -u 10 -r 10 -t 10s --headless" to perform the test in Linuc CLI directly.
Parameter -u means number of users; -r means users per second; -t means total run times; --headless is used to perfrom test instantly without web interface.
You may issue "locust -h" to see more details.

from locust import HttpUser, task, constant_pacing

class MainClassTest(HttpUser):
    wait_time = constant_pacing(1)
    @task
    def get_user(self):
        with self.client.get('/people/1/', catch_response=True) as response:
            if response.status_code != 200:
                response.failure("FAIL: Status code is not equal to 200")
            if len(response.json()['vehicles']) < 1:
                response.failure("FAIL: Vehicles count is less than 1")


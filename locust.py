import time
from locust import HttpUser, task, between

class HackazonUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def main_page(self):
        self.client.get("/", verify=False)

import time
from locust import HttpUser, task, between

class HackazonUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def main_page(self):
        self.client.get("/index.php?delay=100&length=6000", verify=False)

import time
from locust import HttpUser, task, between

class HackazonUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def main_page(self):
        self.client.get("/", verify=False)

    @task
    def view_items(self):
        self.client.get("/product/view?id=72", verify=False)
        self.client.get("/product/view?id=81", verify=False)
        self.client.get("/product/view?id=16", verify=False)
        self.client.get("/category/view?id=2", verify=False)
        self.client.get("/category/view?id=3", verify=False)
        self.client.get("/category/view?id=1", verify=False)




    @task(2)
    def other_tasks(self):
        self.client.get("/faq", verify=False)
        self.client.get("/contact", verify=False)
        self.client.get("/", verify=False)


from locust import HttpUser, between, task


class SecretaireDeClub(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def afficher_les_competitions(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(1)
    def acheter_une_place(self):
        self.client.post("/purchasePlaces", data={
            "competition": "Winter Cup",
            "club": "Simply Lift",
            "places": "1",
        })

    @task(1)
    def afficher_le_tableau_des_points(self):
        self.client.get("/points")

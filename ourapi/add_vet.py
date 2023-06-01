import requests

firstname = input("First Name: ")
lastname = input("Last Name: ")
phone = input("Phone Number: ")
address = input("Address: ")
room = input("Please input Room: ")
appointment_times = input("Please input appointment time: ")
email = input("Email: ")


Add_vet = requests.post(
    "http://localhost:8000/api/add_vet"
)
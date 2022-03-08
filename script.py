import requests

data = {"up_front_payed": "true"}
requests.put('http://localhost:8080/edit_investment/1/', data=data)


import httpx
import time

"""Создание пользователя"""
payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}
res_new_user = httpx.post("http://localhost:8003/api/v1/users", json=payload)
res_data = res_new_user.json()
print("Created new user json: ", res_data)
print("Status code: ", res_new_user.status_code)


"""Открытие счета новому пользователю"""
payload_dep = {
  "userId": res_data['user']['id']
}
res_open_deposit = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=payload_dep)
res_open_dep_answer = res_open_deposit.json()
print("Open deposit account answer: ", res_open_dep_answer)
print("Status code: ", res_open_deposit.status_code)
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
print("\nCreated new user json: ", res_data)
print("Status code: ", res_new_user.status_code)


"""Создать кредитный счёт для пользователя"""
json_for_open_cc = {
  "userId": res_data['user']['id']
}
res_open_cc = httpx.post('http://localhost:8003/api/v1/accounts/open-credit-card-account', json=json_for_open_cc)
res_open_cc_answer = res_open_cc.json()
print('\nOpen credit card: ', res_open_cc_answer)
print('Open credit card status code: ', res_open_cc.status_code)


"""Совершить операцию покупки (purchase)"""
json_for_purchase_operation = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "category": "taxi",
  "cardId": res_open_cc_answer['account']['cards'][0]['id'],
  "accountId": res_open_cc_answer['account']['cards'][0]['accountId']
}
res_make_purchase_op = httpx.post('http://localhost:8003/api/v1/operations/make-purchase-operation', json=json_for_purchase_operation)
res_make_purchase_op_answer = res_make_purchase_op.json()
print("\nMake purchase opertaion: ", res_make_purchase_op_answer)
print("Make purchase opertaion status code: ", res_make_purchase_op.status_code)


"""Получить чек по операции"""
res_operation_receipt = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{res_make_purchase_op_answer["operation"]["id"]}")
res_operation_receipt_answer = res_operation_receipt.json()
print("\nOperation receipt: ", res_operation_receipt_answer)
print("Operation receipt status code: ", res_operation_receipt.status_code)
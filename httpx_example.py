import httpx


res = httpx.get('https://jsonplaceholder.typicode.com/todos/1', timeout=None)
print(res.text)


# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
    
# }
res_2 = httpx.post('https://jsonplaceholder.typicode.com/todos', timeout=None)
print(res_2.text)


# headers = {"Authorization": "Bearer my_secret_token"}
# res_3 = httpx.get("https://httpbin.org/get", headers=headers)
# print(res_3.text)
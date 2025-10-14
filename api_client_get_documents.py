from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

# Инициализация клиентов для взаимодействия с различными сервисами Gateway
users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()

# Шаг 1: Создание нового пользователя в системе
create_user_response = users_gateway_client.create_user()
print("Create user response:", create_user_response)

# Шаг 2: Открытие кредитного счета для созданного пользователя
create_credit_card_account = accounts_gateway_client.open_credit_card_account(create_user_response["user"]["id"])
print("Create credit card account response:", create_credit_card_account)

# Шаг 3: Получение тарифного документа для открытого счета
get_tariff_document = documents_gateway_client.get_tariff_document(create_credit_card_account["account"]["id"])
print("Get tariff document response:", get_tariff_document)

# Шаг 4: Получение договорного документа для открытого счета
get_contract_document = documents_gateway_client.get_contract_document(create_credit_card_account['account']["id"])
print("Get contract document response:", get_contract_document)

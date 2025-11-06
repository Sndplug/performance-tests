from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client

# Инициализация клиентов для взаимодействия с различными сервисами Gateway
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
operations_gateway_client = build_operations_gateway_grpc_client()

# Шаг 1: Создание нового пользователя в системе
create_user_response = users_gateway_client.create_user()
print("Create user response:", create_user_response)

# Шаг 2: Открыть дебетовый счет для созданного пользователя
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(create_user_response.user.id)
print("Open debit card account response:", open_debit_card_account_response)

# Шаг 3: Создать операцию пополнения счета
account_id = open_debit_card_account_response.account.id
card_id = open_debit_card_account_response.account.cards[0].id  # берем первую карту

make_top_up_operations_response = operations_gateway_client.make_top_up_operation(
    card_id=card_id,         # ID карты из предыдущего шага
    account_id=account_id    # ID счета из предыдущего шага
)
print("Make top up operations response:", make_top_up_operations_response)
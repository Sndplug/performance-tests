from locust import User, between, task

from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client

class OpenDebitCardAccountScenarioUser(User):

    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient

    def on_start(self) -> None:
        """
        Метод, вызываемый при старте каждого виртуального пользователя.
        Здесь происходит инициализация gRPC API клиентов и создание пользователя.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)

    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача: создание дебетого счета для клиента.
        Метод будет многократно вызываться Locust-агентами.
        """
        self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id,
        )
import grpc
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub

from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
OpenDebitCardAccountRequest,
OpenDebitCardAccountResponse
)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub

from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
IssueVirtualCardRequest,
IssueVirtualCardResponse
)
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub

from tools.fakers import fake


channel = grpc.insecure_channel('localhost:9003')

users_gateway_service = UsersGatewayServiceStub(channel)
cards_gateway_service = CardsGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)


create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number(),
)

create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print("Create user response:", create_user_response)


open_credit_card_request = OpenDebitCardAccountRequest(user_id=create_user_response.user.id)
open_credit_card_response: IssueVirtualCardResponse = (
    accounts_gateway_service.OpenDebitCardAccount(open_credit_card_request))
print("Open credit card response:", open_credit_card_response)


issue_virtual_card_request = IssueVirtualCardRequest(
                            user_id=create_user_response.user.id,
                            account_id=open_credit_card_response.account.id)
issue_virtual_card_response: IssueVirtualCardResponse = cards_gateway_service.IssueVirtualCard(issue_virtual_card_request)
print("Issue virtual card response:", issue_virtual_card_response)

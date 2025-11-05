from clients.grpc.client import GRPCClient
from grpc import Channel
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest, GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest, GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest, MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest, MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest, MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет методы для работы с операциями: получение информации, создание операций разных типов.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(self.channel)

    # Низкоуровневые методы API
    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с ID операции
        :return: Ответ от сервиса с данными операции
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с ID операции
        :return: Ответ от сервиса с данными чека операции
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос с параметрами для получения списка операций
        :return: Ответ от сервиса со списком операций
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос с параметрами для получения статистики операций
        :return: Ответ от сервиса со статистикой операций
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос для создания операции комиссии
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос для создания операции пополнения
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос для создания операции кэшбэка
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос для создания операции перевода
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос для создания операции покупки
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос для создания операции оплаты по счету
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.

        :param request: gRPC-запрос для создания операции снятия наличных
        :return: Ответ от сервиса с данными созданной операции
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    # Высокоуровневые методы-обёртки
    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получить информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции
        :return: Ответ с данными операции
        """
        request = GetOperationRequest(operation_id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получить чек по операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции
        :return: Ответ с данными чека операции
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Получить список операций для определенного счета.

        :param account_id: Идентификатор счета
        :return: Ответ со списком операций
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получить статистику по операциям для определенного счета.

        :param account_id: Идентификатор счета
        :return: Ответ со статистикой операций
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
        Создать операцию пополнения счета.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
        Создать операцию кэшбэка.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
        Создать операцию перевода средств.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            category=fake.category(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
        Создать операцию оплаты счета/квитанции.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Создать операцию снятия наличных.

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор счета
        :return: Ответ с данными созданной операции
        """
        request = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())
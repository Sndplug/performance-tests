from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """Структура данных для получения списка операций."""
    accountId: str

class GetOperationsSummaryQueryDict(TypedDict):
    """Структура данных для получения статистики по операциям."""
    accountId: str

class MakeOperationRequestDict(TypedDict):
    """Общий словарь для создания операций
    
    :param status: Статус операции (например, 'FAILED', 'SUCCESS', 'IN_PROGRESS', 'UNSPECIFIED')
    :param amount: Сумма операции
    :param accountId: Идентификатор счета
    :param cardId: Идентификатор карты
    """
    status: str
    amount: float
    cardId: str
    accountId: str
    
class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции комиссии."""
    pass
    
class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции пополнения счета."""
    pass
    
class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции кэшбэка."""
    pass

class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции перевода средств."""
    pass
    
class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции покупки."""
    category: str

class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции оплаты счета/квитанции."""
    pass
    
class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """Структура данных для создания операции снятия наличных."""
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    Предоставляет методы для работы с операциями: получение информации, создание операций разных типов.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения информации об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека по операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными чека операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос для получения списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, включая accountId.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))
    
    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос для получения статистики по операциям для определенного счета за период.

        :param query: Словарь с параметрами запроса, включая accountId.
        :return: Объект httpx.Response со статистикой операций.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))
    
    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param data: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param data: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param data: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param data: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param data: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param data: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param data: Словарь с данными для создания операции снятия наличных.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
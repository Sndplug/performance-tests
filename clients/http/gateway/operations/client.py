from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


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

class OperationDict(TypedDict):
    """Структура данных для ответа с информацией об операции."""
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """Структура данных для чека операции."""
    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """Структура данных для статистики по операциям."""
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float
    
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

# Структуры с возвращаемыми данными
class GetOperationsResponseDict(TypedDict):
    """Структура ответа для получения списка операций."""
    operations: list[OperationDict]

class GetOperationResponseDict(TypedDict):
    """Структура ответа для получения списка операции."""
    operation: OperationDict

class GetOperationsSummaryResponseDict(TypedDict):
    """Структура ответа для получения сводной статистики по операциям."""
    summary: list[OperationsSummaryDict]

class GetOperationReceiptResponseDict(TypedDict):
    """Структура ответа для получения чека по операции."""
    receipt: list[OperationReceiptDict]

class MakeFeeOperationResponseDict(TypedDict):
    """Структура ответа для создания операции комиссии."""
    operation: OperationDict

class MakeTopUpOperationResponseDict(TypedDict):
    """Структура ответа для создания операции пополнения."""
    operation: OperationDict

class MakeCashbackOperationResponseDict(TypedDict):
    """Структура ответа для создания операции кэшбэка."""
    operation: OperationDict

class MakeTransferOperationResponseDict(TypedDict):
    """Структура ответа для создания операции перевода."""
    operation: OperationDict

class MakePurchaseOperationResponseDict(TypedDict):
    """Структура ответа для создания операции покупки."""
    operation: OperationDict

class MakeBillPaymentOperationResponseDict(TypedDict):
    """Структура ответа для создания операции оплаты счета."""
    operation: OperationDict

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Структура ответа для создания операции снятия наличных."""
    operation: OperationDict


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

    ####Высокоуровневые методы
    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить информацию об операции по её идентификатору.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operation_api
        и преобразует ответ в структурированные данные.

        :param operation_id: Уникальный идентификатор операции.
        :return: Словарь с данными операции.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получить чек по операции по её идентификатору.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operation_receipt_api
        и преобразует ответ в структурированные данные.

        :param operation_id: Уникальный идентификатор операции.
        :return: Словарь с данными чека операции.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций для определенного счета.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operations_api
        и преобразует ответ в структурированные данные.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получить статистику по операциям для определенного счета.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operations_summary_api
        и преобразует ответ в структурированные данные.

        :param account_id: Идентификатор счета.
        :return: Словарь со статистикой операций.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, status: str, amount: float, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Создать операцию комиссии.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_fee_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeFeeOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, status: str, amount: float,
                              card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Создать операцию пополнения счета.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_top_up_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeTopUpOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, status: str, amount: float, card_id: str,
                                account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Создать операцию кэшбэка.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_cashback_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeCashbackOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, status: str, amount: float, card_id: str,
                                account_id: str) -> MakeTransferOperationResponseDict:
        """
        Создать операцию перевода средств.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_transfer_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeTransferOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, status: str, amount: float, card_id: str, account_id: str,
                                category: str) -> MakePurchaseOperationResponseDict:
        """
        Создать операцию покупки.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_purchase_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :param category: Категория покупки.
        :return: Словарь с данными созданной операции.
        """
        request = MakePurchaseOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, status: str, amount: float, card_id: str,
                                    account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Создать операцию оплаты счета/квитанции.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_bill_payment_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeBillPaymentOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, status: str, amount: float, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создать операцию снятия наличных.

        Высокоуровневый метод, который выполняет HTTP-запрос через make_cash_withdrawal_operation_api
        и преобразует ответ в структурированные данные.

        :param status: Статус операции.
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
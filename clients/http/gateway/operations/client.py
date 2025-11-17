from httpx import Response, QueryParams
from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    OperationStatusRequest,
    GetOperationsQuerySchema,
    GetOperationsSummaryQuerySchema,
    MakeFeeOperationRequestSchema,
    MakeTopUpOperationRequestSchema,
    MakeCashbackOperationRequestSchema,
    MakeTransferOperationRequestSchema,
    MakePurchaseOperationRequestSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeCashWithdrawalOperationRequestSchema,
    GetOperationsResponseSchema,
    GetOperationResponseSchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema
)

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
        return self.get(f"/api/v1/operations/{operation_id}",
                        extensions=HTTPClientExtensions(route="/api/v1/operations/{operation_id}")
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека по операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными чека операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}",
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operation-receipt/{operation_id}")
        )

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, включая accountId.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations",
                        params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations")
        )
    
    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения статистики по операциям для определенного счета за период.

        :param query: Словарь с параметрами запроса, включая accountId.
        :return: Объект httpx.Response со статистикой операций.
        """
        return self.get("/api/v1/operations/operations-summary",
                        params=QueryParams(**query.model_dump(by_alias=True)),
                        extensions=HTTPClientExtensions(route="/api/v1/operations/operations-summary")
        )
    
    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param data: Словарь с данными для создания операции комиссии.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))
    
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param data: Словарь с данными для создания операции пополнения.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param data: Словарь с данными для создания операции кэшбэка.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param data: Словарь с данными для создания операции перевода.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param data: Словарь с данными для создания операции покупки.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету.

        :param data: Словарь с данными для создания операции оплаты по счету.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param data: Словарь с данными для создания операции снятия наличных.
        :return: Объект httpx.Response с результатом создания операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    ####Высокоуровневые методы
    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получить информацию об операции по её идентификатору.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operation_api
        и преобразует ответ в структурированные данные.

        :param operation_id: Уникальный идентификатор операции.
        :return: Словарь с данными операции.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получить чек по операции по её идентификатору.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operation_receipt_api
        и преобразует ответ в структурированные данные.

        :param operation_id: Уникальный идентификатор операции.
        :return: Словарь с данными чека операции.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получить список операций для определенного счета.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operations_api
        и преобразует ответ в структурированные данные.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получить статистику по операциям для определенного счета.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_operations_summary_api
        и преобразует ответ в структурированные данные.

        :param account_id: Идентификатор счета.
        :return: Словарь со статистикой операций.
        """
        query = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
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
        request = MakeFeeOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self,
                              card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
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
        request = MakeTopUpOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str,
                                account_id: str) -> MakeCashbackOperationResponseSchema:
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
        request = MakeCashbackOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str,
                                account_id: str) -> MakeTransferOperationResponseSchema:
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
        request = MakeTransferOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str,
                                category: str) -> MakePurchaseOperationResponseSchema:
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
        request = MakePurchaseOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str,
                                    account_id: str) -> MakeBillPaymentOperationResponseSchema:
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
        request = MakeBillPaymentOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
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
        request = MakeCashWithdrawalOperationRequestSchema(
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
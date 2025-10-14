from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client  # Импортируем builder


class DocumentDict(TypedDict):
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    tariff: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить тарифный документ по счету.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_tariff_document_api

        :param account_id: Идентификатор счета для получения тарифного документа
        :return: Словарь с данными тарифного документа
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить контракта по счету.

        Высокоуровневый метод, который выполняет HTTP-запрос через get_contract_document_api

        :param account_id: Идентификатор счета для получения контракта по счету.
        :return: Словарь с данными контракта по счету.
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


# Добавляем builder для DocumentsGatewayHTTPClient
def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
from client.http.client import HTTPClient
from httpx import Response
from typing import TypedDict


class IssueVirtualCardDict(TypedDict):
    """
    Структура данных для создани виртаульной карты пользователю
    """
    userId: str
    accountId: str


class IssuePhysicalCardDict(TypedDict):
    """
    Структура данных для создани физической карты пользователю
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """Клиент для работы с API карт - /api/v1/cards/"""
    
    
    def issue_virtual_card_api(self, request: IssueVirtualCardDict) -> Response:
        """
        Создание виртуальной карты.

        Args:
            request: Словарь с данными для создания виртуальной карты.
                Содержит поля:
                - userId (str): Идентификатор пользователя
                - accountId (str): Идентификатор аккаунта

        Returns:
            Response: Ответ сервера с результатом операции о создании виртуальной карты
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)
    
    
    def issue_physical_card_api(self, request: IssuePhysicalCardDict) -> Response:
        """
        Создание физической карты.

        Args:
            request: Словарь с данными для создания физической карты.
                Содержит поля:
                - userId (str): Идентификатор пользователя
                - accountId (str): Идентификатор аккаунта

        Returns:
            Response: Ответ сервера с результатом операции о создании физической карты
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
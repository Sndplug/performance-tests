from pydantic import BaseModel, ConfigDict, Field
from enum import StrEnum
from datetime import datetime

class GetOperationsQuerySchema(BaseModel):
    """Структура данных для получения списка операций."""
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class GetOperationsSummaryQuerySchema(BaseModel):
    """Структура данных для получения статистики по операциям."""
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")

class OperationStatusRequest(StrEnum):
    FAILED="FAILED"
    COMPLETED="COMPLETED"
    IN_PROGRESS="IN_PROGRESS"
    UNSPECIFIED="UNSPECIFIED"

class MakeOperationRequestSchema(BaseModel):
    """Общий словарь для создания операций

    :param status: Статус операции (например, 'FAILED', 'COMPLETED', 'IN_PROGRESS', 'UNSPECIFIED' -> Class OperationStatusRequest)
    :param amount: Сумма операции
    :param account_id: Идентификатор счета
    :param card_id: Идентификатор карты
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatusRequest
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class OperationType(StrEnum):
    FEE="FEE"
    TOP_UP="TOP_UP"
    PURCHASE="PURCHASE"
    CASHBACK="CASHBACK"
    TRANSFER="TRANSFER"
    BILL_PAYMENT="BILL_PAYMENT"
    CASH_WITHDRAWAL="CASH_WITHDRAWAL"

class OperationStatusResponse(StrEnum):
    FAILED="FAILED"
    COMPLETED="COMPLETED"
    IN_PROGRESS="IN_PROGRESS"
    UNSPECIFIED="UNSPECIFIED"

class OperationSchema(BaseModel):
    """Структура данных для ответа с информацией об операции."""
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: OperationType
    status: OperationStatusResponse
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """Структура данных для чека операции."""
    url: str
    document: str

class OperationsSummarySchema(BaseModel):
    """Структура данных для статистики по операциям."""
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции комиссии."""
    pass

class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции пополнения счета."""
    pass

class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции кэшбэка."""
    pass

class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции перевода средств."""
    pass

class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции покупки."""
    category: str

class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции оплаты счета/квитанции."""
    pass

class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для создания операции снятия наличных."""
    pass

# Структуры с возвращаемыми данными
class GetOperationsResponseSchema(BaseModel):
    """Структура ответа для получения списка операций."""
    operations: list[OperationSchema]

class GetOperationResponseSchema(BaseModel):
    """Структура ответа для получения списка операции."""
    operation: OperationSchema

class GetOperationsSummaryResponseSchema(BaseModel):
    """Структура ответа для получения сводной статистики по операциям."""
    summary: list[OperationsSummarySchema]

class GetOperationReceiptResponseSchema(BaseModel):
    """Структура ответа для получения чека по операции."""
    receipt: list[OperationReceiptSchema]

class MakeFeeOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции комиссии."""
    operation: OperationSchema

class MakeTopUpOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции пополнения."""
    operation: OperationSchema

class MakeCashbackOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции кэшбэка."""
    operation: OperationSchema

class MakeTransferOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции перевода."""
    operation: OperationSchema

class MakePurchaseOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции покупки."""
    operation: OperationSchema

class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции оплаты счета."""
    operation: OperationSchema

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Структура ответа для создания операции снятия наличных."""
    operation: OperationSchema
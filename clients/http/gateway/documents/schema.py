from pydantic import BaseModel, ConfigDict


class DocumentSchema(BaseModel):
    url: str
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    contract: DocumentSchema
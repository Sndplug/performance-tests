from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserBaseSchema(BaseModel):
    """Базовая схема с общими полями"""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class UserSchema(UserBaseSchema):
    """Схема пользователя с ID"""
    id: str

class CreateUserRequestSchema(UserBaseSchema):
    """Схема запроса на создание пользователя"""
    pass

class CreateUserResponseSchema(BaseModel):
    """Схема ответа с созданным пользователем"""
    user: UserSchema
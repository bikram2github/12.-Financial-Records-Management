from pydantic import BaseModel, Field,EmailStr
from typing import Optional,Annotated,Literal

class FinancialRecord(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier of the financial record")
    amount: float = Field(...,gt=0, description="The amount of the financial record,It should be greater than 0")
    record_type: Literal["income", "expense"] = Field(..., description="The type of the financial record, type such as income or expense")
    category: str = Field(..., description="The category of the financial record")
    date: Optional[str] = Field(None, default=None, description="The date of the financial record in DD-MM-YYYY format. If not provided, it will be set to the current date.")
    note: Optional[str] = Field(None, description="A brief description of the financial record")

    class Config:
        schema_extra = {
            "example": {
                "date": "04-04-2026",
                "amount": 5000,
                "record_type": "expense",
                "category": "Rent",
                "note": "Paid monthly rent for April"
            }
        }



class FinancialRecordUpdate(BaseModel):
    amount: Annotated[Optional[float], Field(None, gt=0, default=None, description="The amount of the financial record, It should be greater than 0")]
    record_type: Annotated[Optional[Literal["income", "expense"]], Field(None, description="The type of the financial record, type such as income or expense")] = Field(..., description="The type of the financial record, type such as income or expense")
    category: Annotated[Optional[str], Field(None, description="The category of the financial record")] = Field(..., description="The category of the financial record")
    date: Annotated[Optional[str], Field(None, default=None, description="The date of the financial record in DD-MM-YYYY format. If not provided, it will be set to the current date.")] = Field(None, default=None, description="The date of the financial record in DD-MM-YYYY format. If not provided, it will be set to the current date.")
    note: Annotated[Optional[str], Field(None, description="A brief description of the financial record")] = Field(None, description="A brief description of the financial record")


class Usersignup(BaseModel):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., min_length=6, description="The password for the user account, It should be at least 6 characters long")


class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., description="The password for the user account")
from pydantic import BaseModel, Field
from typing import Optional,Annotated,Literal

class FinancialRecord(BaseModel):
    tran_id: Optional[str] = Field(None, description="The unique identifier of the financial record")
    amount: float = Field(...,gt=0, description="The amount of the financial record,It should be greater than 0")
    record_type: Literal["income", "expense"] = Field(..., description="The type of the financial record, type such as income or expense")
    category: str = Field(..., description="The category of the financial record")
    note: Optional[str] = Field(description="A brief description of the financial record")


    class Config:
        json_schema_extra  = {
            "example": {
                "amount": 5000,
                "record_type": "expense",
                "category": "Rent",
                "note": "Paid monthly rent for April"
            }
        }



class FinancialRecordUpdate(BaseModel):
    amount: Annotated[Optional[float],Field(None, gt=0, description="The amount must be greater than 0")]
    record_type: Annotated[Optional[Literal["income", "expense"]],Field(None, description="Type: income or expense")]
    category: Annotated[Optional[str],Field(None, description="Category of the record")]
    note: Annotated[Optional[str],Field(None, description="Short description")]


'''
class Usersignup(BaseModel):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., min_length=6, description="The password for the user account, It should be at least 6 characters long")


class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., description="The password for the user account")'''
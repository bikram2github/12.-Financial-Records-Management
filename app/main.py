from fastapi import FastAPI,Path,Query,HTTPException
from fastapi.responses import JSONResponse
from app.schemas import FinancialRecord,FinancialRecordUpdate
from app.database import create_db_table, delete_record, insert_record, get_all_records, get_records_by_date, get_by_category, get_by_type,sort_records, update_record,create_users_table
import uuid
import json


app = FastAPI()


def load_data():
    data=get_all_records()
    data=json.dumps(data)

    return data


@app.lifespan("startup")
def startup():
    create_db_table()
    create_users_table()


@app.get("/")
def root():
    return {"message": "Financial Records Management"}



@app.post("/create")
def create_record(record: FinancialRecord):
    data = record.model_dump()
    data["tran_id"] = str(uuid.uuid4())
    insert_record(data["tran_id"], data["amount"], data["record_type"], data["category"], data["note"])

    return {"message": "Record created successfully", "record": data}



@app.get("/records")
def read_records():
    records = get_all_records()
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"records": records}



@app.get("/records/date/{date}")
def read_records_by_date(date: str = Path(..., description="The date of the financial records in DD-MM-YYYY format",example="04-04-2026")):
    records = get_records_by_date(date)
    if not records:
        raise HTTPException(status_code=404, detail="No records found for this date")
    return {"records": records}



@app.get("/records/category/{category}")
def read_records_by_category(category: str = Path(..., description="The category of the financial records",example=["Rent","Groceries","Education","Entertainment","Utilities","Transportation","Healthcare"])):
    records = get_by_category(category)
    if not records:
        raise HTTPException(status_code=404, detail="No records found for this category")
    return {"records": records}



@app.get("/records/type/{record_type}")
def read_records_by_type(record_type: str = Path(..., example="income")):
    
    if record_type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Invalid type.Should be either 'income' or 'expense'")

    records = get_by_type(record_type)

    if not records:
        raise HTTPException(status_code=404, detail="No records found")

    return {"records": records}



@app.get("/sort")
def read_sorted_records(sort_by: str = Query(..., description="The field to sort by.It should be either 'date' or 'amount'.", example=["date", "amount"])):
    if sort_by not in ["date", "amount"]:
        raise HTTPException(status_code=400, detail="Invalid sort field.Should be either 'date' or 'amount'")
    sorted_records = sort_records(sort_by)
    if not sorted_records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"records": sorted_records}


@app.delete("/records/{record_id}")
def delete_record_by_id(record_id: str = Path(..., description="The unique identifier of the financial record to be deleted")):
    deleted=delete_record(record_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="No records found")
    return {"message": f"Record with id {record_id} has been deleted successfully."}


@app.put("/update/{record_id}")
def update_record_by_id(record_id: str, record: FinancialRecordUpdate):
    updated = update_record(record_id, record.model_dump(exclude_unset=True))

    if not updated:
        raise HTTPException(status_code=404, detail="Record not found")

    return {"message": f"Record with id {record_id} has been updated successfully."}
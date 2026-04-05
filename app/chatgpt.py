from fastapi import FastAPI, Path, Query, HTTPException
from app.schemas import FinancialRecord, FinancialRecordUpdate
from app.database import create_db_table, create_users_table
from app.crud import (
    create_record,
    get_records,
    get_records_date,
    get_records_category,
    get_records_type,
    get_sorted,
    delete,
    update
)

app = FastAPI()


@app.on_event("startup")
def startup():
    create_db_table()
    create_users_table()


@app.get("/")
def root():
    return {"message": "Financial Records Management"}



@app.post("/create")
def create(record: FinancialRecord):
    data = create_record(record)
    return {
        "message": "Record created successfully",
        "record": data
    }



@app.get("/records")
def read_records():
    records = get_records()
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"records": records}



@app.get("/records/date/{date}")
def read_records_by_date(
    date: str = Path(..., description="Format: YYYY-MM-DD", examples=["2026-04-05"])
):
    records = get_records_date(date)
    if not records:
        raise HTTPException(status_code=404, detail="No records found for this date")
    return {"records": records}



@app.get("/records/category/{category}")
def read_records_by_category(category: str):
    records = get_records_category(category)
    if not records:
        raise HTTPException(status_code=404, detail="No records found for this category")
    return {"records": records}


@app.get("/records/type/{record_type}")
def read_records_by_type(record_type: str):
    if record_type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Invalid type.Please provide either 'income' or 'expense'")

    records = get_records_type(record_type)
    if not records:
        raise HTTPException(status_code=404, detail="No records found")

    return {"records": records}


@app.get("/sort")
def read_sorted_records(
    sort_by: str = Query(..., description="date or amount", examples=["date"])
):
    if sort_by not in ["date", "amount"]:
        raise HTTPException(status_code=400, detail="Invalid sort field")

    records = get_sorted(sort_by)
    if not records:
        raise HTTPException(status_code=404, detail="No records found")

    return {"records": records}


@app.delete("/records/{record_id}")
def delete_record_by_id(record_id: str):
    deleted = delete(record_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Record not found")

    return {"message": f"Record {record_id} deleted successfully"}


@app.put("/update/{record_id}")
def update_record_by_id(record_id: str, record: FinancialRecordUpdate):
    updated = update(record_id, record.model_dump(exclude_unset=True))

    if not updated:
        raise HTTPException(status_code=404, detail="Record not found")

    return {"message": f"Record {record_id} updated successfully"}
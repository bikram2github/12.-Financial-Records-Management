import uuid
from app.database import (
    insert_record,
    get_all_records,
    get_records_by_date,
    get_by_category,
    get_by_type,
    sort_records,
    delete_record,
    update_record
)


def create_record(record):
    data = record.model_dump()
    data["tran_id"] = str(uuid.uuid4())

    insert_record(
        data["tran_id"],
        data["amount"],
        data["record_type"],
        data["category"],
        data["note"]
    )

    return data


def get_records():
    return get_all_records()


def get_records_date(date):
    return get_records_by_date(date)


def get_records_category(category):
    return get_by_category(category)


def get_records_type(record_type):
    return get_by_type(record_type)


def get_sorted(sort_by):
    return sort_records(sort_by)


def delete(tran_id):
    return delete_record(tran_id)


def update(tran_id, data):
    return update_record(tran_id, data)
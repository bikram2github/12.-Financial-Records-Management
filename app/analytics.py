import pandas as pd
from database import get_all_records

def show_records():
    data=get_all_records()
    df = pd.DataFrame(data)
    return df


'''data=show_records()
print(data)
'''

def show_summary():
    data=show_records()
    total_income=data[data['record_type']=='income']['amount'].sum()
    total_expense=data[data['record_type']=='expense']['amount'].sum()
    balance=total_income-total_expense
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

def show_category_summary():
    data=show_records()
    category_summary=data.groupby('category')['amount'].sum().to_dict()
    return category_summary




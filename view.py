import pandas as pd
from app.database import get_all_records

def show_records():
    data=get_all_records()
    df = pd.DataFrame(data)
    return df
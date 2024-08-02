import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(left=customers, right=orders,
         left_on='id', right_on='customerId' , how='left')
    return pd.DataFrame({"Customers":
    df[df['customerId'].isna()]['name']})

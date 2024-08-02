import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employee, employee, how='left', left_on = 'managerId', right_on = 'id')

    return pd.DataFrame({'Employee': df[df.salary_x>df.salary_y]['name_x']})
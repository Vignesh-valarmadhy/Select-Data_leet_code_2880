import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to select rows where student_id is 101
    result = students.loc[students['student_id'] == 101, ['name', 'age']]
    return result

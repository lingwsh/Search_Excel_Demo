import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel ('data/IMEX-IN-2016-06-EX.part2.xlsx',engine='openpyxl')
my_conn = create_engine("mysql+mysqldb://wsh:8384810@localhost/Isynet_Test")
df.to_sql('excel_data', con=my_conn)
import pandas as pd
from sqlalchemy import create_engine
  
engine = create_engine('sqlite:///data.db', echo=False)

x = pd.read_excel("D:/Raw Data.xlsx")  

x.to_sql('D:/Project/Python_Tutorial/database_connectivity/slite_databases/data.db', con=engine)

df = pd.read_sql('D:/Project/Python_Tutorial/database_connectivity/slite_databases/data.db', con=engine)
  
df
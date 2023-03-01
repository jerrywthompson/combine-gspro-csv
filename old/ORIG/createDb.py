import pandas as pd
import sqlite3

df = pd.read_csv('GSProCombinedFile.csv')

conn = sqlite3.connect('../database.db')
df.to_sql('results', conn, if_exists='replace', index=False)

conn.close()

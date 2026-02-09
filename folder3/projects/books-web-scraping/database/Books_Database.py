import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("Cleaned_Bookdata.csv")

# Create SQLite database
conn = sqlite3.connect("books.db")

# Save DataFrame to database
df.to_sql("books", conn, if_exists="replace", index=False)

# Verify data
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM books")
count = cursor.fetchone()[0]

print("Total records inserted:", count)

conn.close()

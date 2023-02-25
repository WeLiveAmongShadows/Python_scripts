import pyodbc as DB2
import pandas as pd
from pandas import ExcelWriter
from datetime import date
from tkinter import *
import tkinter as tk
import os

# # Create object
# splash_root = Tk()
 
# # Adjust size
# splash_root.geometry("700x300")
# splash_root.configure(bg= 'green', borderwidth='80')

# # Set Label
# splash_label = tk.Label(splash_root, text="Exporting precounted data\n🖥  ➡➡➡  🌍", font='12')
# splash_label.pack()

# # Execute tkinter
# mainloop()


#Get user name
user_ = os.getlogin()
print(user_)

#Today
today = date.today()
today_ = today.strftime('%m-%d-%Y')
file_name = "Whs 2 Inventory "
today_slash = today.strftime('%m/%d/%Y')
Conn = DB2.connect("DSN=AE_SIMIP23;UID=MISOLO;PWD=MISOLO13")
Cur = Conn.cursor()
MAS_A = f"""
SELECT

   TRIM(SLQNTY.ITNBR) AS "Part Number",
   TRIM(ITEMASA.ITDSC) AS "Item Description",
   TRIM(SLQNTY.HOUSE) AS "Warehouse",
   TRIM(SLQNTY.LLOCN) AS "Location",
   SLQNTY.LQNTY AS "Quantity",
   SLQNTY.LBHNO AS "Batch/Lot",
   SUBSTRING(SLQNTY.FDATE, 4, 2) || '/' || SUBSTRING(SLQNTY.FDATE, 6, 2) || '/20' || SUBSTRING(SLQNTY.FDATE, 2, 2) AS "FIFO date",
   '{today_slash}' as "Date", 
CASE
  WHEN SLQNTY.LBHNO LIKE 'J0%' THEN 'Yes'
  ELSE 'No'
END AS "Pre-count status",
SUBSTRING(TRIM(SLQNTY.LLOCN), 1, 3) AS "Rack"

FROM
   AMFLIBE.SLQNTY SLQNTY
    LEFT OUTER JOIN AMFLIBE.ITEMASA ITEMASA
     ON SLQNTY.ITNBR = ITEMASA.ITNBR

WHERE
  SLQNTY.HOUSE = '2'
  AND ITEMASA.ITDSC NOT LIKE 'MRO%'

"""
rq = pd.read_sql(MAS_A,Conn)
df = pd.DataFrame(rq)

Pre_counted_data = df.to_csv(rf'C:\Users\{user_}\Eaton\CRDS RWD MCB Haina Plant - Documents\Data management\Pre-counted\Data' + f'\Whs 2 Inventory {today_}.csv', index=False)
exit()
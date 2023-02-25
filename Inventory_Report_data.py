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
# splash_label = tk.Label(splash_root, text="Exporting inventory data\n🖥  ➡➡➡  🌍", font='12')
# splash_label.pack()

# # Execute tkinter
# mainloop()


#Get user name
user_ = os.getlogin()
print(user_)

#Today
today = date.today()
today_ = today.strftime('%m-%d-%Y')
file_name = "Inventory Report "
today_slash = today.strftime('%m/%d/%Y')
Conn = DB2.connect("DSN=AE_SIMIP23;UID=MISOLO;PWD=MISOLO13")
Cur = Conn.cursor()
MAS_A = f"""
SELECT 
    CASE
     WHEN SLQNTY.HOUSE = 'H2' THEN 'Hold - Haina'
     WHEN SLQNTY.LLOCN = 'CORE' AND SLQNTY.HOUSE = 'W' THEN 'Core Rework'
     WHEN SLQNTY.LLOCN = 'OTHER' AND SLQNTY.HOUSE = 'W' THEN 'Other Rework'
     WHEN SLQNTY.LLOCN = 'SUPPLY' AND SLQNTY.HOUSE = 'W' THEN 'SUPPLY'
     WHEN SLQNTY.LLOCN = '2ASORT' AND SLQNTY.HOUSE = '2' THEN 'RWSORT'
     WHEN SLQNTY.LLOCN = '2APPAP' AND SLQNTY.HOUSE = 'W' THEN 'PPAP'
     WHEN SLQNTY.HOUSE = 'W' AND SLQNTY.LLOCN NOT IN ('SUPPLY','OTHER','CORE','2APPAP') THEN 'Rework - Haina'
      ELSE 'Other invetory group' 
    END AS "Inventory block",
	TRIM(SLQNTY.HOUSE) AS "Whs",
	TRIM(SLQNTY.LLOCN) AS "Location",
	TRIM(SLQNTY.ITNBR) AS "Item number",
	TRIM(M_ICSWB1.IDESC) AS "Item description",
	SLQNTY.LQNTY AS "Qty",
	ROUND( SLQNTY.LQNTY * M_ICSWB1.MAT, 2 ) AS "Material cost",
    ROUND( SLQNTY.LQNTY * M_ICSWB1.TOTAL, 2 ) AS "Total cost",
	ITEMASA.ITTYP AS "Item type",
	ITEMBL.ITCLS AS "Item class",
    SLQNTY.LBHNO AS "Batch/lot number",
    SUBSTRING(SLQNTY.FDATE, 4, 2) || '/' || SUBSTRING(SLQNTY.FDATE, 6, 2) || '/20' || SUBSTRING(SLQNTY.FDATE, 2, 2) AS "FIFO date",
   '{today_slash}' as "Date"

FROM 
	AMFLIBE.SLQNTY SLQNTY
	LEFT OUTER JOIN AMFLIBE.ITEMBL ITEMBL
	ON 
		SLQNTY.ITNBR = ITEMBL.ITNBR AND
		SLQNTY.HOUSE = ITEMBL.HOUSE
	LEFT OUTER JOIN LCLDTAAE.ICSWB1 M_ICSWB1
	ON 
		SLQNTY.ITNBR = M_ICSWB1.STYLE
	LEFT OUTER JOIN AMFLIBE.ITEMASA ITEMASA
	ON 
		SLQNTY.ITNBR = ITEMASA.ITNBR
	LEFT OUTER JOIN AMFLIBE.ITEMASB ITEMASB
	ON 
		ITEMASA.ITNBR = ITEMASB.ITNBR
	 
WHERE 
	NOT ITTYP = '9'
	AND SLQNTY.HOUSE IN ('H2','W','2') 
  AND M_ICSWB1.IDESC NOT LIKE 'MRO%'
ORDER BY 
	2, 
	4

"""
rq = pd.read_sql(MAS_A,Conn)
df = pd.DataFrame(rq)

Pre_counted_data = df.to_csv(rf'C:\Users\{user_}\Eaton\CRDS RWD MCB Haina Plant - Documents\Data management\Inventory Report\Data' + f'\Inventory Report {today_}.csv', index=False)
exit()
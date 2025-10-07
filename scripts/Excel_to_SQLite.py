import pandas as pd
import sqlite3

# 1. Charger le fichier Excel
df = pd.read_excel("owid-energy-data.xlsx", sheet_name="Data")

# 2. Connexion / création de la base SQLite
conn = sqlite3.connect("/Users/gillesperruche/PythonProjects/MonPremierProjet/Base_SQL_Projet_Energie.db")

# 3. Importer le DataFrame dans SQLite
df.to_sql("ma_table", conn, if_exists="replace", index=False)

# 4. Fermer la connexion
conn.close()
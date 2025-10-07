import sqlite3
import pandas as pd

# Connexion à la base SQLite
conn = sqlite3.connect("Base_SQL_Projet_Energie.db")

# Requête SQL (modifie selon ton besoin)
query = """
WITH base AS (SELECT *
FROM ma_table m

WHERE country IN ('Austria', 'Belgium', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Slovakia', 'Slovenia',
'Spain', 'Sweden', 'Switzerland', 'Turkey', 'United Kingdom')

)

-- Les différents types d'énergies : fossil, nucleaire & renouvelable -> Check des données OK
SELECT country, year, fossil_fuel_consumption, fossil_share_energy,
nuclear_consumption, nuclear_share_energy, 
renewables_consumption, renewables_share_energy,
gas_consumption, gas_share_energy

FROM base
WHERE year > 1999
GROUP BY country, year
ORDER BY country, year ASC
"""

# Charger le résultat dans un DataFrame
df = pd.read_sql_query(query, conn)

# Exporter en Excel
df.to_excel("energie_transfo_01.xlsx", index=False)

# Fermer la connexion
conn.close()

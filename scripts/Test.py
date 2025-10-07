from tableauhyperapi import HyperProcess, Telemetry, Connection

input_tde = "/Users/gillesperruche/Documents/Mon_dossier_Tableau/Workbooks/getting_started_with_calculations/Data/Global_Superstore_2016.twb_Files/excel-direct.0olym3o0bydvm91ed3uil1hx3lp2.tde"

with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
    with Connection(endpoint=hyper.endpoint, database=input_tde) as connection:
        print("Connexion au TDE réussie")
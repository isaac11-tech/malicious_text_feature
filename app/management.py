from app.connection_db import ConnectionDB


class Management:

    iranmaldb = ConnectionDB("IranMalDB","tweets")
    df = iranmaldb.collection_to_df()




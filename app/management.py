from app.connection_db import ConnectionDB
from app.data_processing import DataProcessing


class Management:

    iranmaldb = ConnectionDB("IranMalDB","tweets")

    #print(iranmaldb.get_all_documents())

    df = iranmaldb.collection_to_df()
    print(df)

    processing = DataProcessing(df)

    processing.create_rate_word()

    processing.create_rate_word()





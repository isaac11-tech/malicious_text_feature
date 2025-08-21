from app.connection_db import ConnectionDB
from app.data_processing import DataProcessing


class Management:

    def __init__(self):
        #connction to the DB
        self.iranmaldb = ConnectionDB("IranMalDB", "tweets")
        #convert to df
        self.df = self.iranmaldb.collection_to_df()
        #creat object of DataProcessing
        self.processing = DataProcessing(self.df)
        #processing the df and add col of rate_word
        self.processing.create_rate_word()
        #processing the df and add col of weapon
        self.processing.create_weapon()
        #processing the df and add col of sentiment
        self.processing.create_sentiment()


    #return the data processed
    def get_data_processed(self):
        return self.df














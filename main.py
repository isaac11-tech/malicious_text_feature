from app.connection_db import ConnectionDB

#c = ConnectionDB("IranMalDB","tweets")

#df = c.collection_to_df()

with open("data/weapon_list.txt", "r", encoding="utf-8") as f:
    black_list = [line.strip() for line in f.readlines()]
    print(type(black_list[0]))




from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean


metadata = MetaData()

tour = Table(
    "tour", 
    metadata, 
    Column("id", Integer, primary_key=True),
    Column("tour_name", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("user_name", String, nullable= False),
)
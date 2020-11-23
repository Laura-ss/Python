import pandas
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://usuariodb:abc@192.168.56.12:5432/municipios')

print()
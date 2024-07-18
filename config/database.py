import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session  import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#nombre variable = (../ para que cree el archivo en la carpeta madre)nombre base de datos 
sqlite_file_name = "../database.sqlite"
#para que lea el directorio actual(__file__)
base_dir = os.path.dirname(os.path.realpath(__file__))

# creaar la url de mi base de datos uniendo mi base de datos con sqlite
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#variable para representar la base de datos(mi url, echo para mostrar por consola lo ue se esta haciendo)
engine = create_engine(database_url, echo=True)

# crear la secion para conectarme ala base de datos y lo enlsao al motor de la base de datos (bind=engine)
Session = sessionmaker(bind=engine)

Base = declarative_base ()
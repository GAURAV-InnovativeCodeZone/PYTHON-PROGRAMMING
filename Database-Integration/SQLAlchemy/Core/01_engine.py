# ==============================================================
#                      SQLALCHEMY ENGINE
#
# Engine → SQLAlchemy's central database connectivity object
# Engine manages database connectivity, dialect and connections
#
# create_engine() → Creates a SQLAlchemy Engine
#
# ==============================================================


from sqlalchemy import create_engine


# SQLite Database URL

DATABASE_URL = "sqlite:///example.db"


# Create Engine

engine = create_engine(
    DATABASE_URL
)


print("Engine created successfully")
print(engine)

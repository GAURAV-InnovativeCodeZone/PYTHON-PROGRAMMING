# ============================================================
#                      CONNECTION
#
# Connection → Represents an active database connection
# engine.connect() → Obtains a connection from the Engine
# execute() → Executes a SQL statement through the connection
# scalar() → Returns the first column of the first row
# Context manager → Automatically releases the connection
# ============================================================


# -----------------------------------------------------------------------------------------
# way 1 (recommended) -  Automatic Connection Close - use context manager - with statement
# -----------------------------------------------------------------------------------------

from sqlalchemy import create_engine, text

# SQLite Database URL

DATABASE_URL = "sqlite:///G:/GAURAV PANWAR/CODING/PYTHON-PROGRAMMING/Database-Integration/SQLAlchemy/Core/example.db"

# Create Engine

engine = create_engine(DATABASE_URL)

# Create Connection and Execute SQL

with engine.connect() as connection:

    result = connection.execute(text("SELECT 1"))

    print(result.scalar())



# # --------------------------------------------
# # way 2 - Manual Connection Close
# # --------------------------------------------

# from sqlalchemy import create_engine, text

# # SQLite Database URL

# DATABASE_URL = "sqlite:///SQLAlchemy/Core/example.db"

# # Create Engine

# engine = create_engine(DATABASE_URL)

# # Create Connection and Execute SQL

# connection = engine.connect()

# result = connection.execute(
#     text("SELECT 1")
# )

# print(result.scalar())

# connection.close()


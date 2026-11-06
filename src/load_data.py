import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from getpass import getpass
from urllib.parse import quote_plus

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# PostgreSQL details
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "recruitment_analysis"

# Ask for password without displaying it
DB_PASSWORD = getpass("Enter your PostgreSQL password: ")

# Create database connection
encoded_password = quote_plus(DB_PASSWORD)

connection_string = (
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(connection_string)

# Tables must be loaded in this order because of foreign keys
tables = [
    "sources",
    "recruiters",
    "jobs",
    "candidates",
    "applications",
    "interviews",
    "offers",
    "hires",
]

print("\nStarting data import...\n")

for table in tables:
    file_path = DATA_DIR / f"{table}.csv"

    print(f"Loading {file_path.name} → {table}")

    df = pd.read_csv(file_path)

    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False,
    )

    print(f"✓ {len(df)} rows inserted into {table}\n")

print("================================")
print("DATA IMPORT COMPLETED SUCCESSFULLY")
print("================================")
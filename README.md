# Setup

Create and activate the virtual environment, then install the project dependencies.

### 1. Create virtual environment
python -m venv .venv

### 2. Activate virtual environment
 Windows:
 
 .venv\Scripts\activate
 
 macOS/Linux:
 
 
source .venv/bin/activate

### 3. Install dependencies and local package
uv pip install -r requirements.txt



# Run ETL
### Run the ETL script to process raw data and generate the analytics tables.

Mac / Liux

PYTHONPATH=src uv run ./scripts/run_etl.py

Windows

set PYTHONPATH=src && python scripts/run_etl.py

# Outputs
### After running the ETL script, the following files will be generated in the

data/processed/ directory:

data/processed/orders_clean.parquet

data/processed/users.parquet

data/processed/analytics_table.parquet

data/processed/_run_meta.json

 # EDA
To view the analysis and generate figures:

Ensure the ETL script has been executed successfully.

Open the notebook notebooks/eda.ipynb.

Run all cells to produce charts in reports/figures/.

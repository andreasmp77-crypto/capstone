'''
W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-31
'''

import pandas as pd
from pathlib import Path

# Get the directory where this script is located
DATA_DIR = Path(__file__).resolve().parent

# Define the raw data directory
RAW_DATA_DIR = DATA_DIR / "raw"

EUROCONTROL_FILE = RAW_DATA_DIR / "All_Pre-Departure_Delay.xlsx"

SEAFARERS_2015_FILE = (
    RAW_DATA_DIR / "2015 US.Seafarers_20260831_120803.csv"
)

SEAFARERS_2021_FILE = (
    RAW_DATA_DIR / "2021 US.Seafarers_20260831_111621.csv"
)

CREW_CHANGE_FILE = (
    RAW_DATA_DIR / "synthetic_crew_change_plans.csv"
)


def inspect_dataframe(df, dataset_name):
    """
    Print a standard data quality summary for a DataFrame.
    """

    print("\n" + "=" * 70)
    print(f"DATASET: {dataset_name}")
    print("=" * 70)

    # Shape
    print("\n1. SHAPE")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")

    # Columns
    print("\n2. COLUMN NAMES")
    print(df.columns.tolist())

    # Data types
    print("\n3. DATA TYPES")
    print(df.dtypes)

    # Sample
    print("\n4. FIRST 5 ROWS")
    print(df.head())

    # Missing values
    print("\n5. MISSING VALUES")
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)

    if missing.empty:
        print("No missing values found.")
    else:
        print(missing)

    # Duplicates
    print("\n6. DUPLICATE ROWS")
    print(f"Duplicate rows: {df.duplicated().sum():,}")

    # Unique values
    print("\n7. UNIQUE VALUES PER COLUMN")
    print(df.nunique().sort_values())


def inspect_excel_sheets(file_path):
    """
    Display the sheet names in an Excel workbook.
    """
    try:
        excel_file = pd.ExcelFile(file_path)
    except ImportError as exc:
        print("\n" + "=" * 70)
        print("EXCEL WORKBOOK SHEETS")
        print("=" * 70)
        print(f"Skipping Excel inspection: {exc}")
        return

    print("\n" + "=" * 70)
    print("EXCEL WORKBOOK SHEETS")
    print("=" * 70)
    print(excel_file.sheet_names)


def main():
    print("\n" + "#" * 70)
    print("CAPSTONE ROUND 1 - DATA INSPECTION")
    print("#" * 70)

    print(f"\nData directory: {DATA_DIR}")
    print(f"Raw data directory: {RAW_DATA_DIR}")

    files_to_check = [
        EUROCONTROL_FILE,
        SEAFARERS_2015_FILE,
        SEAFARERS_2021_FILE,
        CREW_CHANGE_FILE,
    ]

    print("\nFILE AVAILABILITY CHECK")
    for file in files_to_check:
        if file.exists():
            print(f"Found: {file.name}")
        else:
            print(f"NOT FOUND: {file.name}")

    # ==============================================
    # DATASET 1: EUROCONTROL AIRPORT DELAYS
    # ==============================================
    inspect_excel_sheets(EUROCONTROL_FILE)

    try:
        eurocontrol_df = pd.read_excel(
            EUROCONTROL_FILE,
            sheet_name="DATA",
        )
    except ImportError as exc:
        print(f"\nSkipping EUROCONTROL data load: {exc}")
        eurocontrol_df = None

    if eurocontrol_df is not None:
        inspect_dataframe(
            eurocontrol_df,
            "EUROCONTROL - All Pre-Departure Delay",
        )

        print("\nEUROCONTROL SPECIFIC CHECKS")
        print("\nDate range:")
        print(
            eurocontrol_df["FLT_DATE"].min(),
            "to",
            eurocontrol_df["FLT_DATE"].max(),
        )
        print("\nNumber of airports:")
        print(eurocontrol_df["APT_ICAO"].nunique())

    # ==============================================
    # DATASET 2A: UNCTAD SEAFARERS - 2015
    # ==============================================
    seafarers_2015_df = pd.read_csv(SEAFARERS_2015_FILE)

    inspect_dataframe(
        seafarers_2015_df,
        "UNCTAD Seafarers - 2015",
    )

    # ==============================================
    # DATASET 2B: UNCTAD SEAFARERS - 2021
    # ==============================================
    seafarers_2021_df = pd.read_csv(SEAFARERS_2021_FILE)

    inspect_dataframe(
        seafarers_2021_df,
        "UNCTAD Seafarers - 2021",
    )

    print("\n" + "=" * 70)
    print("UNCTAD 2015 vs 2021 COMPARISON")
    print("=" * 70)

    columns_2015 = set(seafarers_2015_df.columns)
    columns_2021 = set(seafarers_2021_df.columns)

    print("\nColumns only in 2015:")
    print(columns_2015 - columns_2021)

    print("\nColumns only in 2021:")
    print(columns_2021 - columns_2015)

    print("\nCommon columns:")
    print(columns_2015 & columns_2021)

    economies_2015 = set(seafarers_2015_df["Economy_Label"])
    economies_2021 = set(seafarers_2021_df["Economy_Label"])

    print("\nEconomies only in 2015:")
    print(sorted(economies_2015 - economies_2021))

    print("\nEconomies only in 2021:")
    print(sorted(economies_2021 - economies_2015))

    # ==============================================
    # DATASET 3: SYNTHETIC CREW CHANGE PLANS
    # ==============================================
    crew_change_df = pd.read_csv(CREW_CHANGE_FILE)

    inspect_dataframe(
        crew_change_df,
        "Synthetic Crew Change Plans",
    )

    print("\nSYNTHETIC CREW CHANGE SPECIFIC CHECKS")
    print("\nUnique Crew Change IDs:")
    print(crew_change_df["crew_change_id"].nunique())

    print("\nRisk Level Distribution:")
    print(crew_change_df["risk_level"].value_counts())


if __name__ == "__main__":
    main()

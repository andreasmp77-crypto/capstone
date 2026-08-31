'''
W8D5_Project_5_Capstone
- Week 8 / Day 5
- Student: Andreas Papachristophorou
- Course: AI Consulting & Integration 2026-07
- Date: 2026-08-31
'''

import pandas as pd
from pathlib import Path


# ============================================================
# PATH CONFIGURATION
# ============================================================

# Get the directory where this script is located.
# This should point to the project's /data folder.
DATA_DIR = Path(__file__).resolve().parent

# Define the location of the original source files.
RAW_DATA_DIR = DATA_DIR / "raw"

# Define where the cleaned Tableau-ready files will be saved.
CLEAN_DATA_DIR = DATA_DIR / "clean"

# Create the clean folder automatically if it does not exist.
CLEAN_DATA_DIR.mkdir(exist_ok=True)


# ============================================================
# INPUT FILE PATHS
# ============================================================

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


# ============================================================
# OUTPUT FILE PATHS
# ============================================================

EUROCONTROL_OUTPUT = (
    CLEAN_DATA_DIR / "eurocontrol_delays_clean.csv"
)

SEAFARERS_OUTPUT = (
    CLEAN_DATA_DIR / "unctad_seafarers_clean.csv"
)

CREW_CHANGE_OUTPUT = (
    CLEAN_DATA_DIR / "synthetic_crew_change_plans_clean.csv"
)


# ============================================================
# HELPER FUNCTION
# ============================================================

def print_cleaning_summary(dataset_name, original_rows, cleaned_rows):
    """
    Print a simple summary showing how many rows were retained
    after cleaning.
    """

    rows_removed = original_rows - cleaned_rows

    print("\n" + "=" * 70)
    print(f"CLEANING SUMMARY: {dataset_name}")
    print("=" * 70)
    print(f"Original rows: {original_rows:,}")
    print(f"Cleaned rows:  {cleaned_rows:,}")
    print(f"Rows removed:  {rows_removed:,}")


# ============================================================
# DATASET 1: EUROCONTROL AIRPORT DELAY DATA
# ============================================================

def clean_eurocontrol():
    """
    Clean EUROCONTROL airport delay data for Tableau analysis.

    Cleaning decisions:
    - Convert date column to datetime
    - Remove exact duplicate rows
    - Keep only rows with valid flight and delay data
    - Keep only rows where IFR departures are greater than zero
    - Rename columns to clearer Tableau-friendly names

    Important:
    We do NOT replace missing delay or flight values with zero.
    Missing data means 'unknown', not 'zero delay'.
    """

    print("\n" + "#" * 70)
    print("CLEANING DATASET 1: EUROCONTROL AIRPORT DELAYS")
    print("#" * 70)

    # Load the DATA sheet from the Excel workbook.
    df = pd.read_excel(
        EUROCONTROL_FILE,
        sheet_name="DATA"
    )

    original_rows = len(df)

    print(f"\nOriginal rows: {original_rows:,}")

    # --------------------------------------------------------
    # 1. Remove exact duplicate rows
    # --------------------------------------------------------

    duplicates = df.duplicated().sum()
    print(f"Exact duplicate rows found: {duplicates:,}")

    df = df.drop_duplicates()

    # --------------------------------------------------------
    # 2. Convert the flight date to a proper datetime format
    # --------------------------------------------------------

    df["FLT_DATE"] = pd.to_datetime(
        df["FLT_DATE"],
        errors="coerce"
    )

    # --------------------------------------------------------
    # 3. Remove rows where the date could not be interpreted
    # --------------------------------------------------------

    invalid_dates = df["FLT_DATE"].isna().sum()
    print(f"Invalid or missing dates: {invalid_dates:,}")

    df = df.dropna(subset=["FLT_DATE"])

    # --------------------------------------------------------
    # 4. Keep only rows with valid operational data
    # --------------------------------------------------------

    # Our key Tableau metric will be based on:
    #
    # SUM(total delay minutes)
    # ----------------------
    # SUM(IFR departures)
    #
    # Therefore, rows missing either value cannot contribute
    # meaningfully to this calculation.
    #
    # We deliberately DO NOT replace missing values with zero.
    df = df.dropna(
        subset=[
            "FLT_DEP_IFR_2",
            "DLY_ALL_PRE_2"
        ]
    )

    # --------------------------------------------------------
    # 5. Remove rows where IFR departures are zero or negative
    # --------------------------------------------------------

    # A zero denominator would make the delay-per-flight metric
    # invalid or meaningless.
    df = df[
        df["FLT_DEP_IFR_2"] > 0
    ]

    # --------------------------------------------------------
    # 6. Remove negative delay values, if any exist
    # --------------------------------------------------------

    # Negative total delay minutes would not make business sense
    # for this use case.
    df = df[
        df["DLY_ALL_PRE_2"] >= 0
    ]

    # --------------------------------------------------------
    # 7. Add useful time dimensions for Tableau
    # --------------------------------------------------------

    # These fields make filtering and trend analysis easier
    # without changing the original date information.
    df["Year"] = df["FLT_DATE"].dt.year
    df["Month"] = df["FLT_DATE"].dt.month
    df["Month_Name"] = df["FLT_DATE"].dt.month_name()
    df["Year_Month"] = df["FLT_DATE"].dt.to_period("M").astype(str)

    # --------------------------------------------------------
    # 8. Rename important columns
    # --------------------------------------------------------

    # We keep the dataset easier to understand in Tableau by
    # using clear business-friendly column names.
    df = df.rename(
        columns={
            "FLT_DATE": "Flight_Date",
            "APT_ICAO": "Airport_ICAO",
            "APT_NAME": "Airport_Name",
            "STATE_NAME": "Country",
            "FLT_DEP_IFR_2": "IFR_Departures",
            "DLY_ALL_PRE_2": "Total_Delay_Minutes"
        }
    )

    # --------------------------------------------------------
    # 9. Keep relevant columns for the dashboard
    # --------------------------------------------------------

    # We select only the fields needed for the intended analysis.
    # This creates a cleaner Tableau dataset.
    columns_to_keep = [
        "Flight_Date",
        "Year",
        "Month",
        "Month_Name",
        "Year_Month",
        "Airport_ICAO",
        "Airport_Name",
        "Country",
        "IFR_Departures",
        "Total_Delay_Minutes"
    ]

    df = df[columns_to_keep]

    # --------------------------------------------------------
    # 10. Sort the dataset
    # --------------------------------------------------------

    df = df.sort_values(
        by=[
            "Flight_Date",
            "Airport_ICAO"
        ]
    )

    # --------------------------------------------------------
    # 11. Save cleaned dataset
    # --------------------------------------------------------

    df.to_csv(
        EUROCONTROL_OUTPUT,
        index=False
    )

    print_cleaning_summary(
        "EUROCONTROL AIRPORT DELAYS",
        original_rows,
        len(df)
    )

    print(f"\nSaved cleaned file to:")
    print(EUROCONTROL_OUTPUT)

    return df


# ============================================================
# DATASET 2: UNCTAD SEAFARERS
# ============================================================

def clean_seafarers():
    """
    Clean and combine UNCTAD seafarer datasets from 2015 and 2021.

    Cleaning decisions:
    - Add an explicit Year column to each dataset
    - Remove completely empty columns
    - Keep relevant analysis columns
    - Standardise column names
    - Combine both years into one dataset

    Final structure:
    Economy | Seafarer_Type | Seafarer_Count | World_Share_Percent | Year

    This "long format" structure is particularly suitable for
    Tableau because Year can be used as a filter or time dimension.
    """

    print("\n" + "#" * 70)
    print("CLEANING DATASET 2: UNCTAD SEAFARERS")
    print("#" * 70)

    # --------------------------------------------------------
    # 1. Load both datasets
    # --------------------------------------------------------

    df_2015 = pd.read_csv(SEAFARERS_2015_FILE)
    df_2021 = pd.read_csv(SEAFARERS_2021_FILE)

    original_rows_2015 = len(df_2015)
    original_rows_2021 = len(df_2021)

    print(f"\n2015 original rows: {original_rows_2015:,}")
    print(f"2021 original rows: {original_rows_2021:,}")

    # --------------------------------------------------------
    # 2. Add the year explicitly
    # --------------------------------------------------------

    # The raw files themselves do not contain a Year column.
    # We know the reporting year from the source file being used,
    # so we explicitly label each dataset before combining them.
    df_2015["Year"] = 2015
    df_2021["Year"] = 2021

    # --------------------------------------------------------
    # 3. Combine the two datasets
    # --------------------------------------------------------

    # pd.concat() stacks the datasets vertically.
    #
    # Think of it like placing the 2015 spreadsheet on top of
    # the 2021 spreadsheet while keeping the column structure.
    df = pd.concat(
        [df_2015, df_2021],
        ignore_index=True
    )

    original_combined_rows = len(df)

    # --------------------------------------------------------
    # 4. Remove exact duplicate rows
    # --------------------------------------------------------

    duplicates = df.duplicated().sum()
    print(f"Exact duplicate rows found: {duplicates:,}")

    df = df.drop_duplicates()

    # --------------------------------------------------------
    # 5. Keep only columns relevant to our analysis
    # --------------------------------------------------------

    columns_to_keep = [
        "Economy_Label",
        "SeafarerType_Label",
        "Absolute_value_Value",
        "Percentage_of_total_world_Value",
        "Year"
    ]

    df = df[columns_to_keep]

    # --------------------------------------------------------
    # 6. Rename columns to Tableau-friendly names
    # --------------------------------------------------------

    df = df.rename(
        columns={
            "Economy_Label": "Economy",
            "SeafarerType_Label": "Seafarer_Type",
            "Absolute_value_Value": "Seafarer_Count",
            "Percentage_of_total_world_Value": "World_Share_Percent"
        }
    )

    # --------------------------------------------------------
    # 7. Clean text fields
    # --------------------------------------------------------

    # Strip removes accidental spaces before or after text.
    df["Economy"] = (
        df["Economy"]
        .astype("string")
        .str.strip()
    )

    df["Seafarer_Type"] = (
        df["Seafarer_Type"]
        .astype("string")
        .str.strip()
    )

    # --------------------------------------------------------
    # 8. Ensure numerical columns are numeric
    # --------------------------------------------------------

    df["Seafarer_Count"] = pd.to_numeric(
        df["Seafarer_Count"],
        errors="coerce"
    )

    df["World_Share_Percent"] = pd.to_numeric(
        df["World_Share_Percent"],
        errors="coerce"
    )

    # --------------------------------------------------------
    # 9. Remove rows missing essential information
    # --------------------------------------------------------

    # A row without an economy, seafarer type, or count cannot
    # be meaningfully analysed in Tableau.
    df = df.dropna(
        subset=[
            "Economy",
            "Seafarer_Type",
            "Seafarer_Count"
        ]
    )

    # --------------------------------------------------------
    # 10. Remove impossible negative counts
    # --------------------------------------------------------

    df = df[
        df["Seafarer_Count"] >= 0
    ]

    # --------------------------------------------------------
    # 11. Sort the dataset
    # --------------------------------------------------------

    df = df.sort_values(
        by=[
            "Year",
            "Economy",
            "Seafarer_Type"
        ]
    )

    # --------------------------------------------------------
    # 12. Save cleaned dataset
    # --------------------------------------------------------

    df.to_csv(
        SEAFARERS_OUTPUT,
        index=False
    )

    print_cleaning_summary(
        "UNCTAD SEAFARERS",
        original_combined_rows,
        len(df)
    )

    print("\nYears included:")
    print(sorted(df["Year"].unique()))

    print("\nSeafarer types:")
    print(df["Seafarer_Type"].unique())

    print(f"\nSaved cleaned file to:")
    print(SEAFARERS_OUTPUT)

    return df


# ============================================================
# DATASET 3: SYNTHETIC CREW CHANGE PLANS
# ============================================================

def clean_crew_change():
    """
    Clean the synthetic crew-change planning dataset.

    Cleaning decisions:
    - Remove exact duplicates
    - Convert date columns to datetime
    - Remove rows without a unique crew_change_id
    - Preserve missing connection data because it may mean
      'no connection required', rather than 'unknown'
    - Remove completely empty columns

    Important:
    This dataset remains clearly identified as SYNTHETIC.
    No values should be presented as real industry statistics.
    """

    print("\n" + "#" * 70)
    print("CLEANING DATASET 3: SYNTHETIC CREW CHANGE PLANS")
    print("#" * 70)

    # --------------------------------------------------------
    # 1. Load dataset
    # --------------------------------------------------------

    df = pd.read_csv(CREW_CHANGE_FILE)

    original_rows = len(df)

    print(f"\nOriginal rows: {original_rows:,}")

    # --------------------------------------------------------
    # 2. Remove completely empty columns
    # --------------------------------------------------------

    # Some columns may contain no values at all.
    # Keeping them provides no value to Tableau and can create
    # unnecessary confusion.
    empty_columns = [
        column
        for column in df.columns
        if df[column].isna().all()
    ]

    if empty_columns:
        print("\nCompletely empty columns removed:")
        print(empty_columns)

        df = df.drop(
            columns=empty_columns
        )

    # --------------------------------------------------------
    # 3. Remove exact duplicate rows
    # --------------------------------------------------------

    duplicates = df.duplicated().sum()

    print(
        f"\nExact duplicate rows found: {duplicates:,}"
    )

    df = df.drop_duplicates()

    # --------------------------------------------------------
    # 4. Remove rows without a crew change ID
    # --------------------------------------------------------

    # crew_change_id acts as the unique identifier for each plan.
    df = df.dropna(
        subset=["crew_change_id"]
    )

    # --------------------------------------------------------
    # 5. Check for duplicate crew change IDs
    # --------------------------------------------------------

    duplicate_ids = df["crew_change_id"].duplicated().sum()

    print(
        f"Duplicate crew_change_id values: {duplicate_ids:,}"
    )

    # We do not automatically delete duplicate IDs here because
    # duplicates could represent a legitimate business situation.
    # Instead, we only report them for transparency.

    # --------------------------------------------------------
    # 6. Convert date columns
    # --------------------------------------------------------

    # Only convert columns that actually exist in the dataset.
    # This makes the script slightly more robust.
    date_columns = [
        "plan_created_date",
        "scheduled_departure",
        "scheduled_arrival",
        "vessel_eta",
        "reporting_deadline"
    ]

    for column in date_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    # --------------------------------------------------------
    # 7. Clean text columns
    # --------------------------------------------------------

    # Strip leading/trailing spaces from text values.
    # We loop through object/string columns automatically
    # rather than manually listing every text column.
    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:

        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
        )

    # --------------------------------------------------------
    # 8. Validate risk score if the column exists
    # --------------------------------------------------------

    if "risk_score" in df.columns:

        df["risk_score"] = pd.to_numeric(
            df["risk_score"],
            errors="coerce"
        )

    # --------------------------------------------------------
    # 9. Preserve missing connection information
    # --------------------------------------------------------

    # IMPORTANT:
    #
    # We intentionally do NOT replace missing connection_airport
    # values with "Unknown".
    #
    # A missing connection airport may mean there was no
    # connecting flight at all, which is different from not
    # knowing the connection airport.

    # --------------------------------------------------------
    # 10. Sort dataset if a creation date exists
    # --------------------------------------------------------

    if "plan_created_date" in df.columns:

        df = df.sort_values(
            by="plan_created_date"
        )

    # --------------------------------------------------------
    # 11. Save cleaned dataset
    # --------------------------------------------------------

    df.to_csv(
        CREW_CHANGE_OUTPUT,
        index=False
    )

    print_cleaning_summary(
        "SYNTHETIC CREW CHANGE PLANS",
        original_rows,
        len(df)
    )

    # Display the risk distribution if available.
    if "risk_level" in df.columns:

        print("\nRisk level distribution:")

        print(
            df["risk_level"]
            .value_counts(dropna=False)
        )

    print(f"\nSaved cleaned file to:")
    print(CREW_CHANGE_OUTPUT)

    return df


# ============================================================
# MAIN FUNCTION
# ============================================================

def main():
    """
    Run the complete cleaning pipeline.
    """

    print("\n" + "#" * 70)
    print("CAPSTONE ROUND 1 - DATA CLEANING PIPELINE")
    print("#" * 70)

    print(f"\nRaw data directory:")
    print(RAW_DATA_DIR)

    print(f"\nClean data directory:")
    print(CLEAN_DATA_DIR)

    # --------------------------------------------------------
    # Check that all required input files exist before starting.
    # --------------------------------------------------------

    required_files = [
        EUROCONTROL_FILE,
        SEAFARERS_2015_FILE,
        SEAFARERS_2021_FILE,
        CREW_CHANGE_FILE
    ]

    missing_files = []

    for file in required_files:

        if not file.exists():

            missing_files.append(file)

    # Stop the program early if files are missing.
    if missing_files:

        print("\nERROR: The following required files were not found:")

        for file in missing_files:

            print(f"- {file}")

        return

    # --------------------------------------------------------
    # Run the cleaning functions
    # --------------------------------------------------------

    clean_eurocontrol()

    clean_seafarers()

    clean_crew_change()

    # --------------------------------------------------------
    # Final confirmation
    # --------------------------------------------------------

    print("\n" + "#" * 70)
    print("DATA CLEANING COMPLETED SUCCESSFULLY")
    print("#" * 70)

    print("\nClean files created:")

    for file in CLEAN_DATA_DIR.glob("*.csv"):

        print(f"- {file.name}")


# ============================================================
# RUN THE SCRIPT
# ============================================================

if __name__ == "__main__":
    main()
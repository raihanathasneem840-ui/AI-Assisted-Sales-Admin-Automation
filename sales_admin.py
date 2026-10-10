from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "sales_admin_records.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

REQUIRED_COLUMNS = [
    "RecordID", "AccountName", "ContactName", "Email",
    "MeetingDate", "OpportunityAmount", "MeetingNotes"
]

def main():
    df = pd.read_csv(INPUT_FILE, dtype={"RecordID": "string"})

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {missing_columns}")

    issues = []

    for index, row in df.iterrows():
        record_id = str(row["RecordID"])
        csv_row = index + 2  # header is row 1

        if pd.isna(row["AccountName"]) or not str(row["AccountName"]).strip():
            issues.append([record_id, csv_row, "Missing account name",
                           "High", "Request the correct account name"])

        email = "" if pd.isna(row["Email"]) else str(row["Email"]).strip()
        if not email:
            issues.append([record_id, csv_row, "Missing email",
                           "Medium", "Request the contact email"])
        elif "@" not in email or "." not in email.split("@")[-1]:
            issues.append([record_id, csv_row, "Email format needs review",
                           "Medium", "Verify email with the source"])

        amount = pd.to_numeric(row["OpportunityAmount"], errors="coerce")
        if pd.isna(amount):
            issues.append([record_id, csv_row, "Amount is not numeric",
                           "High", "Check the source value"])
        elif amount < 0:
            issues.append([record_id, csv_row, "Negative amount",
                           "High", "Confirm intended amount; do not guess"])

        parsed_date = pd.to_datetime(row["MeetingDate"], errors="coerce")
        if pd.isna(parsed_date):
            issues.append([record_id, csv_row, "Invalid meeting date",
                           "Medium", "Confirm date with the record owner"])

    duplicate_mask = df["RecordID"].duplicated(keep=False)
    for index in df.index[duplicate_mask]:
        issues.append([
            str(df.loc[index, "RecordID"]), index + 2,
            "Duplicate RecordID", "High",
            "Check whether duplicate or ID-entry error"
        ])

    report_columns = [
        "RecordID", "CSVRow", "IssueType", "Severity", "SuggestedNextStep"
    ]
    report = pd.DataFrame(issues, columns=report_columns)
    report.to_csv(OUTPUT_DIR / "exception_report.csv", index=False)

    df["MeetingDateParsed"] = pd.to_datetime(df["MeetingDate"], errors="coerce")
    df.to_csv(OUTPUT_DIR / "records_review_copy.csv", index=False)

    print(f"Read {len(df)} records.")
    print(f"Found {len(report)} issues.")
    print(f"Exception report: {OUTPUT_DIR / 'exception_report.csv'}")

if __name__ == "__main__":
    main()

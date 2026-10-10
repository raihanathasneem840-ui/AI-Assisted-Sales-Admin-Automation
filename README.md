# AI-Assisted Sales Admin Automation

## Project Overview

This beginner-level Revenue Operations project demonstrates how Python and AI can support sales administration through automated data-quality checks and AI-assisted text tasks.

## Business Problem

Sales administration records can contain missing information, duplicate IDs, invalid dates, incorrectly formatted emails, and unusual opportunity amounts. Manual checking can be repetitive and time-consuming.

## Tools Used

- Python
- pandas
- CSV files
- Excel
- ChatGPT for meeting-note summarization and follow-up drafting

## Automated Checks

- Missing email addresses
- Email format issues
- Negative or non-numeric opportunity amounts
- Invalid meeting dates
- Duplicate record IDs

## Outputs

- Exception report
- Records review copy
- Human review log
- AI prompt and review notes
- Test log

## AI Use

AI was used to summarize fictional discovery-meeting notes and draft follow-up emails. Generated content was reviewed by a human before use.

## Data Quality and Safety

The project uses fictional data. The script flags issues instead of silently correcting source records. AI-generated suggestions are not automatically written to a CRM.

## Limitations

- The email check is a basic format check, not proof that an email address exists.
- The project does not connect to a live Salesforce or other CRM system.
- AI-generated content requires human verification.

## Learning Outcome

This project demonstrates entry-level Python automation, data validation, exception reporting, responsible AI use, and human-reviewed workflow design.
DROP TABLE IF EXISTS violations;

CREATE TABLE violations (
    citation_id TEXT PRIMARY KEY,
    filed_date DATE,
    issue_date DATE,
    violation_code TEXT NOT NULL,
    violation_title TEXT NOT NULL,
    violation_location TEXT NOT NULL,
    agency TEXT NOT NULL,
    defendent_lastname TEXT NOT NULL,
    defendent_firstname TEXT NOT NULL,
    defendent_city TEXT NOT NULL,
    defendent_state VARCHAR(2) NOT NULL,
    defendent_zip INTEGER(5) NOT NULL,
    defendent_dob DATE,
    gender VARCHAR(1) NOT NULL,
    amount_due  INTEGER(3) NOT NULL,
    amount_paid INTEGER(3) NOT NULL,
    closing_disposition TEXT NOT NULL,
    disposition_date DATE,
    judge TEXT NOT NULL,
    owner_lastname TEXT NOT NULL,
    owner_firstname TEXT NOT NULL,
    owner_city TEXT NOT NULL,
    owner_state VARCHAR(2) NOT NULL,
    owner_zip INTEGER(5) NOT NULL,
    hearing_datetime DATETIME
);

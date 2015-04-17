This directory scripts for inserting the traffic violations data into a Sqlite database for SQL querying. The actual file database is over the GitHub file size limit of 100 MB, but can be downloaded [here](http://s3.amazonaws.com/dwalk/phila_open_data/phila_traffic.db). The MD5 sum of the database is `fb1e6ec24107b8ed6b0c17e5c814d9c7`.

### Requirements
* [Sqlite](https://sqlite.org)  
* If running the insert script, you'll need [Python](http://python.org)

### Instructions
Load the database in Sqlite with:  
    `sqlite3 philly_traffic.db`

To populate another database besides the one included here:

1. From the command line: `sqlite3 [your database name]`
2. At the Sqlite prompt: `.read create_table.sql`
3. Quit sqlite: `.exit`
4. Run the Python insert script: `python insert_data.py`. Change the `DATABASE_NAME`, if necessary, at the top of that file.

### Verification

#### Schema
```sqlite> .schema violations```

| column               | datetype    | constraints |
|----------------------|-------------|-------------|
| citation_id          | TEXT        | PRIMARY KEY |
| filed_date           | DATE        |             |
| issue_date           | DATE        | NOT NULL    |
| violation_code       | TEXT        | NOT NULL    |
| violation_title      | TEXT        | NOT NULL    |
| violation_location   | TEXT        | NOT NULL    |
| agency               | TEXT        | NOT NULL    |
| defendent_lastname   | TEXT        | NOT NULL    |
| defendent_firstname  | TEXT        | NOT NULL    |
| defendent_city       | TEXT        | NOT NULL    |
| defendent_state      | VARCHAR(2)  | NOT NULL    |
| defendent_zip        | INTEGER(5)  | NOT NULL    |
| defendent_dob        | DATE        |             |
| gender               | VARCHAR(1)  | NOT NULL    |
| amount_due           | INTEGER(3)  | NOT NULL    |
| amount_paid          | INTEGER(3)  | NOT NULL    |
| closing_disposition  | TEXT        | NOT NULL    |
| disposition_date     | DATE        |             |
| judge                | TEXT        | NOT NULL    |
| owner_lastname       | TEXT        | NOT NULL    |
| owner_firstname      | TEXT        | NOT NULL    |
| owner_city           | TEXT        | NOT NULL    |
| owner_state          | VARCHAR(2)  | NOT NULL    |
| owner_zip            | INTEGER(5)  | NOT NULL    |
| hearing_datetime     | DATETIME    |             |
| defendent_zip        | INTEGER(5)  |             |

Record counts by year

`sqlite> select strftime("%Y", issue_date) as year, count(*) as citations from violations GROUP BY year;`

| Year | Citations |
|------|-----------|
| 2006 | 116227    |
| 2007 | 106843    |
| 2008 | 114647    |
| 2009 | 98056     |
| 2010 | 84087     |
| 2011 | 108098    |
| 2012 | 166805    |
| 2013 | 155208    |
| 2014 | 74332     |

# Books Database Module
This module demonstrates how scraped and preprocessed book data can be stored in databases as part of a real-world data pipeline.
The project intentionally uses **two databases** to reflect a realistic learning-to-production workflow.
---
## Purpose
- Persist cleaned scraped data
- Practice database-backed data pipelines
- Prepare data for analytics and ML workflows
---
## Phase 1: SQLite (Learning & Prototyping)
### Why SQLite?
SQLite was used initially to:
- Quickly test database concepts
- Learn table creation and inserts
- Work without database server setup
### Database Details
- Engine: SQLite
- File: `books.db`
- Table: `books`
- Records: 1000
This phase helped validate the data schema and pipeline logic.
---

## Phase 2: MySQL (Production-Oriented Pipeline)
After validating the pipeline with SQLite, the data was migrated to **MySQL** to simulate real-world usage.
### Why MySQL?
- Industry-standard relational database
- Scalable and production-ready
- Commonly used in ML data pipelines
---
## Tech Stack
- Python 3.10
- Pandas
- MySQL
- mysql-connector-python
---
## Steps Performed
1. Scraped multi-page book data
2. Cleaned and preprocessed the dataset
3. Designed relational database schema
4. Created MySQL database and table
5. Inserted cleaned CSV data into MySQL
---


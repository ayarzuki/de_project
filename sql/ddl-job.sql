DROP TABLE IF EXISTS jobs;

CREATE TABLE IF NOT EXISTS jobs (
    -- JobId SERIAL PRIMARY KEY,
    JobTitle TEXT,             -- Menambahkan kolom JobTitle
    JobCategory TEXT,          -- Menambahkan kolom JobCategory
    DatePosted TEXT,           -- Menambahkan kolom DatePosted
    CompanyName TEXT,          -- Menambahkan kolom CompanyName
    JobLocation TEXT,          -- Menambahkan kolom JobLocation
    JobExpiredDate TEXT,       -- Menambahkan kolom JobExpiredDate
    MinimalSalary FLOAT,       -- Menambahkan kolom MinimalSalary
    MaximalSalary FLOAT,       -- Menambahkan kolom MaximalSalary
    EmploymentType TEXT,       -- Menambahkan kolom EmploymentType
    JobURL TEXT                -- Menambahkan kolom JobURL
);

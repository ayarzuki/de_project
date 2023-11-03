COPY jobs FROM '/data/job_data_a.csv' DELIMITER AS ',' CSV HEADER;
SELECT * FROM jobs LIMIT 5;
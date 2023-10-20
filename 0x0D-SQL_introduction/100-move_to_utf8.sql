--  a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT to CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table ADD COLUMN name_utf varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
UPDATE first_table set name_utf = name;
ALTER TABLE first_table DROP COLUMN name;
ALTER TABLE first_table RENAME COLUMN name_utf TO name;

/*****************
* File name: doctor.sql
* Author: Eldor
* Date: 2021-06-24
* Version: 1.0
*************
* Changelog
* 2021-06-24 First init
*************/


CREATE TABLE IF NOT EXISTS doctor (
    id_doctor BIGSERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    father_name TEXT,
    user_id INT UNIQUE NOT NULL,
    is_delete BOOLEAN DEFAULT FALSE
);

ALTER TABLE doctor
    ADD COLUMN IF NOT EXISTS first_name TEXT,
    ADD COLUMN IF NOT EXISTS last_name TEXT,
    ADD COLUMN IF NOT EXISTS father_name TEXT,
    ADD COLUMN IF NOT EXISTS user_id INT,

    ADD COLUMN IF NOT EXISTS reg_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    ADD COLUMN IF NOT EXISTS mod_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS exp_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS is_delete BOOLEAN NOT NULL DEFAULT FALSE;

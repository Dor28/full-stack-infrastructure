/*****************
* File name: patient.sql
* Author: Eldor
* Date: 2021-06-30
* Version: 1.0
*************
* Changelog
* 2021-06-30 First init
*************/


CREATE TABLE IF NOT EXISTS patient (
    id_patient BIGSERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    father_name TEXT,
    phone TEXT NOT NULL ,
    address TEXT,
    is_delete BOOLEAN DEFAULT FALSE
);

ALTER TABLE patient
    ADD COLUMN IF NOT EXISTS first_name TEXT,
    ADD COLUMN IF NOT EXISTS last_name TEXT,
    ADD COLUMN IF NOT EXISTS father_name TEXT,
    ADD COLUMN IF NOT EXISTS phone TEXT,
    ADD COLUMN IF NOT EXISTS address TEXT,


    ADD COLUMN IF NOT EXISTS reg_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    ADD COLUMN IF NOT EXISTS mod_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS exp_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS is_delete BOOLEAN NOT NULL DEFAULT FALSE;

/*****************
* File name: visit.sql
* Author: Eldor
* Date: 2021-06-30
* Version: 1.0
*************
* Changelog
* 2021-06-30 First init
* 2021-07-10 Unique constraint removed from patient_id and doctor_id
*************/


CREATE TABLE IF NOT EXISTS visit (
    id_visit BIGSERIAL PRIMARY KEY,
    patient_id INT  NOT NULL ,
    doctor_id INT  NOT NULL ,
    date TIMESTAMP WITH TIME ZONE,
    status TEXT,
    is_delete BOOLEAN DEFAULT FALSE
);

ALTER TABLE visit
    ADD COLUMN IF NOT EXISTS patient_id INT,
    ADD COLUMN IF NOT EXISTS doctor_id INT,
    ADD COLUMN IF NOT EXISTS date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS status TEXT,

    ADD COLUMN IF NOT EXISTS reg_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    ADD COLUMN IF NOT EXISTS mod_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS exp_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS is_delete BOOLEAN NOT NULL DEFAULT FALSE;

/*****************
* File name: analysis.sql
* Author: Eldor
* Date: 2021-06-30
* Version: 1.0
*************
* Changelog
* 2021-06-30 First init
*************/


CREATE TABLE IF NOT EXISTS analysis (
    id_analysis BIGSERIAL PRIMARY KEY,
    document TEXT  NOT NULL ,
    patient_id INT NOT NULL,
    is_delete BOOLEAN DEFAULT FALSE
);

ALTER TABLE analysis
    ADD COLUMN IF NOT EXISTS document TEXT,
    ADD COLUMN IF NOT EXISTS patient_id INT,


    ADD COLUMN IF NOT EXISTS reg_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    ADD COLUMN IF NOT EXISTS mod_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS exp_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS is_delete BOOLEAN NOT NULL DEFAULT FALSE;

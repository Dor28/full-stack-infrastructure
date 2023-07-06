/*****************
* File name: analysis_add.sql
* Author: Eldor
* Date: 2021-07-05
* Version: 1.0
*************
* Changelog
* 2021-07-05 First init
*************/



CREATE OR REPLACE FUNCTION analysis_add(in_document TEXT DEFAULT NULL, in_patient_id INT DEFAULT NULL)

    returns TABLE
            (
                out_id_analysis  BIGINT,
                out_document  TEXT,
                out_patient_id  INT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'analysis_add';
    ERR_CODE  INT  := 4001;

BEGIN
    IF in_document IS NULL OR in_patient_id IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %', ERR_CODE, FUNC_NAME, in_document, in_patient_id
            USING HINT = 'document or patient_id cannot be null';
    END IF;


    RETURN QUERY INSERT INTO analysis (document, patient_id) VALUES (in_document,in_patient_id)
        RETURNING id_analysis, document, patient_id, reg_date, mod_date;


end;
$$
    LANGUAGE 'plpgsql';


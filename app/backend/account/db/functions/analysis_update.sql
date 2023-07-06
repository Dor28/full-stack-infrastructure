/*****************
* File name: analysis_update.sql
* Author: Eldor
* Date: 2021-07-05
* Version: 1.0
*************
* Changelog
* 2021-07-05 First init
*************/


CREATE OR REPLACE FUNCTION analysis_update(in_id_analysis BIGINT DEFAULT NULL, in_document TEXT DEFAULT  NULL , in_patient_id INT DEFAULT NULL )
    returns TABLE
            (   out_id_analysis  BIGINT,
                out_document  TEXT,
                out_patient_id  INT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'analysis_update';
    ERR_CODE  INT  := 4003;

BEGIN
    IF in_id_analysis IS NULL THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %', ERR_CODE, FUNC_NAME, in_id_analysis, in_document, in_patient_id
            USING HINT = 'id_analysis cannot be null';
    END IF;

     IF NOT EXISTS(SELECT 1 FROM analysis WHERE id_analysis=in_id_analysis) OR
       EXISTS(SELECT 1 FROM analysis WHERE  id_analysis=in_id_analysis AND is_delete = TRUE) THEN
        RAISE EXCEPTION 'Error --> % % params %', ERR_CODE, FUNC_NAME, in_id_analysis
            USING HINT = 'analysis not exists';
    END IF;



      IF EXISTS(SELECT 1 FROM analysis WHERE patient_id = in_patient_id AND document = in_document) THEN
        RAISE EXCEPTION 'Error --> % % params %, %, %, %', ERR_CODE, FUNC_NAME, in_document,  in_patient_id
            USING HINT = 'analysis with similar document and patient already exists';
    END IF;


    UPDATE analysis
    SET patient_id=COALESCE(in_patient_id, patient_id),
        document=COALESCE(in_document, document),
        mod_date = now()
    WHERE id_analysis = in_id_analysis;

    RETURN QUERY SELECT id_analysis, document,  patient_id,  reg_date, mod_date
                 FROM analysis
                 WHERE id_analysis = in_id_analysis;


end;
$$
    LANGUAGE 'plpgsql';

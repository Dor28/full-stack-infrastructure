/*****************
* File name: analysis_get_list.sql
* Author: Eldor
* Date: 2021-07-05
* Version: 1.0
*************
* Changelog
* 2021-07-05 First init
*************/


CREATE OR REPLACE FUNCTION analysis_get_list(in_id_analysis BIGINT DEFAULT NULL, in_document TEXT DEFAULT  NULL , in_patient_id INT DEFAULT NULL)
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
    FUNC_NAME TEXT := 'analysis_get_list';
    ERR_CODE  INT  := 4005;

BEGIN
    return QUERY SELECT id_analysis,
                        document,
                        patient_id,
                        reg_date,
                        mod_date
                 FROM analysis

                 where (in_id_analysis IS NULL OR id_analysis = in_id_analysis)
                   AND (in_patient_id IS NULL OR patient_id = in_patient_id)
                   AND (in_document IS NULL OR document =  in_document)
                   AND is_delete = FALSE;

end;
$$
    LANGUAGE 'plpgsql';


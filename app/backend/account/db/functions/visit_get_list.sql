/*****************
* File name: visit_get_list.sql
* Author: Eldor
* Date: 2021-07-04
* Version: 1.0
*************
* Changelog
* 2021-07-04 First init
*************/


CREATE OR REPLACE FUNCTION visit_get_list(in_id_visit BIGINT DEFAULT NULL, in_patient_id INT DEFAULT NULL, in_doctor_id INT DEFAULT NULL,
                                       in_date TIMESTAMP WITH TIME ZONE DEFAULT NULL, in_status TEXT DEFAULT NULL)
     returns TABLE
            (
                out_id_visit BIGINT,
                out_patient_id INT,
                out_doctor_id  INT,
                out_date   TIMESTAMP WITH TIME ZONE,
                out_status TEXT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'visit_get_list';
    ERR_CODE  INT  := 4005;

BEGIN
    return QUERY SELECT id_visit,
                        patient_id,
                        doctor_id,
                        date,
                        status,
                        reg_date,
                        mod_date
                 FROM visit

                 where (in_id_visit IS NULL OR id_visit = in_id_visit)
                   AND (in_patient_id IS NULL OR patient_id = in_patient_id)
                   AND (in_doctor_id IS NULL OR doctor_id = in_doctor_id)
                   AND (in_date IS NULL OR date = in_date)
                   AND (in_status IS NULL OR status = in_status)
                   AND is_delete = FALSE;

end;
$$
    LANGUAGE 'plpgsql';


/*****************
* File name: patient_get_list.sql
* Author: Eldor
* Date: 2021-07-01
* Version: 1.0
*************
* Changelog
* 2021-07-01 First init
*************/


CREATE OR REPLACE FUNCTION patient_get_list(in_id_patient BIGINT DEFAULT NULL,in_first_name TEXT DEFAULT NULL, in_last_name TEXT DEFAULT NULL,
                                       in_father_name TEXT DEFAULT NULL, in_address TEXT DEFAULT NULL,
                                       in_phone TEXT DEFAULT NULL)
     returns TABLE
            (
                out_id_patient  BIGINT,
                out_first_name  TEXT,
                out_last_name   TEXT,
                out_father_name TEXT,
                out_address  TEXT,
                out_phone TEXT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'patient_get_list';
    ERR_CODE  INT  := 4005;

BEGIN
    return QUERY SELECT id_patient,
                        first_name,
                        last_name,
                        father_name,
                        address,
                        phone,
                        reg_date,
                        mod_date
                 FROM patient

                 where (in_id_patient IS NULL OR id_patient = in_id_patient)
                   AND (in_first_name IS NULL OR first_name = in_first_name)
                   AND (in_last_name IS NULL OR last_name = in_last_name)
                   AND (in_father_name IS NULL OR father_name = in_father_name)
                   AND (in_address IS NULL OR address= in_address)
                   AND (in_phone IS NULL OR phone=in_phone)
                   AND is_delete = FALSE;

end;
$$
    LANGUAGE 'plpgsql';


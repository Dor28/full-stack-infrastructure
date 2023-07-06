/*****************
* File name: reception_get_list.sql
* Author: Eldor
* Date: 2021-06-25
* Version: 1.0
*************
* Changelog
* 2021-06-25 First init
*************/


CREATE OR REPLACE FUNCTION reception_get_list(in_id_reception BIGINT DEFAULT NULL, in_first_name TEXT DEFAULT NULL,
                                             in_last_name TEXT DEFAULT NULL, in_father_name TEXT DEFAULT NULL,
                                             in_user_id INT DEFAULT NULL)
     returns TABLE
            (
                out_id_reception  BIGINT,
                out_first_name  TEXT,
                out_last_name   TEXT,
                out_father_name TEXT,
                out_user_id  INT,
                out_reg_date    TIMESTAMP WITH TIME ZONE,
                out_mod_date    TIMESTAMP WITH TIME ZONE
            )
as
$$
DECLARE
    FUNC_NAME TEXT := 'reception_get_list';
    ERR_CODE  INT  := 4005;

BEGIN
    return QUERY SELECT id_reception,
                        first_name,
                        last_name,
                        father_name,
                        user_id,
                        reg_date,
                        mod_date
                 FROM reception

                 where (in_id_reception IS NULL OR id_reception = in_id_reception)
                   AND (in_first_name IS NULL OR first_name = in_first_name)
                   AND (in_last_name IS NULL OR last_name = in_last_name)
                   AND (in_father_name IS NULL OR father_name = in_father_name)
                   AND (in_user_id IS NULL OR user_id = in_user_id)
                   AND is_delete = FALSE;

end;
$$
    LANGUAGE 'plpgsql';


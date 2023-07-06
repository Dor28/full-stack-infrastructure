/*****************
* File name: users.sql
* Author: Zafar
* Date: 2021-06-23
* Version: 1.0
*************
* Changelog
* 2021-06-23 First init
*************/

CREATE TABLE IF NOT EXISTS users (
    id_user BIGSERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_delete BOOLEAN default FALSE
);

ALTER TABLE users
    ADD COLUMN IF NOT EXISTS username TEXT,
    ADD COLUMN IF NOT EXISTS password TEXT,

    ADD COLUMN IF NOT EXISTS reg_date TIMESTAMP WITH TIME ZONE DEFAULT now(),
    ADD COLUMN IF NOT EXISTS mod_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS exp_date TIMESTAMP WITH TIME ZONE,
    ADD COLUMN IF NOT EXISTS is_delete BOOLEAN NOT NULL DEFAULT FALSE;
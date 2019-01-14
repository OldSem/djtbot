CREATE TABLE tgbot_historyupdateid (
    id bigserial primary key,
    created timestamp default NULL,
    update_id varchar(50) NOT NULL,
);
CREATE TABLE tgbot_historyupdate (
    id bigserial primary key,
    update_id varchar(50) NOT NULL,
    article_desc text NOT NULL,
    created timestamp default NULL
);
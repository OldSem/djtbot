/*
sudo -u postgres psql
*/

CREATE DATABASE bot;
CREATE USER advbot WITH password '11bot22';
GRANT ALL ON DATABASE bot TO advbot;

/*
\q
psql -h localhost bot advbot
*/
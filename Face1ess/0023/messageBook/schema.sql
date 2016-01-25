drop table if exists messages;
create table messages(
    id integer primary key autoincrement,
    name text not null,
    text text not null
);


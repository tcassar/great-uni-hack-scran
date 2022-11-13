create table registry
(
    id       INTEGER
        primary key,
    calories INTEGER,
    protein  INTEGER
);

create table pantry
(
    id   INTEGER
        primary key
        references registry,
    mass INTEGER
);

create table recipes
(
    id            INTEGER
        primary key,
    ingredient_id INTEGER
        references registry,
    mass          INTEGER
);

create table shop
(
    id    INTEGER
        primary key
        references registry,
    mass  INTEGER,
    price INTEGER
);


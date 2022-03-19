DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS recipe_ingredients;
DROP TABLE IF EXISTS preparations;
DROP TABLE IF EXISTS recipe_preparations;

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    file_name TEXT UNIQUE
);

CREATE TABLE locations (
    id INTEGER PRIMARY KEY,
    location TEXT UNIQUE,
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE recipe_ingredients (
    ingredient_id INTEGER,
    recipe_id INTEGER,
    amount TEXT,
    PRIMARY KEY (ingredient_id, recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);

CREATE TABLE preparations (
    id INTEGER PRIMARY KEY,
    term TEXT UNIQUE,
    definition TEXT
);

CREATE TABLE recipe_preparations (
    preparation_id INTEGER,
    recipe_id INTEGER,
    PRIMARY KEY (preparation_id, recipe_id),
    FOREIGN KEY (preparation_id) REFERENCES preparations(id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id)
);
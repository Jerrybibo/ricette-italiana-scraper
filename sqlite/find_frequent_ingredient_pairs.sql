-- SELECT ingredient_id, ingredients.name, COUNT(*) AS count
-- FROM ingredients, recipe_ingredients
-- WHERE ingredients.id = recipe_ingredients.ingredient_id
-- GROUP BY ingredient_id
-- ORDER BY count DESC;

SELECT ingredient_id, ingredients.name, COUNT(*) AS frequency
FROM ingredients, recipe_ingredients
WHERE ingredients.id = recipe_ingredients.ingredient_id
    AND recipe_ingredients.recipe IN (
        SELECT recipe_ingredients.recipe
        FROM ingredients, recipe_ingredients
        WHERE recipe_ingredients.ingredient_id = ingredients.id
            AND ingredients.name = 'Salmone'
    )
GROUP BY ingredient_id
ORDER BY frequency DESC;

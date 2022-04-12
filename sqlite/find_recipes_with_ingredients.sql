SELECT recipe_ingredients.recipe
FROM ingredients, recipe_ingredients
WHERE ingredients.id = recipe_ingredients.ingredient_id
AND ingredient_id IN (
    SELECT ingredients.id
    FROM ingredients
    WHERE ingredients.name IN (
        'Aceto balsamico'
    )
)
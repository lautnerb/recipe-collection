from recipe_collection.models import Category, DietLabel, Reference, Ingredient, \
    Spice, TriedCategory, Recipe

category = Category(name="kenyérkrém")
diet_label1 = DietLabel(name="gluténmentes")
diet_label2 = DietLabel(name="cukormentes")
reference = Reference(name="Salátagyár", link="https://salatagyar.hu/cukormentes-mogyorokrem-dietas-nutella/")
ingredient1 = Ingredient(name="törökmogyoró")
ingredient2 = Ingredient(name="kókusztej")
spice1 = Spice(name="kakaópor")
spice2 = Spice(name="őrölt vanília")
tried_category = TriedCategory(name="bevált")
recipe = Recipe(
    name="Mogyorókrém",
    picture="https://i2.wp.com/salatagyar.hu/wp-content/uploads/2017/05/"
            "cukormentes-mogyorokrem-dietas-nutella-hazilag-recept-12.jpg",
    reference=reference,
    category=category,
    tried_category=tried_category,
    comment="egy hétig áll el",
)


def save_all(objects):
    for o in objects:
        o.save()


save_all([
    category,
    diet_label1,
    diet_label2,
    reference,
    ingredient1,
    ingredient2,
    spice1,
    spice2,
    tried_category,
    recipe,
])

recipe.diet_labels.add(diet_label1)
recipe.diet_labels.add(diet_label2)
recipe.ingredients.add(ingredient1)
recipe.ingredients.add(ingredient2)
recipe.spices.add(spice1)
recipe.spices.add(spice2)

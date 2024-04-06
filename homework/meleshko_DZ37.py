import asyncio
from aiohttp import ClientSession


url_recipe = "https://www.themealdb.com/api/json/v1/1/random.php"


async def get_meals_with_butter(url_by_id, session, category):
    async with session.get(url_by_id) as response:
        meals = await response.json()
        meal = meals["meals"][0]["strMeal"]
        if "Butter" in meals["meals"][0].values():
            return meal
        return None


async def get_meals(url_meals, session, category):
    async with session.get(url_meals) as response:
        meals = await response.json()
        lst_meals = []
        lst_meals_with_butter = []
        for el in meals["meals"]:
            lst_meals.append(el["strMeal"])
            id_meal = el["idMeal"]
            url_by_id = (
                "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + id_meal
            )
            with_butter = await get_meals_with_butter(url_by_id, session, category)
            if with_butter:
                lst_meals_with_butter.append(with_butter)

        print(f"получили список блюд категории {category}: {lst_meals}")
        print(
            f"получили список блюд категории {category} с маслом: {lst_meals_with_butter} "
        )


async def get_recipe(url_recipe):
    async with ClientSession() as session:
        async with session.get(url_recipe) as response:
            recipe = await response.json()
            category = recipe["meals"][0]["strCategory"]
            print(category)
            url_meals = (
                "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
            )
            await get_meals(url_meals, session, category)


async def main(url):
    tasks = []
    for _ in range(0, 3):
        tasks.append(asyncio.create_task(get_recipe(url_recipe)))

    for task in tasks:
        await task


asyncio.run(main(url_recipe))

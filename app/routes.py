from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.models import Recipe
from app.ai_service import simplify_recipe

router = APIRouter()

recipes: List[Recipe] = []

@router.post("/recipes")
def add_recipe(recipe: Recipe):
    recipes.append(recipe)
    return {"message": "Recipe added successfully"}

@router.post("/ai/simplify")
def ai_simplify(data: dict):
    if "instructions" not in data:
        raise HTTPException(status_code=400, detail="Instructions required")

    result = simplify_recipe(data["instructions"])
    return {"ai_response": result}

@router.get("/recipes", response_model=List[Recipe])
def get_recipes():
    return recipes

@router.get("/recipes/search")
def search_recipes(
    cuisine: Optional[str] = None,
    vegetarian: Optional[bool] = None,
    max_time: Optional[int] = None,
    ingredient: Optional[str] = None
):
    result = recipes

    if cuisine:
        result = [r for r in result if r.cuisine.lower() == cuisine.lower()]

    if vegetarian is not None:
        result = [r for r in result if r.isVegetarian == vegetarian]

    if max_time:
        result = [r for r in result if r.prepTimeMinutes <= max_time]

    if ingredient:
        result = [r for r in result if ingredient.lower() in [i.lower() for i in r.ingredients]]

    return result

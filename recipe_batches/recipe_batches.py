#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #if recipe and ingredients don't contain the same keys, then return 0
  if set(recipe.keys()) != set(ingredients.keys()):
    return 0
  #loop through each ingredient of the recipe, and record the quotient of amount of this ingredient in ingredients dict and recipe dict
  batches = {i: int(ingredients[i]/recipe[i]) if ingredients[i] >= recipe[i] else 0 for i in recipe.keys()}
  #return the minimum batches 
  return min(batches.values())

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
  ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  # { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
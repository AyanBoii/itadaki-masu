import os
import google.generativeai as genai

# Configure Gemini API key
os.environ["API_KEY"] = "Your Key Here"
genai.configure(api_key=os.environ["API_KEY"])

# Function to generate a recipe using Gemini API
def recipe_generator(ingredients):
    prompt = f"try to Generate a recipe using the following ingredients: {', '.join(ingredients)}. Make sure that the recipe is acceptable and fits in the convetional definition of tasty, you can use the ingredients in a modified way, for example if a certain ingredient doesn't match a flavour you can use it as a garnish or a side dish, keeping in context not to use any additional ingredients apart from the ones specified."
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# Get user input for ingredients
user_input = input("Enter ingredients (separate each with a space): ")
user_ingredients = user_input.split()

# Generate recipe
recipe = recipe_generator(user_ingredients)
print("Generated Recipe:")
print(recipe)

# Swaad - AI Chatbot: Food-Related Queries<br>
A hackathon project that did not help us win. We did, however, get the consolation prize.

## Basic Information
**What this is:** An AI chatbot with a simple interface trained on reliable recipe and nutrititonal data taken from <a href="https://cosylab.iiitd.edu.in/recipedb/">RecipeDB</a>.<br>
**What this does:** Answers recipe, diet, nutrition related queries. Examples below.<br>
**Expected Users:** Anyone looking to cook, or learn about what they're eating.<br><br>
**Tech Stack:** Streamlit, Python.<br>
**Model Used:** Gemini 1.0 Pro. Limited by 30000 tokens, but trained on a much larger dataset through a prompt-engineering workaround.<br><br>
![photo_2024-08-23_17-31-59 (2)](https://github.com/user-attachments/assets/ddb65d0a-954a-459e-92ec-b842ee756246)

## Example Prompts
- Hi, how are you?
- What is the recipe for chicken curry?
- Suggest me a low calorie recipe
- Give me a low fat recipe
- Suggest me an Indian/Italian/healthy/anything recipe
- Suggest me three good summer recipes
- Give me a recipe for someone with an egg allergy
- Give me the nutritional value for the above recipe
- What to cook for Valentine’s night?
<br>
<p>
  <img src="https://github.com/user-attachments/assets/0af2f5ed-5360-45d0-8e45-1f9229c5b37e" alt="mobile screenshot" height="600" style="display: inline-block; margin-right: 100px;"/>
___________
  <img src="https://github.com/user-attachments/assets/2efd1feb-b11b-4c98-9b2e-2e30ed364ec9" alt="second screenshot" height="600" style="display: inline-block;"/>
</p>

## This can't be run anymore
As of today, Google has changed the way API calls to Gemini are made. Along with this, API key for RecipeDB has also expired. The code needs proper updatation for it to run. 

## Acknowledgments
- **Streamlit**: Built a simple and easy-to-use interface for the chatbot through Streanlit.
- **Gemini 1.0 Pro**: For the powerful large-language model behind the chatbot.
- **RecipeDB**: For the comprehensive recipe and nutritional dataset.

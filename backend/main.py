import pandas as pd 
import numpy as np 
import google.generativeai as genai
from langchain.prompts import PromptTemplate

api_key = "AIzaSyDOSxuJMXlB5su56qhVTDr2KP0q7CX9uAk"

genai.configure(api_key=api_key)
model = genai.GenerativeModel()
df = pd.read_csv(r"backend\MoviesOnStreamingPlatforms_updated.csv")
print(df.head())
df_cleaned = df.dropna()

prompt_template = """
You are a skilled data analyst and Python expert. You will receive a description of a query, and your task is to generate the equivalent pandas code to query the movie dataset.
Your Aim is to Help the User to find the best movies only.

Description:
{query_description}

Columns:
['ID', 'Title', 'Year', 'Age', 'IMDb', 'Rotten Tomatoes', 'Netflix',
       'Hulu', 'Prime Video', 'Disney+', 'Type', 'Directors', 'Genres',
       'Country', 'Language', 'Runtime']

Example:
- If the description is: "Get all movies with an IMDb rating greater than 8."
- The output should be:"IMDb > 8"

Output the query as pandas code ONLY that I can query.
How it will run:
df.query(YOUR_PROVIDED_QUERY)

JUST THE YOUR_PROVIDED_QUERY CODE no OTHER TEXT JUST THE PLAIN QUERY THAT I CAN JUST PLUCK IT IN
"""

prompt_template_res = PromptTemplate(
    input_variables=["query_description"],
    template=prompt_template
)
import time
def response(user_input:str):
    res = model.generate_content(contents=prompt_template_res.format(
        query_description=user_input,
    )).text.strip()
    
    try:
        query_result = df.query(res)
        print(query_result)
    except Exception as e:
        print(f"Error executing query: {e}\n Hi")
        return (model.generate_content(contents=f"{user_input}").text.strip())

    summary_prompt = f"""
You have received the results of a pandas query, which provides a selection of movies based on user preferences. 

**Query Result:**
{query_result.to_string(index=False)}

**Task:**
Based on the displayed movies, please offer a relevant recommendation to help the user find a great movie to watch. Consider factors such as genre, popularity, and user ratings in your recommendation.

**User's Description:**
{user_input}

Please present your recommendation clearly and concisely as you are talking to the customer.
"""
    summary_res = model.generate_content(contents=summary_prompt).text.strip()
    
    print("Recommendation based on query result:")
    return summary_res


    


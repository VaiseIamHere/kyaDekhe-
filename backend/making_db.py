import pandas
# import prompts
# import google.generativeai as genai
# from langchain_core.prompts import PromptTemplate
# # Your API key for generative AI
# api_key = "AIzaSyDUl_6Ll4iamZy7gp9Ipv4uc_EbFMRxqHk"
# genai.configure(api_key=api_key)

# # Initialize the model
# model = genai.GenerativeModel("gemini-pro")

# # Create the prompt template
# prompt_template = PromptTemplate(
#     input_variables=["movie_name", "movie_year", "movie_director"],
#     template=prompts.add_actors_prompt  # Ensure this template string is properly defined
# )

# # Create the prompt using format with correct dictionary input
# formatted_prompt = prompt_template.format(
#     movie_name="Lagaan: Once Upon a Time in India",
#     movie_year="2001",
#     movie_director="Ashutosh Gowariker"
# )

# # Generate content using the model
# res = model.generate_content(contents=formatted_prompt)

# # Print the result
# print(res.text.strip())

# Uncomment this if you plan to read a CSV file with movies data
df = pandas.read_csv("MoviesOnStreamingPlatforms_updated.csv")
print(df.isnull().sum())

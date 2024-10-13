add_actors_prompt = """
You are an AI tasked with generating a list of actors for a given movie. Your inputs will include the movie's name, its release year, and the director's name. Based on this information, please provide a comma-separated list of the main cast members associated with the specified movie.

**Input Format:**
- Movie Name: [string]
- Year: [integer]
- Director: [string]

**Output Format:**
- A single line containing the names of the all cast members, separated by commas.

**Example Input:**
- Movie Name: "Inception"
- Year: 2010
- Director: "Christopher Nolan"

**Example Output:**
Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy, Ken Watanabe

Give the list of cast of movie {movie_name} ,year of release {movie_year} and director {movie_director}

A single line containing the names of the ALL cast members, separated by commas ONLY.
"""


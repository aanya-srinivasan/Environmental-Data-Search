
🟢 Part 1: Air Quality Data Analysis 🌿
📚 Overview
Part 1 of this project focuses on analyzing air quality data for New York City (NYC) neighborhoods, specifically using data from UHF (Urban Health and Fitness) locations. The main objective is to read air quality measurements from CSV files, map them by geographic region and date, and provide users with an interactive interface to query this data by various search parameters.

⚙️ Functionality
📥 Reading Air Quality Data (read_air_qual)

The read_air_qual() function reads data from the air_quality.csv file, which contains air quality measurements, including the UHF ID, region, date, and particulate matter (PM) concentration.
It returns two dictionaries:
geo_map: Maps each UHF ID to a list of measurement tuples (UHF id, region, date, pm).
date_map: Maps each date to a list of measurements for that date.
📋 Reading UHF Data (read_uhf)

The read_uhf() function reads data from the uhf.csv file, which contains UHF ID information along with associated zip codes and boroughs.
It returns two dictionaries:
zip_map: Maps each zip code to a list of corresponding UHF IDs.
borough_map: Maps each borough to a list of corresponding UHF IDs, avoiding duplicate entries.
🔍 Interactive Search (search)

The search() function allows the user to search the air quality data interactively based on four parameters: zip code, UHF id, borough, or date.
Depending on the user's input, it fetches and prints air quality data for the specified parameter, including the UHF ID, region, date, and PM concentration.
If the user enters an invalid query, the program will prompt them to try again.
🏁 Main Function (main)

The main() function initializes the process by reading the air quality and UHF data from CSV files, and then calls the search() function to allow the user to interact with the data.
📝 Example of Usage
The user is prompted to choose one of the following search parameters:

📍 Zip code
🆔 UHF id
🏙️ Borough
📅 Date
For example, a user may choose to search by borough, enter Brooklyn, and the program will output the air quality data (including PM concentration) for all UHF IDs in Brooklyn.

🎯 Key Features:
🔎 Data Mapping: Efficiently maps data for quick lookups by UHF ID, date, and borough.
🤖 Interactive Queries: Allows users to search for air quality data based on various criteria (zip code, UHF ID, borough, date).
⚡ Flexibility: Can be easily extended to include additional search parameters or data sources.
📂 Files Used:
air_quality.csv: Contains air quality measurements with columns for UHF ID, region, date, and PM concentration.
uhf.csv: Contains UHF location data, mapping UHF IDs to zip codes and boroughs.
🚀 Future Improvements:
Handle missing or invalid data more robustly.
Add visualization 📊 (e.g., graphs or charts) to display air quality trends.
Optimize performance ⚙️ for larger datasets.

Part 2: Data Analysis Functions 🧑‍🔬
In Part 2, we implement several analysis functions that leverage the air quality and UHF data for deeper insights. These functions allow querying and analyzing pollution levels across different geographic locations (by UHF ID, Zip Code, Borough, Date, and Year), and calculating key statistics such as high/low pollution levels, average pollution per borough, and identifying areas that exceed a pollution threshold.

Key Features:
get_pm(query_type, query, geo_map, date_map, zip_map, borough_map)
Retrieves a list of pollution data (PM levels) based on a given query (zip code, UHF ID, borough, date, or year). Returns a list of tuples containing the UHF ID, Region, Date, and PM value.

high_low_poll(zip_code, geo_map, date_map, zip_map, borough_map)
Returns the lowest and highest pollution levels ever recorded in a given zip code.

worst_poll(year, geo_map, date_map, zip_map, borough_map)
Identifies the UHF ID with the highest pollution recorded for a given year.

avg_poll(year, borough, geo_map, date_map, zip_map, borough_map)
Calculates the average pollution in a specific borough for a given year.

highest_avg_poll(year, geo_map, date_map, zip_map, borough_map)
Finds the borough with the highest average pollution for a given year.

uhf_above_threshold(thresh, year, borough, geo_map, date_map, zip_map, borough_map)
Returns a list of UHF neighborhoods within a specified borough and year that exceed a given pollution threshold.

These functions provide a flexible way to perform air quality analysis at various spatial and temporal levels, helping to uncover pollution hotspots and understand trends in different neighborhoods of New York City. 🌍🌿

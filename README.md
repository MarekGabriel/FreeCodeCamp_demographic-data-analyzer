# Demographic Data Analyzer

This project is part of the ***Data Analysis with Python*** certification from freeCodeCamp.

## Project Description

The goal of this project is to analyze a dataset containing demographic information and extract meaningful insights such as:

* Race distribution
* Average age of men
* Percentage of people with a Bachelor's degree
* Income analysis based on education level
* Work hours statistics
* Country-based income comparisons
* Most popular occupation data

All analysis is performed using Python, primarily with the Pandas library.

## Technologies Used

* Python
* Pandas
* NumPy (optional)

## Dataset

https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/refs/heads/main/adult.data.csv
Dataset Source:
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.

## How to Run

1. Clone the repository:
   git clone https://github.com/MarekGabriel/FreeCodeCamp_demographic-data-analyzer.git

2. Navigate to the project folder:
   cd FreeCodeCamp_demographic-data-analyzer

3. Run the script:
   demographic_data_analyzer.py

## Example Usage

Input:
no input needed (main function imports proper data from .csv)

Output:

Number of each race:
[pandas.Series]
Average age of men: x.x
Percentage with Bachelors degrees: x.x%
Percentage with higher education that earn >50K: x.x%
Percentage without higher education that earn >50K: x.x%
Min work time: x.x hours/week
Percentage of rich among those who work fewest hours: x.x%
Country with highest percentage of rich: xxx
Highest percentage of rich people in country: x.x%
Top occupations in India: xxx

The script returns additionally a Python's dictionary like:
{
'race_count': x,
'average_age_men': x,
'percentage_bachelors': x,
'higher_education_rich': x,
'lower_education_rich': x,
'min_work_hours': x,
'rich_percentage': x,
'highest_earning_country': x,
'highest_earning_country_percentage': x,
'top_IN_occupation': x
}

## Project Structure

* demographic_data_analyzer.py — main function implementation
* main.py — An entrypoint file to be used in development. It imports main function implemented and runs unit tests automatically.
* test_module.py — unit tests provided by freeCodeCamp

## License

This project is licensed under the MIT License.

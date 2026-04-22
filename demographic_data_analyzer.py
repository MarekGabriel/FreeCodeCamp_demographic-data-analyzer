import pandas as pd


def calculate_demographic_data(print_data=True):
    
    # Read data from file
    df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/refs/heads/main/adult.data.csv',
                     header = 0, index_col = False)

    
    #question.01
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby('race')['race'].count()

    
    #question.02
    # What is the average age of men?
    average_age_men = round(df['age'][df['sex'] == 'Male'].mean(), 1)

    
    #question.03
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'][df['education'] == 'Bachelors'].count() / df['education'].count()) * 100, 1)


    #question.04 & question.05
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    salaries_for_people_with_adv_education = df['salary'][(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]

    salaries_for_people_without_adv_education = df['salary'][(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    #Zakomentowałem poniższe zmienne. Pr-podobnie chciano, żeby pod nie przypisać całą ramkę danych dla ludzi z wyższym lub nie wykształceniem,
    #a nie tylko kolumnę Salary (ja właśnie tak jednak zrobiłem jak powyżej)
    #higher_education = None
    #lower_education = None

    # percentages with salary >50K
    higher_education_rich = round((salaries_for_people_with_adv_education[salaries_for_people_with_adv_education == '>50K'].count() / salaries_for_people_with_adv_education.count()) * 100, 1)
    lower_education_rich = round((salaries_for_people_without_adv_education[salaries_for_people_without_adv_education == '>50K'].count() / salaries_for_people_without_adv_education.count()) * 100, 1)

    
    #question.06
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    
    #question.07
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]

    rich_percentage = round((sum(num_min_workers['salary'] == '>50K') / num_min_workers['salary'].count()) * 100, 1)


    #question.08
    # What country has the highest percentage of people that earn >50K?

    #DataFrame with salaries over 50k
    df_salary_over50k = df[df['salary'] == '>50K']
    #number of people grouped per country
    gr1 = pd.DataFrame(df.groupby('native-country')['salary'].count())
    #number of people with salaries over 50k grouped per country
    gr2 = pd.DataFrame(df_salary_over50k.groupby('native-country')['salary'].count())
    #columns renaming: salary_gr1 - number of all people, salary_gr2 - number of people with salary over 50k
    gr1.columns = ['salary_gr1']
    gr2.columns = ['salary_gr2']
    ###print(gr1)
    ###gr1.shape, gr2.shape
    #both DataFrames merged (how-rodzaj JOINa; indicator-kolumna opisuje pochodzenie wiersza; left_index&right_index=True to join po indeksie)
    salary_groups_merged = gr1.merge(gr2, left_index = True, right_index = True, how = 'left', indicator = True)
    #NaN replacing by 0
    salary_groups_merged.fillna({'salary_gr2' : 0}, inplace = True)
    #new column 'percentage_rate' added - for each country percentage of people that earn >50K
    salary_groups_merged['percentage_rate'] = salary_groups_merged['salary_gr2'] / salary_groups_merged['salary_gr1']
    ###salary_groups_merged
    #row with country with the highest percentage of people that earn >50K
    country_highest_percentage_rate = salary_groups_merged[salary_groups_merged['percentage_rate'] == salary_groups_merged['percentage_rate'].max()]
    ###print(country_highest_percentage_rate)

    #country with the highest percentage of people that earn >50K
    highest_earning_country = country_highest_percentage_rate.index[0]
    #the value of the highest percentage of people that earn >50K
    highest_earning_country_percentage = round(country_highest_percentage_rate.iloc[0]['percentage_rate'] * 100, 1)

    
    #question.09
    # Identify the most popular occupation for those who earn >50K in India.
    
    #DataFrame of occupations for those who earn >50K in India
    occupations_selected = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].to_frame()
    #number of people corresponding with occupations for those who earn >50K in India
    occupations_selected_grouped = occupations_selected.groupby('occupation')['occupation'].count().to_frame()
    #column's renaming: number_of_people as a counter 
    occupations_selected_grouped.columns = ['number_of_people']
    #final DataFrame with most popular occupation(s)
    most_popular_occupations = occupations_selected_grouped[occupations_selected_grouped['number_of_people'] == occupations_selected_grouped['number_of_people'].max()]
    #jeżeli więcej jest najpopularniejszych, to przerabiam wynik na listę, w przeciwnym razie wyciągam pierwszy i jedyny element z indeksu
    if len(most_popular_occupations.index) > 1:
        result = list(most_popular_occupations.index)
    else:
        result = most_popular_occupations.index[0]

    #most popular occupation(s) as name(s)
    top_IN_occupation = result

    
    #final results
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

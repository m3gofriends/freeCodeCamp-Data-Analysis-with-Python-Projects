import pandas as pd

def calculate_demographic_data(print_data = True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_list = []
    race_count_list = []
    
    for race in df['race'].values:
        if race not in race_list:
            race_list.append(race)

    for race_name in race_list:
        race_count_list.append(df['race'].values.tolist().count(race_name))

    race_count = pd.Series(race_count_list, race_list)

    # What is the average age of men?
    average_age_men = round(df[(df.sex == 'Male')]['age'].values.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[(df.education == 'Bachelors')]) / len(df) * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[(df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')])
    lower_education = len(df) - higher_education

    # percentage with salary >50K
    higher_education_rich = round((len(df[((df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')) & (df.salary == '>50K')]) / higher_education) * 100, 1)
    lower_education_rich = round((len(df[(df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate') & (df.salary == '>50K')]) / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'].values)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df["hours-per-week"] == 1])
    rich_percentage = round((len(df[(df["hours-per-week"] == 1) & (df.salary == '>50K')]) / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_and_percentage = ["", 0]
    for country_name in set(df['native-country'].values):
        country_percentage = round((len(df[(df['native-country'] == country_name) & (df.salary == '>50K')]) / df['native-country'].values.tolist().count(country_name)) * 100, 1)
        if(max(highest_earning_country_and_percentage[1], country_percentage) != highest_earning_country_and_percentage[1]):
            highest_earning_country_and_percentage[0] = country_name
            highest_earning_country_and_percentage[1] = country_percentage
                
    highest_earning_country = highest_earning_country_and_percentage[0]
    highest_earning_country_percentage = highest_earning_country_and_percentage[1]

    # Identify the most popular occupation for those who earn >50K in India.
    india_list = df[(df['native-country'] == 'India') & (df.salary == '>50K')].occupation.tolist()
    top_IN_occupation = max(india_list, key = india_list.count)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours / week")
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

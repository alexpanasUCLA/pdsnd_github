
import pandas as pd
import numpy as np
import time 



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ('january', 'february', 'march', 'april', 'may', 'june','all')
weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','all')
cities = list(CITY_DATA.keys())



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
  

    while True:
        city = str(input("For what city do you want do select data, New York City, Chicago or Washington?: ")).lower()
        if city in cities:
            print("Thank's for correct input for the city ",city)
            break
        else:
            print("Please, try once again")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('choose month out of all, january, february, march, april, may, june: ')).lower()
        if month in months:
            print("Thank's for correct input for the month ",month)
            break
        else:
            print("Please, try once again")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('choose day of the week or all, enter using commas: ')).lower()
        if day in weekdays:
            print("Thank's for correct input for the weekday ",day)
            break
        else:
            print("Please, try once again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day
#     """

    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time column into datetime format

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Hour'] = df['Start Time'].dt.hour
   

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # month is integer

    df['day_of_week'] = df['Start Time'].dt.day_name()
   
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
       

    # filter by month to create the new dataframe
        df = df[df['month'] == month]
      

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most rides were in: ',months[most_common_month-1].title())
    # TO DO: display the most common day of week
    # most_common_weekday_count = df.groupby(['day_of_week'])['month'].count()
    most_common_weekday = df['day_of_week'].mode()[0]
    print('Most common day of week: ',most_common_weekday)
    # print(most_common_weekday_count)

    # TO DO: display the most common start hour
    most_common_hour = df['Start Hour'].mode()[0]
    print('Most common hour: ',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("The most commonly used start station is: " +
          most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " +
          most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
  
    start_end_combination_count = df.groupby(['Start Station','End Station'])['month'].count().nlargest(1)
    

    print(start_end_combination_count.head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() #in seconds
    duration_days = total_travel_time//(60*60*24)
    duration_hours = total_travel_time % (60*60*24) // 3600
    duration_info = str(duration_days)+" days "+str(duration_hours)+ " hours."
    print('Total travel time', duration_info)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_info = (str(int(mean_travel_time//60)) + "m " +
                        str(int(mean_travel_time % 60)) + "s")

    print('Mean travel time', mean_travel_info)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")
    print(user_types)


    # TO DO: Display counts of gender
    try:
        gender_distribution = df["Gender"].value_counts().to_string()
        print("\nDistribution for each gender:")
        print(gender_distribution)
    except:
        print("There is no data on gender.")


    # TO DO: Display earliest, most recent, and most common year of birth
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = str(int(df["Birth Year"].min()))
        print("\nThe earliest_birth_year ", earliest_birth_year)
        most_recent_birth_year = str(int(df["Birth Year"].max()))
        print("The latest birth year:", most_recent_birth_year)
        most_common_birth_year = str(int(df["Birth Year"].mode()[0]))
        print("Most common year ",most_common_birth_year)
    except:
        print("No data on birth years.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rows(df):
    row=0
    is_show = input("Type yes to show more data or no to stop  ").lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if is_show == 'no':
            break
        elif is_show == 'yes':
            print(df.iloc[row:row+5]) # display next five rows
            is_show = input("Would like to show more? yes or no?  ").lower()
            row += 5
        else:
            is_show= input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

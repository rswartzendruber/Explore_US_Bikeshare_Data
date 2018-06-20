import time
import pandas as pd
import numpy as np
from clear_console import clear

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def welcome_message():
    """Prints a welcome message"""
    clear()
    print('Hello! Let\'s explore some US bikeshare data!')
    input('Press [enter] to continue...')

def quit_message():
    """Prints a message on screen as user leaves program"""
    clear()
    print('Goodbye.')
    time.sleep(1.5)
    clear()

def convert_seconds(seconds):
    """Converts the provided seconds value into days, hours, minutes, seconds and returns a tuple containing each of these values"""

    # Converting seconds to a standard python float type to resolve the "negative 0 when using numpy.float64 type" issue .
    seconds = float(seconds)
    
    # Convert seconds to minutes and store remainder
    minutes = seconds // 60
    seconds = seconds % 60

    # Convert minutes to hours and store remainder
    hours = minutes // 60
    minutes = minutes % 60

    # Convert hours to days and store remainder
    days = hours // 24
    hours = hours % 24

    return days, hours, minutes, seconds


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ""
    month = ""
    day = ""
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    #clear the screen
    clear()

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA:
        city = input("Please select a city's data to analyze (\"Chicago\", \"New York City\", or \"Washington\"): ").lower()
        if city not in CITY_DATA:
            print("Invalid selection.")

    # get user input for month (all, january, february, ... , june)
    clear()
    print('City:  ' + city.title() + '\n' + '-'*40)
    while month not in months:
        month = input(    "If you'd like to filter the data by a specific month, " +
                        "enter that month's name here (January - June). Otherwise, enter \"all\": ").lower()
        if month not in months:
            print("Invalid selection.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    clear()
    print('City:  ' + city.title())
    print('Month: ' + month.title()  + '\n' + '-'*40)
    while day not in days_of_week:
        day = input(    "If you'd like to filter the data by a specific day of the week, " +
                        "enter that day's name here (Monday - Friday). Otherwise, enter \"all\": ").lower()
        if day not in days_of_week:
            print("Invalid selection.")

    clear()
    print('City:  ' + city.title())
    print('Month: ' + month.title())
    print('Day:   ' + day.title()   + '\n' + '-'*40)
    choice = input("Do the above settings look correct (no to reselect)? ")

    if choice.lower() == "no":
        city, month, day = get_filters() 

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Clear the screen and display loading message
    clear()
    print("Loading data set based on selected conditions...")

    # Load the appropriate csv based on city provided by user
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    clear()

    print('Calculating the Most Frequent Times of Travel...')
    start_time = time.time()

    # calc the "most common" time stats
    most_common_month = df['month'].mode()[0]
    most_common_day = df['day_of_week'].mode()[0]
    most_common_hour = df['Start Time'].dt.hour.mode()[0]

    # Print calculation performance times
    print('This operation took {} seconds to complete.'.format(time.time() - start_time))
    print('-' * 40)
    
    # display the statistics
    print('Most common month:       {0}\n'.format(most_common_month) +
          'Most common day of week: {0}\n'.format(most_common_day) + 
          'Most common hour:        {0}\n'.format(most_common_hour))

    input('Press [enter] to return to Main Menu...')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    clear()

    print('Calculating the Most Popular Stations and Trip...')
    start_time = time.time()

    # Calc the "most common" station stats
    most_common_start = df['Start Station'].mode()[0]
    most_common_end = df['End Station'].mode()[0]
    most_common_trip = df.groupby(['Start Station', 'End Station']).size() \
                         .sort_values(ascending=False) \
                         .reset_index(name='count')

    # Print calculation performance times
    print('This operation took {} seconds to complete.'.format(time.time() - start_time))
    print('-' * 40)

    # Display the station statistics
    print('Most common start station: {0}\n'.format(most_common_start) + 
          'Most common end station:   {0}\n'.format(most_common_end) + 
          'Most common trip:          {0} to {1}\n'.format(most_common_trip['Start Station'][0], most_common_trip['End Station'][0]))

    input('Press [enter] to return to Main Menu...')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    clear()

    print('Calculating the total and average Trip Duration...')
    start_time = time.time()

    # Calc the total and average trip duration
    total_trip_duration = df['Trip Duration'].sum()
    mean_trip_duration = df['Trip Duration'].mean()

    # Print calculation performance times
    print('This operation took {} seconds to complete.'.format(time.time() - start_time))
    print('-' * 40)

    # Display trip duration statistics
    print('Total trip duration:          {0} days, {1} hours, {2} minutes, and {3} seconds\n'.format(*convert_seconds(total_trip_duration)) + 
          'Average (mean) trip duration: {0} days, {1} hours, {2} minutes, and {3} seconds\n'.format(*convert_seconds(mean_trip_duration)))

    input('Press [enter] to return to Main Menu...')

def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    clear()

    print('Calculating User Stats...')
    start_time = time.time()

    # Calc the user stats
    output = ''
    failed_gender = False
    failed_birth_year = False
    user_count = df.groupby('User Type').size().reset_index(name = 'count')
    try:
        gender_count = df.groupby('Gender').size().reset_index(name = 'count')
    except KeyError:
        failed_gender = True
    try:
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
    except KeyError:
        failed_birth_year = True


    # Print calculation performance times
    print('This operation took {} seconds to complete.'.format(time.time() - start_time))
    print('-' * 40)

    # Build output string by combining literals and looping through dataframes
    output += 'Counts of User Types\n\n'
    for i, row in user_count.iterrows():
        output += (str(row[0]) +
                  ":" +
                  ' ' * (20 - len(str(row[0]) + str(row[1]))) +
                  str(row[1]) +
                  '\n')

    output += '\nCounts of Genders\n\n'
    if not failed_gender:
        for i, row in gender_count.iterrows():
            output += (str(row[0]) +
                      ":" +
                      ' ' * (20 - len(str(row[0]) + str(row[1]))) +
                      str(row[1]) +
                      '\n')
    else:
        output += 'No Gender data found for ' + city.title() + '.\n'

    output += '\nBirth Year Statistics\n\n'
    if not failed_birth_year:
        output += ('Earliest birth year:    ' + str(min_birth_year)[:4] + '\n' +
                   'Most recent birth year: ' + str(max_birth_year)[:4] + '\n' +
                   'Most common birth year: ' + str(most_common_birth_year)[:4] + '\n')
    else:
        output += 'No Birth Year data found for ' + city.title() + '.\n'

    print(output)
    input('Press [enter] to return to Main Menu...')

def disp_raw_data(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
    input('\nPress [enter] to return to Main Menu...')

def menu(city, month, day, df):
    """
    Presents the user with navigation options to each of the stat groupings and the setting screen.
    Collects the correspdoning user choice and calls the appropriate function.
    """
    # Initialize variables
    choice = ''
    options = {'1':time_stats,'2':station_stats,'3':trip_duration_stats,'4':user_stats,'5':disp_raw_data,'6':None,'q':None}
    #Loop menu until user quits
    while choice != 'q':
        # Reinitialize choice
        choice = ''
        # Clear the screen
        clear()
        # Print main menu options
        print('Main Menu\n' + '-' * 40)
        print('City:  ' + city.title())
        print('Month: ' + month.title())
        print('Day:   ' + day.title()   + '\n' + '-'*40)
        print('Navigation Options:\n' + 
              '1. Time Statistics\n' +
              '2. Station Statistics\n' +
              '3. Trip Duration Statistics\n' +
              '4. User Statistics\n' +
              '5. Raw Data\n' + 
              '6. Settings\n' + 
              'Q. Quit\n')
        while choice not in options:
            choice = input("Where would you like to go? ").lower()
            if choice not in options:
                print('Invalid choice. Please try again.')

        if choice not in ['4', '6', 'q']:
            options[choice](df)
        elif choice == '4':
             options[choice](city, df)
        elif choice == '6':
            city, month, day = get_filters()
            df = load_data(city, month, day)
        

def main():
    welcome_message()
    city, month, day = get_filters()
    df = load_data(city, month, day)
    menu(city, month, day, df)
    quit_message()

if __name__ == "__main__":
    main()

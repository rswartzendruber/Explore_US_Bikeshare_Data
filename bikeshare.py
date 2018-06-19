import time
import pandas as pd
import numpy as np
from clear_console import clear

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def welcome_message():
    clear()
    print('Hello! Let\'s explore some US bikeshare data!')
    input('Press enter to continue...')

def quit_message():
    clear()
    print('Goodbye.')

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
    print('City: ' + city.title() + '\n' + '-'*40)
    while month not in months:
        month = input(    "If you'd like to filter the data by a specific month, " +
                        "enter that month's name here (January - June). Otherwise, enter \"all\": ").lower()
        if month not in months:
            print("Invalid selection.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    clear()
    print('City: ' + city.title())
    print('Month: ' + month.title()  + '\n' + '-'*40)
    while day not in days_of_week:
        day = input(    "If you'd like to filter the data by a specific day of the week, " +
                        "enter that day's name here (Monday - Friday). Otherwise, enter \"all\": ").lower()
        if day not in days_of_week:
            print("Invalid selection.")

    clear()
    print('City: ' + city.title())
    print('Month: ' + month.title())
    print('Day: ' + day.title()   + '\n' + '-'*40)
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def menu(city, month, day, df):
    """
    Presents the user with navigation options to each of the stat groupings and the setting screen.
    Collects the correspdoning user choice and calls the appropriate function.
    """
    # Initialize variables
    choice = ''
    options = ['1','2','3','4','5','6','q']
    #Loop menu until user quits
    while choice != 'q':
        # Reinitialize choice
        choice = ''
        # Clear the screen
        clear()
        # Print main menu options
        print('Main Menu\n' + '-' * 40)
        print('City: ' + city.title())
        print('Month: ' + month.title())
        print('Day: ' + day.title()   + '\n' + '-'*40)
        print('Navigation Options:\n' + 
              '1. Time Statistics\n' +
              '2. Station Statistics\n' +
              '3. Trip Duration Statistics\n' +
              '4. User Statistics\n' +
              '5. Settings\n' + 
              'Q. Quit\n')
        while choice not in options:
            choice = input("Where would you like to go: ").lower()
            if choice not in options:
                print('Invalid choice. Please try again.')





def main():
    welcome_message()
    city, month, day = get_filters()
    df = load_data(city, month, day)
    menu(city, month, day, df)
    #time_stats(df)
    #station_stats(df)
    #trip_duration_stats(df)
    #user_stats(df)
    quit_message()

if __name__ == "__main__":
    main()

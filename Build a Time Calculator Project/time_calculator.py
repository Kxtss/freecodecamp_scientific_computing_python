"""
This module provides a function to calculate a new time by adding a duration
to a given start time, handling changes in days and optionally updating
the day of the week.
"""


def add_time(start, duration, day=None):
    """
    Calculates a new time by adding a duration to a start time.

    Args:
        start (str): The initial time in "HH:MM AM/PM" format.
        duration (str): The duration to add in "HH:MM" format.
        day (str, optional): The starting day of the week (e.g., "Monday").
                             Case-insensitive. Defaults to None.

    Returns:
        str: The new time in "HH:MM AM/PM" format.
             Includes "(next day)" or "(n days later)" if applicable.
             Includes the new day of the week if a starting day was provided.
    """
    # Define a list of days of the week for calculation and display.
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # --- Parse the start time ---
    # Example: "3:30 AM" -> start_time_str = "3:30", start_meridian = "AM"
    start_time_str, start_meridian = start.split(" ")
    # Example: "3:30" -> start_hour_str = "3", start_minute_str = "30"
    start_hour_str, start_minute_str = start_time_str.split(":")

    # --- Parse the duration time ---
    # Example: "2:10" -> duration_hour = "2", duration_minute = "10"
    duration_hour, duration_minute = duration.split(":")

    # --- Store parsed components in a list and convert numeric parts to integers ---
    # This structure allows easy access by index for calculations.
    # [start_hour, start_minute, start_meridian, duration_hour, duration_minute]
    time_parts = []
    time_parts.append(int(start_hour_str))  # Index 0: Start hour as int
    time_parts.append(int(start_minute_str))  # Index 1: Start minute as int
    time_parts.append(start_meridian)  # Index 2: Start meridian (AM/PM) as str
    time_parts.append(int(duration_hour))  # Index 3: Duration hour as int
    time_parts.append(int(duration_minute))  # Index 4: Duration minute as int

    # --- Convert start time to 24-hour format (total minutes from midnight) ---
    # This simplifies addition logic by removing AM/PM complexities during calculation.
    curr_hour_24 = time_parts[0]  # Initialize with the start hour (12-hour format)

    if (
        time_parts[2] == "PM" and curr_hour_24 != 12
    ):  # If PM and not 12 PM (e.g., 3 PM -> 15)
        curr_hour_24 += 12
    elif (
        time_parts[2] == "AM" and curr_hour_24 == 12
    ):  # If 12 AM (midnight) (e.g., 12 AM -> 0)
        curr_hour_24 = 0

    # Calculate total minutes from midnight for the start time
    total_start_minutes = (
        curr_hour_24 * 60 + time_parts[1]
    )  # time_parts[1] is start_minute

    # Calculate total minutes for the duration
    # time_parts[3] is duration_hour, time_parts[4] is duration_minute
    total_duration_minutes = time_parts[3] * 60 + time_parts[4]

    # --- Perform the addition and determine days passed ---
    final_total_minutes = total_start_minutes + total_duration_minutes

    # Define minutes in a full day for division.
    minutes_in_day = 24 * 60  # 1440 minutes

    # Calculate the number of full days that have passed.
    days_passed = final_total_minutes // minutes_in_day

    # Calculate the remaining minutes within the last day.
    # This gives the time relative to midnight (00:00) of the new day.
    remaining_minutes = final_total_minutes % minutes_in_day

    # Convert remaining minutes back into hours and minutes for the final time.
    final_hour_24 = remaining_minutes // 60  # Hour in 24-hour format
    final_minute = remaining_minutes % 60  # Minute (0-59)

    # --- Convert the final time back to 12-hour format and determine AM/PM ---
    new_meridian = "AM"  # Default to AM
    display_hour = final_hour_24  # Initialize with 24-hour format

    if final_hour_24 >= 12:  # If hour is 12 or greater, it's PM
        new_meridian = "PM"

    if final_hour_24 == 0:  # If it's 00:xx (midnight in 24h), display as 12 AM
        display_hour = 12
    elif final_hour_24 > 12:  # If it's after 12 PM (e.g., 13:00 -> 1:00 PM)
        display_hour -= 12
    # If final_hour_24 is between 1 and 11, it's already in the correct 12-hour AM format.

    # Format minutes to always have two digits (e.g., 5 -> "05")
    formatted_minute = str(final_minute).zfill(2)

    # --- Handle the optional starting day of the week ---
    final_day_name = (
        ""  # Initialize as empty string; will be populated if 'day' is provided
    )

    if day is not None:  # Check if a starting day was provided
        # Normalize the input day to match the capitalization in the 'days' list
        # e.g., "tueSday" -> "Tuesday"
        normalized_start_day = day.lower().capitalize()

        try:
            # Find the index of the starting day
            start_day_index = days.index(normalized_start_day)

            # Calculate the final day's index using the days_passed
            # The modulo operator ensures the index wraps around (e.g., 7 becomes 0, 8 becomes 1)
            final_day_index = (start_day_index + days_passed) % len(days)

            # Get the name of the final day from the list
            final_day_name = days[final_day_index]
        except ValueError:
            # This block handles cases where 'day' might not be a valid day name.
            # According to problem specs, we assume valid inputs for start time and day,
            # but handling errors makes the code more robust. Here, it just defaults to no day name.
            final_day_name = ""

    # --- Construct the final result string ---
    # Start with the basic time format
    result_string = f"{display_hour}:{formatted_minute} {new_meridian}"

    # Add the day of the week if it was calculated
    if final_day_name:
        result_string += f", {final_day_name}"

    # Add the "next day" or "n days later" indicator
    if days_passed == 1:
        result_string += " (next day)"
    elif days_passed > 1:
        result_string += f" ({days_passed} days later)"

    return result_string


def main():
    """
    Main function to demonstrate the usage of add_time.
    Includes various test cases as per project requirements.
    """
    print(add_time("3:00 PM", "3:10"))  # Expected: 6:10 PM
    print(add_time("11:30 AM", "2:32", "Monday"))  # Expected: 2:02 PM, Monday
    print(add_time("11:43 AM", "00:20"))  # Expected: 12:03 PM
    print(add_time("10:10 PM", "3:30"))  # Expected: 1:40 AM (next day)
    print(
        add_time("11:43 PM", "24:20", "tueSday")
    )  # Expected: 12:03 AM, Thursday (2 days later)
    print(add_time("6:30 PM", "205:12"))  # Expected: 7:42 AM (9 days later)
    print(
        add_time("3:30 AM", "2:10", "Monday")
    )  # Another test case from previous interaction


# Standard Python entry point to ensure main() runs when the script is executed.
if __name__ == "__main__":
    main()

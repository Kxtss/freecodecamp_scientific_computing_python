import math  # Import the math module for math.floor


class Category:
    """
    Represents a budget category with a name and a ledger to record
    deposits, withdrawals, and transfers.
    """

    def __init__(self, name):
        """
        Initializes a new Category instance.

        Args:
            name (str): The name of the category (e.g., "Food", "Entertainment").
        """
        self.name = name
        self.ledger = []  # List to store transactions

    def deposit(self, amount, description=""):
        """
        Records a deposit in the category's ledger.

        Args:
            amount (float): The amount to deposit.
            description (str, optional): A description of the transaction.
                                         Defaults to an empty string.
        """
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        """
        Calculates and returns the current balance of the category.

        Returns:
            float: The total balance of all deposits and withdrawals.
        """
        total_balance = 0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance

    def check_funds(self, amount):
        """
        Checks if the specified amount is less than or equal to the current balance.

        Args:
            amount (float): The amount to check.

        Returns:
            bool: True if the amount is less than or equal to the balance, False otherwise.
        """
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        """
        Records a withdrawal from the ledger if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.
            description (str, optional): A description of the transaction.
                                         Defaults to an empty string.

        Returns:
            bool: True if the withdrawal was successful, False if insufficient funds.
        """
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": description}
            )  # Withdrawals are negative amounts
            return True
        else:
            return False

    def transfer(self, amount, other_category):
        """
        Transfers an amount from this category to another category.

        Performs a withdrawal from this category and a deposit into the other category,
        both with automatic descriptions, if sufficient funds are available.

        Args:
            amount (float): The amount to transfer.
            other_category (Category): The Category object to which money will be transferred.

        Returns:
            bool: True if the transfer was successful, False if insufficient funds.
        """
        if self.check_funds(amount):
            # Withdraw from this category
            self.withdraw(amount, f"Transfer to {other_category.name}")

            # Deposit into the other category
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a string representation of the category, formatted to display
        the title, transactions, and the total balance.
        """
        # Title centered with asterisks, 30 characters wide
        line_title = f"{self.name:*^30}\n"

        description_line = ""
        for item in self.ledger:
            description = item["description"]
            amount = item["amount"]

            # Truncate description to 23 characters and left-justify it
            truncate_description = description[:23]
            display_description = truncate_description.ljust(23)

            # Format amount to 2 decimal places and right-justify it in 7 characters
            display_amount = f"{amount:7.2f}"

            # Concatenate description and amount for each transaction line
            description_line += f"{display_description}{display_amount}\n"

        # Final line with the total balance formatted
        total_line = f"Total: {self.get_balance():.2f}"

        return line_title + description_line + total_line


def create_spend_chart(categories):
    """
    Generates a bar chart showing the percentage of spending
    for each provided category.

    Args:
        categories (list): A list of Category objects.

    Returns:
        str: The string representation of the spending bar chart.

        Percentage spent by category
        100|
         90|
         80|
         70|
         60| o
         50| o
         40| o
         30| o
         20| o  o
         10| o  o  o
          0| o  o  o
            ----------
             F  C  A
             o  l  u
             o  o  t
             d  t  o
                h
                i
                n
                g
    """

    # List to store the total spent (withdrawals) for each category
    category_withdraws = []
    for category in categories:
        total_spent_in_curr_category = 0
        for item in category.ledger:
            # Only consider withdrawals (negative amounts)
            if item["amount"] < 0:
                total_spent_in_curr_category += abs(
                    item["amount"]
                )  # Use absolute value
        category_withdraws.append(total_spent_in_curr_category)

    # Calculate the grand total spent across all categories
    grand_total_spent = sum(category_withdraws)

    # Calculate percentages rounded down to the nearest 10
    rounded_percentages = []
    for total_spent_in_category in category_withdraws:
        if grand_total_spent == 0:
            percentage = 0
        else:
            percentage = (total_spent_in_category / grand_total_spent) * 100
        # Round the percentage down to the nearest 10%
        rounded_percentage = (math.floor(percentage / 10)) * 10
        rounded_percentages.append(rounded_percentage)

    # Start building the chart string
    chart_string = "Percentage spent by category\n"

    # Draw percentage lines and bars (from 100% down to 0%)
    for i in reversed(range(0, 101, 10)):
        # Format the percentage number (e.g., "100|", " 90|", "  0|")
        formatted_i = str(i).rjust(3) + "|"
        for j in range(len(categories)):
            curr_category_rounded = rounded_percentages[j]
            # If the category's percentage is greater than or equal to the current line, draw an 'o'
            if curr_category_rounded >= i:
                formatted_i += " o "  # One space before 'o', and one space after
            else:
                formatted_i += "   "  # Three spaces if no bar
        # A single space at the end of the bar line, followed by a newline
        chart_string += formatted_i + " \n"

    # Draw the horizontal line
    # 4 leading spaces for indentation, followed by dashes.
    # The length of dashes is (3 * number_of_categories) + 1 (for the final extra space)
    horizontal_line = "    " + ("-" * ((3 * len(categories)) + 1)) + "\n"
    chart_string += horizontal_line

    # Find the maximum length of category names to determine how many lines are needed
    max_name_length = 0
    for category in categories:
        if len(category.name) > max_name_length:
            max_name_length = len(category.name)

    # Draw the category names vertically
    for i in range(max_name_length):
        curr_name_line = "    "  # Four leading spaces for indentation and alignment
        for idx, category in enumerate(
            categories
        ):  # Use enumerate to iterate over categories
            if i < len(category.name):
                # Add the current letter of the name, centered in a 3-character block
                curr_name_line += " " + category.name[i] + " "
            else:
                # If the name is shorter than the current line, add 3 empty spaces
                curr_name_line += "   "

        # Add a single space at the end of the name line, followed by a newline
        chart_string += curr_name_line + " \n"

    # Remove the very last newline character from the final string to meet test requirements
    return chart_string.rstrip("\n")


def main():
    """
    Main function to test the functionality of Category and create_spend_chart.
    """
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")

    clothing = Category("Clothing")
    food.transfer(50, clothing)  # Transfer from food to clothing
    clothing.withdraw(20, "new shirt")  # An additional withdrawal for Clothing

    auto = Category("Auto")
    auto.deposit(500, "initial gas fund")
    auto.withdraw(30.00, "gas fill-up")
    auto.withdraw(15.50, "car wash")

    # Print the string representation of the "Food" category
    print(food)

    # Create the spend chart with all test categories
    categories_for_chart = [food, clothing, auto]
    chart_output = create_spend_chart(categories_for_chart)
    print(chart_output)
    """
    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96
    """


if __name__ == "__main__":
    main()

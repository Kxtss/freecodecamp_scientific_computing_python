"""This project involves creating a function that accepts arithmetic problems
in string format and sorts them vertically, as is done in elementary school.
The function will also have the option to display the answers.
"""


def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges a list of arithmetic problems vertically and side-by-side.

    The function takes a list of strings, where each string represents an
    arithmetic problem. It optionally takes a second argument to display
    the answers.
    """
    # Validate: Too many problems.
    # The project specifies a limit of 5 problems.
    if len(problems) > 5:
        return "Error: Too many problems."
    # Initialize lists to store parts of each line of the final output.
    # Each list will hold the formatted string segments for each problem.
    first_line = []    # Stores the top numbers, right-justified
    second_line = []   # Stores the operators and bottom numbers, right-justified
    dash_line = []     # Stores the dashes for each problem
    result_line = []   # Stores the answers, right-justified (if show_answers is True)
    # Iterate through each arithmetic problem string in the input list.
    for problem in problems:
        # Split the problem string into its components: num1, operator, num2.
        # Assumes problems are always in "num1 operator num2" format for simplicity
        # (full validation for malformed strings would be added if needed,
        # but current rules focus on content of parts).
        parts = problem.split(" ")

        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]
        # Validate: Numbers must only contain digits.
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        # Validate: Operator must be '+' or '-'.
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        # Validate: Numbers cannot be more than four digits.
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # Determine the maximum width required for this individual problem's column.
        # This is the length of the longest number + 2 (for operator and a space).
        max_len = max(len(num1), len(num2)) + 2
        # Format the first line (top number).
        # Right-justifies num1 within the calculated max_len.
        first_line.append(num1.rjust(max_len))
        # Calculate spaces needed between the operator and num2 for right-alignment.
        # max_len (total width) - len(num2) - 1 (for operator) = spaces needed before num2
        spaces_op_num2 = max_len - len(num2) - 1
        # Format the second line (operator and bottom number).
        # Concatenates operator, calculated spaces, and the bottom number.
        second_line.append(operator + (" " * spaces_op_num2) + num2)
        # Format the dash line.
        # Creates a string of dashes with the same length as max_len.
        dash_line.append("-" * max_len)
        # If answers are requested, calculate and format them.
        if show_answers:
            result = ""
            num1_int = int(num1)
            num2_int = int(num2)
            # Perform addition or subtraction based on the operator.
            if operator == "+":
                result = str(num1_int + num2_int)
            elif operator == "-":
                result = str(num1_int - num2_int)
            # Append the right-justified result to the result_line list.
            result_line.append(result.rjust(max_len))
    # --- Assemble the final output string outside the loop ---
    # This ensures all problems are processed before joining lines.

    final_output = []
    # Join the individual problem segments for the first line using 4 spaces as separator.
    final_output.append("    ".join(first_line))
    # Join the individual problem segments for the second line.
    final_output.append("    ".join(second_line))
    # Join the individual problem segments for the dash line.
    final_output.append("    ".join(dash_line))
    # If answers were requested, join the result line segments as well.
    if show_answers:
        final_output.append("    ".join(result_line))
    # Join all the constructed lines with newline characters and return the final string.
    return "\n".join(final_output)


def main():
    """
    Main function to demonstrate the usage of arithmetic_arranger.
    """
    # Example usage of the function.
    # This array will be passed to arithmetic_arranger.
    array = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    # Call the function with show_answers set to True and print the formatted output.
    print(f"\n{arithmetic_arranger(array, True)}")


# Standard Python entry point to ensure main() runs when the script is executed.
if __name__ == "__main__":
    main()

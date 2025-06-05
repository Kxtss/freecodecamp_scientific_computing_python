import copy  # Needed for creating deep copies of the Hat object
import random # Needed for random selection of balls

class Hat:
    """
    Represents a hat containing balls of different colors.
    Allows adding balls to the hat and drawing them randomly without replacement.
    """

    def __init__(self, **kwargs):
        """
        Initializes a Hat object with the specified balls by color and quantity.
        
        Args:
            **kwargs: Keyword arguments where the key is the color (str)
                      and the value is the quantity (int) of balls of that color.
                      Example: Hat(red=5, blue=2)
        """
        self.contents = [] # List to store all balls as color strings
        
        # Iterate over each color-quantity pair provided in the arguments
        for color, count in kwargs.items():
            # Add the 'color' to the 'contents' list 'count' number of times
            # to represent each individual ball.
            for _ in range(count):
                self.contents.append(color)
        
        # Store an initial copy of 'contents'. This is crucial for the
        # 'experiment' function to be able to reset the hat to its original state
        # in each new simulation, without modifying the original Hat object.
        self.original_contents = self.contents[:]

    def draw(self, num_balls):
        """
        Draws a specified number of balls randomly from the hat.
        Drawn balls are removed from the hat (without replacement).

        Args:
            num_balls (int): The number of balls to draw from the hat.

        Returns:
            list: A list of strings, where each string is the color of a
                  ball that was drawn. If more balls are requested than available,
                  all remaining balls are returned.
        """
        extracted_balls = [] # List to store the balls drawn in this call

        # If the number of balls to draw is greater than or equal to the number of balls in the hat,
        # draw all remaining balls.
        if num_balls >= len(self.contents):
            # Take a copy of all remaining balls to return them
            all_remaining_balls = self.contents[:]
            self.contents.clear() # Empty the hat as all balls have been drawn
            return all_remaining_balls
        
        # Iterate 'num_balls' times to draw each ball
        for _ in range(num_balls):
            # Select a ball randomly from the remaining balls in the hat.
            # random.choice() selects a random element from the list.
            random_ball = random.choice(self.contents)
            
            # Add the selected ball to the list of extracted balls.
            extracted_balls.append(random_ball)
            
            # Remove the selected ball from the hat's 'contents' list.
            # list.remove(value) deletes the first occurrence of the specified value.
            # This simulates drawing "without replacement".
            self.contents.remove(random_ball)
            
        return extracted_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Performs a Monte Carlo simulation to estimate the probability of
    drawing a specific group of balls from a hat.

    Args:
        hat (Hat): A Hat object representing the initial contents of the hat.
                   This object will be deep-copied for each experiment.
        expected_balls (dict): A dictionary indicating the exact group of balls
                               to look for. E.g., {'red': 2, 'green': 1}.
        num_balls_drawn (int): The number of balls to draw from the hat in
                               each individual experiment.
        num_experiments (int): The total number of experiments (simulations)
                               to perform.

    Returns:
        float: The estimated probability of drawing the expected balls.
    """
    count_success = 0 # Initialize a counter for the number of successful experiments
    
    # Loop 'num_experiments' times to run each simulation
    for _ in range(num_experiments):
        # IMPORTANT: For each experiment, a DEEP COPY of the original 'hat' object
        # must be created. This ensures that each experiment starts with the hat
        # in its pristine initial state, unaffected by previous draws.
        hat_copy = copy.deepcopy(hat)
        
        # Draw 'num_balls_drawn' balls from the hat_copy for this specific experiment.
        # The result (list of drawn balls) is stored in 'drawn_balls'.
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Create a NEW dictionary to count the actual balls drawn in THIS experiment.
        # This is separate from the 'expected_balls' parameter.
        drawn_balls_count = {} 
        for ball in drawn_balls:
            drawn_balls_count[ball] = drawn_balls_count.get(ball, 0) + 1
            
        # Initialize a flag to determine if this experiment meets all expectations.
        # Assume it meets expectations until a condition proves otherwise.
        meets_expectations = True
        
        # Iterate over the 'expected_balls' (color, expected_amount) passed as a parameter.
        # This checks if the *drawn* balls satisfy the *expected* criteria.
        for color, expected_amount in expected_balls.items():
            # Check if the count of 'color' in 'drawn_balls_count' is less than 'expected_amount'.
            # .get(color, 0) handles cases where a color might not have been drawn at all.
            if drawn_balls_count.get(color, 0) < expected_amount:
                meets_expectations = False # If any expected condition is not met, mark as false.
                break # No need to check further colors for this experiment, it has already failed.
        
        # If, after checking all expected colors, 'meets_expectations' is still True,
        # it means this experiment was a success. Increment the success counter.
        if meets_expectations: # Equivalent to 'if meets_expectations == True:' but more concise
            count_success += 1
            
    # Calculate the estimated probability AFTER all 'num_experiments' have completed.
    # This calculation and the return statement must be outside the main 'for' loop.
    probability = count_success / num_experiments
    return probability

def main():
    """
    Main function to demonstrate the usage of the Hat class and experiment function.
    Runs a sample experiment and prints the estimated probability.
    """
    # Create a Hat object with a specific initial set of balls
    hat = Hat(black=6, red=4, green=3)

    # Run the experiment with the defined hat, expected balls, number of balls to draw,
    # and total number of experiments.
    probability = experiment(
        hat=hat,
        expected_balls={"red": 2, "green": 1}, # Example: expecting at least 2 red and 1 green
        num_balls_drawn=5,                     # Drawing 5 balls per experiment
        num_experiments=2000,                  # Performing 2000 experiments
    )

    # Print the estimated probability
    print(probability)

# This standard Python construct ensures that main() is called only when
# the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    main()
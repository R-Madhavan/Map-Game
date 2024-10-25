import turtle
import pandas

# Set up the screen and background
screen = turtle.Screen()
screen.title("Guess The Indian State")
screen.setup(width=650, height=700)
screen.addshape("Indian_Map.gif")
turtle.shape("Indian_Map.gif")

# Load states and coordinates data
location = pandas.read_csv("Indian_states.csv")
all_states = location["State"].to_list()

# Initialize game variables
score = 0
game_on = True

# Start guessing loop
guess = screen.textinput("Guess The State", "Enter the Name of the Next State:")
if guess:
    guess = guess.title()

    while game_on:
        if guess in all_states:
            # Display guessed state on the map
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            new_location = location[location.State == guess]
            score += 1
            state_name.goto(x=new_location["x"].item(), y=new_location["y"].item())
            state_name.write(new_location["State"].item())
            all_states.remove(guess)

        elif guess == "Exit":
            # Save unfound states to a new CSV file and end game
            unfound_states = pandas.DataFrame(all_states, columns=["Unfound States"])
            unfound_states.to_csv("unfound_states.csv", index=False)
            print(f"Unfound states saved to 'unfound_states.csv'.")
            print("Exiting the game...")
            break  # Exit the loop immediately

        # Prompt for the next guess
        guess = screen.textinput(f"{score}/28 Guessed Correctly", "Enter the Name of the Next State:")
        if guess:
            guess = guess.title()
        else:
            print(f"Quitting the game with a score of {score}/28....")
            game_on = False
            turtle.bye()

        # End game if all states are guessed correctly
        if score >= 28:
            print("Congratulations! You guessed all states.")
            game_on = False
            turtle.done()


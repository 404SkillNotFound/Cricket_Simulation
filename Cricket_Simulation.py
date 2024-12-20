import random


indian_players = ["MS Dhoni", "Rohit Sharma", "Virat Kohli", "Jasprit Bumrah", "KL Rahul", "Ravindra Jadeja", "Shikhar Dhawan"]
australian_players = ["Steve Smith", "David Warner", "Pat Cummins", "Aaron Finch", "Glenn Maxwell", "Marcus Stoinis", "Mitchell Starc"]

commentators = ["Ravi Shastri", "Michael Slater"]

def toss():
    teams = ["India", "Australia"]
    toss_winner = random.choice(teams)
    decision = random.choice(["bat", "bowl"])
    return toss_winner, decision

def ball_outcome():
    outcomes = ["0", "1", "2", "3", "4", "6", "W", "NB"]
    return random.choice(outcomes)

def random_commentator():
    return random.choice(commentators)

def random_phrase(outcome):
    phrases = {
        "6": "and it's a huge SIX! That's out of the park!",
        "4": "That's a beautiful shot, perfectly timed for FOUR!",
        "W": "and that's a wicket! What a sensational catch!",
        "NB": "Oh, no-ball! The batsman gets a free hit now.",
        "1": "A quick single, sharp running between the wickets.",
        "2": "They'll come back for two, excellent running!",
        "3": "Brilliant shot, they manage to get three runs!"
    }
    return phrases.get(outcome, "")

def simulate_inning(team_name, players):
    balls = 0
    runs = 0
    wickets = 0
    scorecard = []

    striker = random.choice(players)
    non_striker = random.choice([p for p in players if p != striker])
    bowler = random.choice(australian_players if team_name == "India" else indian_players)

    print(f"\n{team_name} opening batsmen: {striker} and {non_striker}. Bowler: {bowler}")

    while balls < 6 and wickets < 7:  # Limit set to 7 wickets
        outcome = ball_outcome()

        commentator = random_commentator()
        phrase = random_phrase(outcome)

        # Enhanced commentary output
        print(f"\n★ Ball {balls + 1} ★")
        print(f"{commentator}: {phrase}")
        print("-" * 30)

        if outcome == "W":
            wickets += 1
            scorecard.append(f"W")
        elif outcome == "NB":
            extra_run = random.randint(1, 6)
            runs += extra_run  
            scorecard.append(f"NB+{extra_run}")
            continue  
        else:
            runs += int(outcome)
            scorecard.append(outcome)

        balls += 1

        print(f"Ball {balls} (Outcome: {outcome})")
        print(f"Current Score: {runs}/{wickets}")
        print("-" * 30)

    return scorecard, runs, wickets

def play_match():
    # Commentary intro
    print("Welcome everyone for the cricket match between India and Australia!")
    print("Here are the players for today:")
    print("India:", ", ".join(indian_players))
    print("Australia:", ", ".join(australian_players))
    
    # Toss to decide the order of play
    toss_winner, decision = toss()
    print(f"\nThe Indian team captain MS Dhoni comes out for the toss against Steve Smith.")
    print(f"{toss_winner} wins the toss and chooses to {decision}.")

    if decision == "bat":
        batting_team, bowling_team = toss_winner, "Australia" if toss_winner == "India" else "India"
        batting_players, bowling_players = (indian_players, australian_players) if batting_team == "India" else (australian_players, indian_players)
    else:
        bowling_team, batting_team = toss_winner, "Australia" if toss_winner == "India" else "India"
        batting_players, bowling_players = (indian_players, australian_players) if batting_team == "India" else (australian_players, indian_players)

    print(f"\n{batting_team} is batting:")
    batting_scorecard, batting_runs, batting_wickets = simulate_inning(batting_team, batting_players)
    print(f"{batting_team} scored {batting_runs}/{batting_wickets}. Ball outcomes: {batting_scorecard}")

    print(f"\n{bowling_team} is batting now:")
    bowling_scorecard, bowling_runs, bowling_wickets = simulate_inning(bowling_team, bowling_players)
    print(f"{bowling_team} scored {bowling_runs}/{bowling_wickets}. Ball outcomes: {bowling_scorecard}")

    # Declare winner
    commentator = random_commentator()
    if batting_runs > bowling_runs:
        print(f"\n{commentator}: \"What an incredible performance! {batting_team} wins by {batting_runs - bowling_runs} runs!\"")
    elif bowling_runs > batting_runs:
        print(f"\n{commentator}: \"A fantastic game, {bowling_team} clinches victory by {bowling_runs - batting_runs} runs!\"")
    else:
        print(f"\n{commentator}: \"This match was unbelievable! We have a tie!\"")

# Start the match simulation
play_match()

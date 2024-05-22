from higher_lower_logo import logo, vs
import higher_lower_game_data as db
import random

data = db.data
#a = random.choice(data)
#b = random.choice(data)

print(logo)
score = 0
game_should_continue = True

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

account_b = random.choice(data)
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    # Give user feedback

    if is_correct:
        score += 1
        print(f"You're right!, Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, Final score: {score}")

#def getting_info(data):
    #ran_char = random.choice(data)
#    name = ran_char['name']
#    follower = ran_char['follower_count']
#    description = ran_char['description']
#    country = ran_char['country']
#    return f"Compare A: {name}, {description}, from {country}", follower

#person_a, followers_a = getting_info(data)
#person_b, followers_b = getting_info(data)
#
#print(person_a)
#print(f"This is the amount of followers {followers_a}")
#print(person_b)
#print(f"This is the amount of followers {followers_b}")
#
#answer = input("Who has more followers? Type 'A' or 'B': ").lower()
#print(answer)
# format the account data into printalble format


# generate a random number

# get info from data based on the random number

# compare both datas

# if guessed right removed A  and set B as new A and generate the random number again and compare them.

# keep a score variable that display how many right answer u got

# ask who has more followers

# lose when the mount of follower is less than selected and show the score

#print(data)


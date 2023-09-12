from game_logo import logo
from game_data import data

print(logo)
score = 0
next = 0;
last_question = len(data) - 1
other_key = ""
followers_count = {
    'a': data[next].get('follower_count'),
    'b': data[next + 1].get('follower_count')
}


def next_follower_amount(response):
    if response == 'a':
        return followers_count.get('b')
    else:
        return followers_count.get('a')


def compare_followers(follower1, follower2):
    if follower1 > follower2:
        return True
    else:
        return False


while next < last_question:
    # get the questions
    current_question = data[next].get("name") + " " + data[next].get("description")
    next_question = data[next + 1].get("name") + " " + data[next + 1].get("description")

    # display the questions
    print(f'Compare A: {current_question}, {current_question}.')
    print("vs")
    print(f'Against : {next_question}, {next_question}.')
    more_followers = input("Who has more followers? Type 'A' or 'B': ").lower()
    # checking
    current_follower = followers_count.get(more_followers);
    next_follower = next_follower_amount(more_followers)
    result = compare_followers(current_follower,next_follower)
    if result:
        score += 1
    else:
        print(f'sorry that was wrong, score {score}')
        break

    next += 1

print(f'your total is {score}')

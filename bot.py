from urllib.parse import quote_plus

import praw

TEST_TRIGGERS = ["strafe-test"]
REPLY = ["test sucessful"]

def main():
    reddit = praw.Reddit(
        user_agent='u/Strafebot-r by u/Stafe_Stopper',
        client_id='SDaOBSwKeqvYrQ', client_secret="BsE9BaBA_m0C__FsiinzKf6vuXs",
        username='Strafebot-r', password='360F%BepO5zK'
    )

    subreddit = reddit.subreddit('NoahBM')
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    if len(submission.title.split()) > 10:
        return

    normalized_title = submission.title.lower()
    for question_phrase in TEST_TRIGGERS:
        if question_phrase in normalized_title:
            reply_text = REPLY
            print("Replying to: {}".format(submission.title))
            submission.reply(reply_text)
            break


if __name__ == "__main__":
    main()

import praw 
import re

# Connect to reddit API with my bot account
reddit = praw.Reddit(client_id = 'ClLrpX58ASawAQ',
                     client_secret= 'C7QkfGcziDkf6d6PLwQnBM5GMD8',
                     username='overusedBot',
                     password='staysafebot',
                     user_agent='overusedBot')

overused = {'Have an upvote.',
            'Edit: Thanks for the gold kind stranger!',
            'Nice.',
            'nice.',
            'Happy Cake Day',
            'Doggo',
            'Pupper',
            'Good Boye',
            'Fren',
            'Heckin',
            'Came gere to say this',
            'this',
            'This.',
            'This',
            ''
            }
# Choose which subreddit we will scrape
subreddit = reddit.subreddit('funny')


# Utilize stream to update comments live
# The comments are formatted to make them more readable in terminal
for comment in subreddit.stream.comments():
    try:
        parent_id = str(comment.parent())
        original = reddit.comment(parent_id)
        print('Parent:\n')
        format_original = re.sub("(.{64})", "\\1\n" + 5*" ", str(original.body), 0, re.DOTALL)
        print(5 * ' ' + format_original + '\n')

        print(10 * ' ' + 'Reply:')
        comment_original = re.sub("(.{64})", "\\1\n" + 10*" ", str(comment.body), 0, re.DOTALL)
        print(10 * ' ' + comment_original + '\n' + 64*'=')
    except praw.exceptions.PRAWException as e:
        pass



# Recursivley grab all comments and comment IDs from first 3 hot posts
#
# hot_funny = subreddit.hot(limit = 3)

# for submission in hot_funny:
#     if not submission.stickied:
#         print(submission.title)

#         submission.comments.replace_more(limit = 0)
#         for comment in submission.comments.list():
#             print(20*'-')
#             print('Parent ID:', comment.parent())
#             print('Comment ID:', comment.id)
#             print(comment.body)

            
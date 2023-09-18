# secret: LuKoCRahBhEnELQl9_oputhWCEclIQ
# developers	Afraid-Elk-3837 (that's you!) remove
# id Uh3o5mClKNz4JI4HPI936A

# datetime_post = datetime.datetime.fromtimestamp(post.created_utc)

import praw
import datetime
import calendar


def filters_posts_for_the_last_three_days(posts: any) -> list:
    posts_three_days = []

    for post in posts:
        if post.created_utc > utc_time_three_days_ago:
            posts_three_days.append(post)
            url = post.url
    return posts_three_days


def get_counts_the_number_of_post_authors(posts: list) -> dict:
    posts_authors = {}

    for post in posts:
        if post.author not in posts_authors:
            posts_authors[post.author] = 1
        posts_authors[post.author] += 1
        
    return posts_authors


def get_counts_the_number_of_comments_authors(posts: list) -> dict:
    comments_authors = {}

    for post in posts:
        if 'comments' in post.url:
            submission = reddit.submission(url=post.url)
            submission.comments.replace_more(limit=None)            # Берем только верхний слой в древе комментариев к посту

            for top_level_comment in submission.comments:
                if top_level_comment.author not in comments_authors:
                    comments_authors[top_level_comment.author] = 1
                else:
                    comments_authors[top_level_comment.author] += 1
    return comments_authors


def print_top_comments_authors(top: list[tuple]) -> None:
    print('Топ авторов комментов:')
    for k, v in top:
        print(k, v)


def print_top_posts_authors(top: list[tuple]) -> None:
    print('Топ авторов постов:')
    for k, v in top:
        print(k, v)

 
reddit = praw.Reddit(
    client_id='Uh3o5mClKNz4JI4HPI936A',
    client_secret='LuKoCRahBhEnELQl9_oputhWCEclIQ',
    user_agent= 'learn-python (by /u/Rukin17)'
)


delta = datetime.timedelta(days=3)
now = datetime.datetime.now()
three_days_ago = now - delta
utc_time_three_days_ago = calendar.timegm(three_days_ago.utctimetuple())

posts = reddit.subreddit("nhl").new(limit=100)
posts_three_days = filters_posts_for_the_last_three_days(posts=posts)

posts_authors = get_counts_the_number_of_post_authors(posts=posts_three_days)
comments_authors = get_counts_the_number_of_comments_authors(posts=posts_three_days)

sorted_comments_authors = sorted(comments_authors.items(), key=lambda item: item[1], reverse=True)
sorted_posts_authors = sorted(posts_authors.items(), key=lambda item: item[1], reverse=True)


top_comments_authors = sorted_comments_authors[:5]
top_posts_authors = sorted_posts_authors[:5]

print_top_comments_authors(top=top_comments_authors)
print_top_posts_authors(top=top_posts_authors)

    

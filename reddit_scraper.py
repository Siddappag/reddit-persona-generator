import praw

def init_reddit_client():
    return praw.Reddit(
        client_id="7QA1mWMEwuh8EVM5gOfW0g",
        client_secret="xbNed3wliqbA4DcJOYaTrmDfsPagKQ",
        user_agent="windows:reddit.persona:v1.0 (by u/According_Appeal_683)"
    )

def get_user_content(username, limit=100):
    reddit = init_reddit_client()
    user = reddit.redditor(username)
    
    posts = []
    comments = []

    for submission in user.submissions.new(limit=limit):
        posts.append({
            "type": "post",
            "title": submission.title,
            "body": submission.selftext,
            "permalink": f"https://reddit.com{submission.permalink}"
        })

    for comment in user.comments.new(limit=limit):
        comments.append({
            "type": "comment",
            "body": comment.body,
            "permalink": f"https://reddit.com{comment.permalink}"
        })

    return posts + comments

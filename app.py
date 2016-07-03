# Info here http://praw.readthedocs.io/en/stable/pages/call_and_response_bot.html
import praw
import db

user_agent = "SummonerQA-SVC 0.1 by /u/summonerqa"
print("Agent: " + user_agent);

r = praw.Reddit(user_agent=user_agent)

print("Getting stickied summonerschool thread")
dump_comments()

def dump_comments():
    # TODO: Make sure this is the Weekly QA thread
    qa_sticky = r.get_sticky("summonerschool", bottom=False)

    for rcomment in qa_sticky.comments:
        if hasattr(rcomment, "body"):
            comment = db.Comment(rcomment)
            db.insert_comment(comment)

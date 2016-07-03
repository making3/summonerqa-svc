from pymongo import MongoClient
import json

client = MongoClient()
db = client.summonerqa

def comment_exists(id):
    return db.comments.find({ "reddit_id": id }).limit(1).count(True) == 1

def insert_comment(comment):
    j = comment.to_document()
    db.comments.insert_one(w)

class Comment:
    def __init__(self, rcomment):
        self.reddit_id = rcomment.id
        self.body = rcomment.body
        self.score = rcomment.score
        self.permalink = rcomment.permalink
        self.author = rcomment.author.name

        self.replies = []
        for reply in rcomment.replies:
            r = Comment(reply)
            self.replies.append(r)

    def to_document(self):
        # Dump nested structure as string, then load as json obj
        j = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        return json.loads(j)

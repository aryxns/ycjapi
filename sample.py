import api

hn = api.HackerNews()

for i in hn.jobs(limit=5):
    print(i.title)
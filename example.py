from myket_search import MyketSearch

myket = MyketSearch()

apps = myket.search("روبیکا")

for app in apps:
    print(app)

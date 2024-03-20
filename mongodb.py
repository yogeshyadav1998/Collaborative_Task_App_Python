import pymongo
import json
f = open('config.json')
envVariables = json.load(f)

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

client = pymongo.MongoClient(envVariables["MONGODB_URL"])

# database connection
db = pymongo.database.Database(client, 'test')
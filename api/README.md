# Application description
The application creates a simple API using Python Flask (with Blueprint and request) and Mongo database
for returning the logs (GET) and creating a new one (POST).

## DATABASE

A database with name TEST_LOGS_DB is created and one collection. The collection data format is

```
[{"_id": {"$oid": 1}, "user": "user1", "title": "My first log"}]
```

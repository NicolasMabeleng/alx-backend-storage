# MongoDB Cheat Sheet

## Basics

- **Create Database**
  ```bash
  use <database_name>
  ```

- **Show All Databases**
  ```bash
  show dbs
  ```

- **Insert Document**
  ```bash
  db.<collection_name>.insert({ key: value })
  ```

- **Lists all Document**
  ```bash
  db.<collection_name>.find()
  ```

- **Count all Document**
  ```bash
  db.<collection_name>.find().count()
  ```

- **Query Document**
  ```bash
  db.<collection_name>.find({ key: value })
  ```

- **Update Document**
  ```bash
  db.<collection_name>.update({ key: value }, { $set: { new_key: new_value } })
  ```

- **Remove Document**
  ```bash 
  db.<collection_name>.remove({ key: value })
  ```
  ```bash
  db.<collection_name>.deleteMany({ key: value })
  ```

## Indexing

- **Create Index**
  ```bash
  db.<collection_name>.createIndex({ key: 1 })
  ```

- **List All Indexes**
  ```bash
  db.<collection_name>.getIndexes()
  ```

## Aggregation

- **Aggregate Pipeline**
  ```bash
  db.<collection_name>.aggregate([ { $group: { _id: "$key", count: { $sum: 1 } } } ])
  ```

## Backup and Restore

- **Backup Database**
  ```bash
  mongodump --db <database_name> --out <backup_directory>
  ```

- **Restore Database**
  ```bash
  mongorestore --db <database_name> <backup_directory>/<database_name>
  ```

## Tips and Best Practices

- **Data Modeling**
  - Choose appropriate data types and document structures.
  - Design for your application's specific queries.

- **Indexing**
  - Use indexes strategically to optimize query performance.

- **Scaling**
  - Horizontal scaling with sharding for large datasets.

- **Security**
  - Enable authentication and set up user roles.
  - Regularly audit and update security settings.

- **Monitoring**
  - Utilize tools like MongoDB Compass for real-time monitoring.
  - Keep an eye on slow queries for optimization opportunities.

- **Backup and Recovery**
  - Regularly schedule backups to prevent data loss.
  - Test the restore process to ensure data recoverability.

<br>
<hr>
<br>
<hr width='50%'>
<br>
<hr>

# MongoDB with Python (PyMongo) Cheat Sheet

## Install PyMongo

```bash
pip install pymongo
```

## Connect to MongoDB

```python
from pymongo import MongoClient

# Connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Access a specific database (create if not exists)
db = client['your_database_name']
```

## Insert Documents

```python
# Insert a single document into a collection
db.your_collection_name.insert_one({"key": "value"})

# Insert multiple documents into a collection
data = [{"key1": "value1"}, {"key2": "value2"}]
db.your_collection_name.insert_many(data)
```

## Query Documents

```python
# Find documents in a collection
result = db.your_collection_name.find({"key": "value"})

# Iterate over the result
for document in result:
    print(document)
```

## Update Documents

```python
# Update a single document
db.your_collection_name.update_one({"key": "value"}, {"$set": {"new_key": "new_value"}})

# Update multiple documents
db.your_collection_name.update_many({"key": "value"}, {"$set": {"new_key": "new_value"}})
```

## Delete Documents

```python
# Delete a single document
db.your_collection_name.delete_one({"key": "value"})

# Delete multiple documents
db.your_collection_name.delete_many({"key": "value"})
```

## Count Documents

```python
# Count the number of documents in a collection
count = db.your_collection_name.count_documents({})
print("Number of documents:", count)
```

## Indexing

```python
# Create an index on a specific field
db.your_collection_name.create_index([("key", pymongo.ASCENDING)])
```

## Close Connection

```python
# Close the MongoDB connection
client.close()
```

Note: Replace `your_database_name` and `your_collection_name` with the actual names of your database and collection.

This cheat sheet covers basic CRUD operations, connection handling, indexing, and more using PyMongo in Python. Customize the code as per your specific requirements.


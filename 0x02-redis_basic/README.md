# Python Redis Cheatsheet

## Introduction
Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. The `redis-py` library is a Python client for Redis.

### Installation
```bash
pip install redis
```

## Connecting to Redis

```python
import redis

# Connect to a local Redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Check connection
print("Connected:", r.ping())
```

## Key-Value Operations

### SET and GET
```python
# SET key with value
r.set('my_key', 'my_value')

# GET value by key
value = r.get('my_key')
print(value)
```

### DEL
```python
# Delete key
r.delete('my_key')
```

### EXISTS
```python
# Check if key exists
exists = r.exists('my_key')
print("Key exists:", exists)
```

## Data Types

### Strings
```python
# SET and GET string
r.set('string_key', 'Hello, Redis!')
value = r.get('string_key')
print(value)
```

### Lists
```python
# PUSH to list
r.rpush('my_list', 'item1', 'item2', 'item3')

# POP from list
item = r.lpop('my_list')
print(item)
```

### Sets
```python
# ADD to set
r.sadd('my_set', 'member1', 'member2', 'member3')

# REMOVE from set
r.srem('my_set', 'member2')
```

### Hashes
```python
# HSET and HGET for hash
r.hset('my_hash', 'field1', 'value1')
value = r.hget('my_hash', 'field1')
print(value)
```

### Sorted Sets
```python
# ZADD to sorted set
r.zadd('my_sorted_set', {'member1': 1, 'member2': 2, 'member3': 3})

# ZRANGE from sorted set
range_result = r.zrange('my_sorted_set', 0, -1, withscores=True)
print(range_result)
```

## Expiration

### EXPIRE
```python
# Set expiration time for key in seconds
r.expire('my_key', 60)
```

### TTL
```python
# Get time-to-live for key
ttl = r.ttl('my_key')
print("Time-to-live:", ttl)
```

## Pub/Sub (Publish/Subscribe)

### PUBLISH
```python
# Publish a message to a channel
r.publish('my_channel', 'Hello, Subscribers!')
```

### SUBSCRIBE
```python
import threading

def subscriber():
    pubsub = r.pubsub()
    pubsub.subscribe('my_channel')
    
    for message in pubsub.listen():
        if message['type'] == 'message':
            print("Received:", message['data'])

# Start subscriber in a separate thread
thread = threading.Thread(target=subscriber)
thread.start()
```

Remember to replace `'localhost'` and `6379` with your Redis server host and port if they are different. Customize the keys and values based on your use case.


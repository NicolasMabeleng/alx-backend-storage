#!/usr/bin/env python3

"""
Writing strings to Redis
"""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """
            Wraps calls method, adds to the function call
            count and returns the functions results
        """
        # Use the qualified name of the method as the key
        key = method.__qualname__
        # Increment the count in Redis
        self._redis.incr(key)
        # Call the original method and return its result
        result = method(self, *args, **kwargs)

        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to track input and output """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """
            Wraps calls method, adds to the function call
            count and returns the functions results
        """
        # Use the qualified name of the method as the key
        key = method.__qualname__
        # Append input arguments to the Redis list
        inputKey = f'{key}:inputs'
        self._redis.rpush(inputKey, str(args))
        # Execute the original method to get the output
        result = method(self, *args)
        # Append the output to the Redis list
        outputKey = f'{key}:outputs'
        self._redis.rpush(outputKey, result)

        return result
    return wrapper


def replay(fnc: Any) -> None:
    """ Display the history of calls of a particular function """
    key = fnc.__qualname__
    db = redis.Redis()

    # Get the call count from Redis
    callCount = db.get(fnc.__qualname__).decode('UTF-8')
    # Get the list of input arguments from Redis
    inputs = [inp.decode('UTF-8') for inp in db.lrange(f'{key}:inputs',
                                                       0, -1)]
    # Get the list of output results from Redis
    outputs = [inp.decode('UTF-8') for inp in db.lrange(f'{key}:outputs',
                                                        0, -1)]

    # Print the history of function calls, showing input,
    # arguments and output results
    print(f'{key} was called {callCount} times:')
    for inp, outp in zip(inputs, outputs):
        print(f'{key}(*{inp}) -> {outp}')


class Cache:
    """ class Cash """

    def __init__(self) -> None:
        """ Constructor """
        # Create an instance of the Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Add key/value to redis database """
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the input data in Redis using the random key
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Get value by key from redis database """
        val = self._redis.get(key)

        if not val:
            return
        if fn is int:
            return self.get_int(val)
        if fn is str:
            return self.get_str(val)
        if callable(fn):
            return fn(val)

        return val

    def get_str(self, value: Any) -> str:
        """ Convert given value to a string """
        return value.decode('UTF-8')

    def get_int(self, value: Any) -> int:
        """ Convert given value to an integer """
        return int(value)

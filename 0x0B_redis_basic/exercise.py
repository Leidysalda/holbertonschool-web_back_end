#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count Calls method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrappers"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper"""
        inputs = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inputs)
        outputs = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)
        return outputs
    return wrapper


def replay(fn: Callable):
    """ Replay"""
    redis = fn.__self__._redis
    value = fn.__qualname__
    count = redis.get(value).decode("utf-8")
    print(f"{value} was called {count} times:")
    inputs = redis.lrange(value + ":inputs", 0, -1)
    outputs = redis.lrange(value + ":outputs", 0, -1)
    merge_list = list(zip(inputs, outputs))
    for inp, out in merge_list:
        argument, data = inp.decode("utf-8"), out.decode("utf-8")
        print(f"{value}({argument}*) -> {data}")


class Cache:
    """ Class cache"""
    def __init__(self):
        """ Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store method"""
        my_key = str(uuid.uuid4())
        self._redis.set(my_key, data)
        return my_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Get """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str):
        """ Get str """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str):
        """ Get int"""
        dat = self._redis.get(key)
        try:
            return int(data.decode("utf-8"))
        except Exception:
            return 0

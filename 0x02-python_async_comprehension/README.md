# 0x02. Python - Async Comprehension

Python 3.6 added the ability to create Asynchronous Comprehensions and Asynchronous Generators. You can read about asynchronous comprehension in PEP 530 while the asynchronous generators are described in PEP 525. The documentation states that you can now create asynchronous list, set and dict comprehensions and generator expressions. Their example looks like this:

result = [i async for i in aiter() if i % 2]
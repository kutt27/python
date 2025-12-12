# 🐍 The Ultimate Python Challenge List

A collection of **100** conceptual and practical exercises to master Modern Python.
**Rules**: solving these requires writing code, but the focus is on the *concepts*.

---

## 🟢 Part 1: Python Basics & Logic (1-15)

1.  **The FizzBuzz Twist**
    *   **Challenge**: Write a program that prints 1 to 100. Multiples of 3: "Fizz". Multiples of 5: "Buzz". Multiples of both: "FizzBuzz". **Constraint**: Do not use the `%` (modulo) operator.
    *   **Hint**: Maintain counters or use purely arithmetic checks loops.

2.  **Palindrome Detector (Recursive)**
    *   **Challenge**: Check if a string is a palindrome without using valid string slicing (e.g. `s[::-1]`) or loops.
    *   **Hint**: Compare first/last chars, then recurse on the middle substring.

3.  **Dictionary Inverter**
    *   **Challenge**: Swap keys and values in a dictionary. If values are duplicates, list all original keys for that value.
    *   **Hint**: `defaultdict(list)` is your friend.

4.  **Flatten the List**
    *   **Challenge**: Take a list containing arbitrarily nested lists `[1, [2, [3, 4], 5]]` and return a single flat list `[1, 2, 3, 4, 5]`.
    *   **Hint**: Recursion or a stack-based approach.

5.  **Anagram Grouper**
    *   **Challenge**: Given a list of words, group them by anagrams. `["eat", "tea", "tan", "ate", "nat", "bat"]` -> `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`.
    *   **Hint**: Sort the letters of each word to use as a dictionary key.

6.  **Matrix Transpose**
    *   **Challenge**: Flip a 2D matrix (list of lists) over its diagonal (rows become columns). One liner preferred.
    *   **Hint**: `zip(*matrix)` unpacking trick.

7.  **Run Length Encoding**
    *   **Challenge**: Compress "AAAABBBCCDAA" to "4A3B2C1D2A".
    *   **Hint**: `itertools.groupby` makes this trivial.

8.  **Prime Generator**
    *   **Challenge**: Write a generator that yields infinite prime numbers.
    *   **Hint**: Keep a cache of found primes to check divisibility.

9.  **Valid Parentheses**
    *   **Challenge**: Verify if `{[()]}` is valid, but `([)]` is not.
    *   **Hint**: Use a stack (list) to push openers and pop closers.

10. **Custom Sort Order**
    *   **Challenge**: Sort a list of strings based on the *second* letter. If second letters are same, sort by length.
    *   **Hint**: `sorted(list, key=lambda s: (s[1], len(s)))`.

11. **Find Duplicates Avoid Set**
    *   **Challenge**: Find duplicate numbers in a list without using `set()`. Constraints: O(N) time or O(1) space?
    *   **Hint**: If numbers are in range 1..N, you can use index marking. Otherwise, use a `dict`.

12. **String Rotation**
    *   **Challenge**: Check if "waterbottle" is a rotation of "erbottlewat".
    *   **Hint**: "waterbottle" is a substring of "erbottlewat" + "erbottlewat" ? No, other way around. `(s1+s1).contains(s2)`.

13. **List Intersection**
    *   **Challenge**: Find common elements in two lists using list comprehensions only.
    *   **Hint**: `[x for x in list1 if x in list2]`. O(N*M) complexity warning.
    
14. **Yield From**
    *   **Challenge**: Create a generator that flattens a list of iterables using `yield from`.
    *   **Hint**: `yield from sublist`.
    
15. **Context Manager Timer**
    *   **Challenge**: Write a context manager that prints the execution time of a code block.
    *   **Hint**: Implement `__enter__` (record start) and `__exit__` (print end - start).

---

## 🔵 Part 2: Functions & Decorators (16-30)

16. **The Retry Decorator**
    *   **Challenge**: Create `@retry(times=3)` which retries the decorated function on failure.
    *   **Hint**: Write a decorator factory (function returning a decorator). Use `try/except` looping.

17. **Memoization from Scratch**
    *   **Challenge**: Write `@cache_result`. If called with same arguments, return cached result. Do not use `functools.lru_cache`.
    *   **Hint**: Attach a `cache = {}` dictionary to the wrapper function.

18. **Type Enforcer**
    *   **Challenge**: A decorator that checks input arguments against function type hints. Raise error if mismatched.
    *   **Hint**: Use `func.__annotations__` and `isinstance()`.

19. **Single Dispatch**
    *   **Challenge**: Write a function `process(data)` that behaves differently if `data` is `int`, `list`, or `str` using `functools.singledispatch`.
    *   **Hint**: `@singledispatch` on base, `@process.register(int)` on others.

20. **Currying Function**
    *   **Challenge**: Write a generic `curry` function that transforms `f(a, b, c)` into `curried(a)(b)(c)`.
    *   **Hint**: Return lambda checking argument count vs `code object` co_argcount.

21. **Access Control Decorator**
    *   **Challenge**: `@requires_role('admin')` which checks a global `CURRENT_USER` dict.
    *   **Hint**: Standard decorator factory pattern.

22. **Function Introspection**
    *   **Challenge**: Write a function that prints all variable names defined *inside* another function.
    *   **Hint**: `func.__code__.co_varnames`.

23. **Default Mutable Argument Trap**
    *   **Challenge**: Create a function with `def f(l=[])`. Show how it persists state. Then fix it.
    *   **Hint**: Use `None` as default, then `l = [] if l is None else l`.

24. **Star-Args Proxy**
    *   **Challenge**: Write a wrapper that passes all args/kwargs to another function but prints them first.
    *   **Hint**: `*args` and `**kwargs`.

25. **Rate Limiter**
    *   **Challenge**: A decorator ensuring a function is called at most once per second.
    *   **Hint**: Store `last_called` timestamp.

26. **Output Transformer**
    *   **Challenge**: A decorator `@jsonify` that converts the function's dict return value to a JSON string.
    *   **Hint**: `json.dumps(result)`.

27. **Partial Application**
    *   **Challenge**: Use `functools.partial` to create a `power_of_two` function from `math.pow`.
    *   **Hint**: `partial(pow, exp=2)`... wait, base or exp? Partial binds left-to-right usually.

28. **Recursive Lambda**
    *   **Challenge**: Write a factorial function using ONLY a lambda assignment.
    *   **Hint**: You might need a Y-combinator logic or passing the lambda to itself, or simpler: assignment to variable name.

29. **Scope Detective**
    *   **Challenge**: Demonstrate accessing `nonlocal` vs `global` variables in nested functions.
    *   **Hint**: Nested function modifying counter in outer function.

30. **Method Decorator**
    *   **Challenge**: Write a decorator that works on class methods (handling `self` correctly).
    *   **Hint**: `functools.wraps` usually handles this, but be aware of the instance being the first arg.

---

## 🟣 Part 3: Object-Oriented Programming (31-50)

31. **Singleton Pattern**
    *   **Challenge**: Implement a class where only ONE instance ever exists.
    *   **Hint**: Override `__new__` to store and return a class-level instance.

32. **Attribute Validation (Descriptors)**
    *   **Challenge**: Create a descriptor `Integer` that ensures an attribute is always an int.
    *   **Hint**: Implement `__get__` and `__set__` in a separate class.

33. **Custom Context Manager (Class)**
    *   **Challenge**: A class `FileOpener` that works with `with`. Handles exceptions by printing them but not suppressing.
    *   **Hint**: `__enter__` returns file, `__exit__` handles cleanup. Return `False` to propagate error.

34. **Magic Method Math**
    *   **Challenge**: Create a `Vector` class supporting `v1 + v2`, `v1 * 5` (scalar), and `len(v1)`.
    *   **Hint**: `__add__`, `__mul__`, `__len__`.

35. **The Container Protocol**
    *   **Challenge**: Create a class `Bookshelf` that supports `book in shelf` and iteration `for b in shelf`.
    *   **Hint**: `__contains__`, `__iter__`.

36. **Property Computed Fields**
    *   **Challenge**: Class `Rectangle` with `width`/`height`. `area` is a property. Setting `area` should resize the rectangle (keeping aspect ratio? or fixed width?).
    *   **Hint**: `@property` getter and setter.

37. **Abstract Base Classes**
    *   **Challenge**: Define `Animal` with abstract `speak`. Enforce subclasses to implement it.
    *   **Hint**: Inherit `ABC`, decorate `speak` with `@abstractmethod`.

38. **Multiple Inheritance & MRO**
    *   **Challenge**: Create a Diamond Inheritance structure. Predict and verify the resolution order.
    *   **Hint**: `Class.mro()`. Use `super()`.

39. **Metaclass Registry**
    *   **Challenge**: A metaclass that automatically adds every created class to a global `registry` list.
    *   **Hint**: Override `__new__` or `__init__` in the metaclass type.

40. **Slots Optimization**
    *   **Challenge**: Create a class with `__slots__`. Try to add a dynamic attribute at runtime (it should fail).
    *   **Hint**: `__slots__ = ['x', 'y']`. Saves memory.

41. **Dependency Injection**
    *   **Challenge**: A `Car` class that accepts an `Engine` instance in `__init__`. Swap engines (Electric/Gas).
    *   **Hint**: Polymorphism. `Car` waits for `engine.start()`.

42. **Operator Overloading (Comparisons)**
    *   **Challenge**: Make `User` objects sortable by age.
    *   **Hint**: `functools.total_ordering` and implement `__lt__` (less than).

43. **Object Copying**
    *   **Challenge**: Implement `__copy__` and `__deepcopy__` for a class.
    *   **Hint**: `copy` module hooks.

44. **Dynamic Attributes**
    *   **Challenge**: A class `APIWrapper` that handles any method call dynamically (e.g. `api.get_users()` becomes a request to `/get_users`).
    *   **Hint**: `__getattr__`.

45. **Format Protocol**
    *   **Challenge**: Customize how your object looks in f-strings with `f"{obj:short}"` vs `f"{obj:long}"`.
    *   **Hint**: `__format__`.

46. **Callable Objects**
    *   **Challenge**: Create a class `Adder` initialized with `n`. Calling `instance(x)` returns `x+n`.
    *   **Hint**: `__call__`.

47. **Mixin Pattern**
    *   **Challenge**: Create a `JsonSerializableMixin` that gives any class a `.to_json()` method.
    *   **Hint**: Multiple inheritance. Mixin generic logic.

48. **Class vs Instance Attributes**
    *   **Challenge**: Demonstrate the danger of mutable class attributes (shared across instances).
    *   **Hint**: `list` defined at class level.

49. **Dataclasses**
    *   **Challenge**: Rewrite a complex `__init__`/`__repr__`/`__eq__` class using `@dataclass`.
    *   **Hint**: `frozen=True` if possible.

50. **Proxy Pattern**
    *   **Challenge**: Create a `ReadOnlyProxy` that wraps an object and prevents `__setattr__`.
    *   **Hint**: Override `__setattr__` to raise error, delegate `__getattr__`.

---

## 🟡 Part 4: Concurrency & Async (51-75)

51. **Thread vs Process**
    *   **Challenge**: Run a CPU-heavy task with Threads, then Processes. Compare time.
    *   **Hint**: `threading.Thread` (GIL limits) vs `multiprocessing.Process`.

52. **Producer-Consumer Queue**
    *   **Challenge**: One thread produces numbers, two threads consume and print them using `queue.Queue`.
    *   **Hint**: `queue.get()` blocks. Send `None` as poison pill to stop.

53. **Deadlock Simulation**
    *   **Challenge**: Create a deadlock using two Locks and two threads.
    *   **Hint**: T1 holds A needs B. T2 holds B needs A.

54. **Race Condition**
    *   **Challenge**: 100 threads increment a global int 1000 times. Observe partial sum. Fix with Lock.
    *   **Hint**: `x += 1` is not atomic.

55. **ThreadPool Scraper**
    *   **Challenge**: Simulate scraping 10 URLs using `ThreadPoolExecutor`.
    *   **Hint**: `executor.map(fetch, urls)`.

56. **Daemon Threads**
    *   **Challenge**: A thread prints "Heartbeat" every second. Main program sleeps 3s then exits. Thread should die with Main.
    *   **Hint**: `daemon=True`.

57. **Async Hello World**
    *   **Challenge**: Write an `async` function that waits 1s then prints "Hello". Run it.
    *   **Hint**: `asyncio.run(main())`.

58. **Gathering Tasks**
    *   **Challenge**: Run 3 async tasks concurrently (1s, 2s, 1s durations). Total time should be ~2s.
    *   **Hint**: `asyncio.gather()`.

59. **Async Timeout**
    *   **Challenge**: Run a task that sleeps 5s. Set a timeout of 2s. Catch the error.
    *   **Hint**: `asyncio.wait_for()`.

60. **Sync Blocking Async**
    *   **Challenge**: Call `time.sleep(2)` inside an async function. Observe the freeze. Fix it with `run_in_executor`.
    *   **Hint**: Loop blocked = bad. Offload to thread.

61. **Async Context Manager**
    *   **Challenge**: Async connection class `async with DBConnection() as db:`.
    *   **Hint**: `__aenter__` and `__aexit__`.

62. **Async Iterator**
    *   **Challenge**: Make a class iterable with `async for`. Yields numbers with delays.
    *   **Hint**: `__aiter__` and `__anext__`.

63. **Task Cancellation**
    *   **Challenge**: Start a task. Sleep 1s. Cancel it. Handle `CancelledError` inside the task to cleanup.
    *   **Hint**: `task.cancel()`.

64. **Shared State Async**
    *   **Challenge**: Increment shared counter in async tasks. Use `asyncio.Lock` to fix races.
    *   **Hint**: Even async needs locks for logic spanning multiple awaits.

65. **Process Pool Math**
    *   **Challenge**: Use `ProcessPoolExecutor` to calculate squares of a massive list.
    *   **Hint**: `chunksize` helps performance.

66. **Event Objects**
    *   **Challenge**: T1 waits for T2 to set an event before proceeding.
    *   **Hint**: `threading.Event` or `asyncio.Event`.

67. **Semaphore Limiting**
    *   **Challenge**: Limit max concurrent downloads to 3 using a Semaphore.
    *   **Hint**: `async with semaphore:`.

68. **Barrier Synchronization**
    *   **Challenge**: 3 threads "prepare". Wait for all 3 to reach barrier before "starting".
    *   **Hint**: `threading.Barrier(3)`.

69. **Multiprocessing Pipe**
    *   **Challenge**: Send complex object from Parent to Child process via Pipe.
    *   **Hint**: `conn1, conn2 = multiprocessing.Pipe()`.

70. **Shared Memory Array**
    *   **Challenge**: Share an array of integers between processes without copying.
    *   **Hint**: `multiprocessing.Array`.

71. **Actor Model (Queue)**
    *   **Challenge**: Create an "Actor" process that listens to a Queue for messages (commands) and acts.
    *   **Hint**: `while True: msg = q.get()`.

72. **Async Generator Pipeline**
    *   **Challenge**: Generator 1 yields lines. Generator 2 processes. Chained via logical async iteration.
    *   **Hint**: `async for` inside another `async def`.

73. **Fire and Forget**
    *   **Challenge**: Spawn a task that runs in background while main response returns immediately.
    *   **Hint**: `create_task`. Don't await immediately.

74. **Subprocess Management**
    *   **Challenge**: Run a shell command (`ls -la`) from Python using `asyncio.create_subprocess_shell`.
    *   **Hint**: Capturing stdout.

75. **Async Queue**
    *   **Challenge**: Async Producer-Consumer using `asyncio.Queue`.
    *   **Hint**: `await q.put()`, `await q.get()`.

---

## 🟠 Part 5: Functional Programming (76-88)

76. **Pure Functions**
    *   **Challenge**: Refactor a function that uses a global list `history` to store calls, making it pure.
    *   **Hint**: Return the new history along with result.

77. **Immutable Transformation**
    *   **Challenge**: Use `NamedTuple`. "Change" a field by creating a fresh copy.
    *   **Hint**: `_replace()` method or constructor.

78. **Deep Flatten (Recursive)**
    *   **Challenge**: Flatten `[1, [2, [3, [4]]]]` of unknown depth.
    *   **Hint**: If item is list, yield from `recursive_flatten(item)`.

79. **Partial Powers**
    *   **Challenge**: Use `partial` to make `square`, `cube`, `quart` from `pow`.
    *   **Hint**: `functools.partial`.

80. **Function Composition**
    *   **Challenge**: Write `compose(f, g)` returning `f(g(x))`. Use it to clean string -> int -> square.
    *   **Hint**: `lambda x: f(g(x))`.

81. **Filter Map Reduce Chain**
    *   **Challenge**: Take list of users. Filter active. Map to age. Reduce to average.
    *   **Hint**: Functional pipeline.

82. **Infinite Counter**
    *   **Challenge**: Use `itertools.count` to generate IDs for a list of data.
    *   **Hint**: `zip(itertools.count(), data)`.

83. **Group By Date**
    *   **Challenge**: Given list of timestamps, count events per day using `groupby`.
    *   **Hint**: Sort by date first!

84. **Curried Adder**
    *   **Challenge**: Write `add(x)(y)` that returns x+y.
    *   **Hint**: Function returning a function.

85. **Tail Recursion logic**
    *   **Challenge**: Write factorial using accumulator style.
    *   **Hint**: `fact(n, acc)`.

86. **Method Chaining**
    *   **Challenge**: Create class `Query` where `q.filter().order_by().execute()` works.
    *   **Hint**: Each method returns `self` (or new instance for immutability).

87. **Lazy Evaluation**
    *   **Challenge**: Implement a generator that computes fibonacci numbers ONLY when requested.
    *   **Hint**: `yield` pauses execution.

88. **Monad: Maybe**
    *   **Challenge**: Create a `Maybe` class. If value is None, `.bind(func)` does nothing. If value exists, it runs func.
    *   **Hint**: `Just` and `Nothing` subclasses.

---

## 🔴 Part 6: Pydantic & Architecture (89-100)

89. **Validate User JSON**
    *   **Challenge**: Use Pydantic `BaseModel` to validate a user dict. Ensure email is valid.
    *   **Hint**: `EmailStr` type.

90. **Environment Settings**
    *   **Challenge**: Create `AppSettings` that loads `DB_URL` from env var.
    *   **Hint**: `BaseSettings` from pydantic-settings.

91. **Nested Validation**
    *   **Challenge**: Validate `Blog(title, Author(name, age))`.
    *   **Hint**: Model as field type.

92. **Custom Validator**
    *   **Challenge**: Ensure `password` contains "!" using `@field_validator`.
    *   **Hint**: Check value, raise `ValueError` if fail.

93. **Model Dump modes**
    *   **Challenge**: Export model to dict, but exclude `secret_key`.
    *   **Hint**: `exclude={'secret_key'}`.

94. **Strict Types**
    *   **Challenge**: Configure Pydantic to fail if string "123" is passed to int field (no coercion).
    *   **Hint**: `strict=True` in Field or Config.

95. **Computed Field**
    *   **Challenge**: Add `age_group` (Child/Adult) to model output based on `age` field. Matches exported JSON.
    *   **Hint**: `@computed_field`.

96. **Generic Response Model**
    *   **Challenge**: Create `Response[T]` that wraps any data model in `{"data": ...}`.
    *   **Hint**: `Generic[T]`.

97. **Recursive Category**
    *   **Challenge**: Validate a Category tree (Category has list of Categories).
    *   **Hint**: `List['Category']`.

98. **Alias Usage**
    *   **Challenge**: Map JSON field `fistName` (camelCase) to Python `first_name` (snake_case).
    *   **Hint**: `alias` argument.

99. **Factory Default**
    *   **Challenge**: Field `created_at` should default to `now()` when object created.
    *   **Hint**: `default_factory=datetime.now`.

100. **The Final Architecture**
     *   **Challenge**: Sketch (interfaces/classes) a "Task Processor".
         - Input: Pydantic Model.
         - Processing: Async function.
         - Storage: Abstract Base Class (save to implementation).
         - Logic: Clean Architecture (Domain | Data | API).
     *   **Hint**: Combine everything: ABCs, Async, Types, Pydantic.

---

### 🏆 Congratulations! 
If you can solve these 100 challenges, you are in a good position compared to most of Python developers.

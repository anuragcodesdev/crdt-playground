# TypeScript Notes

## Strong vs Static Typing

TypeScript is a statically typed language that adds type checking on top of JavaScript.

Types are checked during compile time, meaning many errors are caught before the program runs.

Example:

```ts
function add(a: number, b: number) {
  return a + b;
}

add("5", 10); // TypeScript error
```
In Python, types are checked at runtime because Python is dynamically typed.

Example:

```python
def add(a, b):
    return a + b

add("5", 10) # Runs until Python hits an invalid operation
```

Static typing helps catch mistakes earlier and improves code readability and tooling.
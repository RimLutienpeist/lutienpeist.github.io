# Reference

#### Declaring

```cpp
int & a = b;
```

#### Rules

1. References must be initialized when defined
2. Bindings don’t change at run time, unlike pointers
3. The target of a reference must have a location!
4. No references to references
5. No pointers to references
   1. `int&* p; // illegal`
   2. Reference to pointer is ok
6. No arrays of references

#### Pointers vs. References

| References                                                   | Pointers                                   |
| ------------------------------------------------------------ | ------------------------------------------ |
| can't be null                                                | can be set to null                         |
| are dependent on an existing variable, they are an alias for an variable | pointer is independent of existing objects |
| can't change to a new "address" location                     | can change to point to a different address |


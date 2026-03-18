"""

Call Stack (simple definition):
Call stack is a **memory structure that stores function calls** in order, so the program knows **which function is running and where to return after it finishes**.

---

### ⚡ Even simpler

* When a function is called → it is **pushed** onto the stack
* When it finishes → it is **popped** (removed)

---

### 🧠 Example (recursion)
"""


def funcThree():
    print("Three")


def funcTwo():
    funcThree()
    print("Two")


def funcOne():
    funcTwo()
    print("One")

funcOne()

### 🔑 Key idea
# **Last In, First Out (LIFO)** – last function called finishes first.

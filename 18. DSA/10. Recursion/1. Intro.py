"""
Recursion means a **function calling itself** to solve a problem step by step.

Every recursive function must have **2 parts**:

---

### 1. Base Case (Stopping Condition)

* This tells the function **when to stop calling itself**
* Without this → infinite recursion (program crash)

---

### 2. Recursive Case

* This is where the function **calls itself again**
* It keeps reducing the problem

---

## 🎁 Simple Example: Open Gift Box

Problem:
You have a gift box.

* If you find a **ball → return it**
* If not → open the next gift box inside

---
"""

### Python Code

def openGiftBox(box):
    # Base case: if ball found, stop recursion
    if box == "ball":
        return "Found the ball 🎉"
    
    # Recursive case: open next box
    return openGiftBox(box - 1)


# Example: starting with 5 nested boxes
print(openGiftBox(5))


### How it Works Step-by-Step
"""
openGiftBox(5)
→ openGiftBox(4)
→ openGiftBox(3)
→ openGiftBox(2)
→ openGiftBox(1)
→ openGiftBox("ball")  ✅ Base case reached
```

Then it returns back step by step.

---

# 🔥 More Realistic Version (Better Understanding)
"""

def openGiftBox(boxes):
    # Base case
    if boxes == 0:
        print("🎉 Found the ball!")
        return
    
    print(f"Opening box {boxes}")
    
    # Recursive case
    openGiftBox(boxes - 1)


openGiftBox(5)

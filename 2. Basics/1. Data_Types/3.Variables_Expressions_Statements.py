# Below are **very simple, short, practical notes** converted from your transcript.
# No emojis, no decoration — **clean notes suitable for VS Code / GitHub**.

# ---

# # Python Variables – Short Notes

# ## What is a Variable?

# * A **variable stores data** in a program.
# * Used to save values like user input, results, or temporary data.
# * Variables help programs **remember information**.

# ### Example

# ```python
# iq = 190
# print(iq)
# ```

# * `iq` is the variable
# * `190` is the value stored
# * `=` means assignment

# ---

# ## Why Variables Are Important

# * Store data
# * Reuse data
# * Perform calculations
# * Make programs dynamic

# Example:

# ```python
# user_age = iq / 4
# print(user_age)
# ```

# ---

# ## Variable Naming Rules (Python)

# ### 1. Snake Case (Best Practice)

# * Use lowercase letters
# * Use `_` instead of spaces

# ```python
# user_iq = 120
# ```

# ❌ Bad:

# ```python
# User IQ = 120
# ```

# ---

# ### 2. Valid Characters

# * Letters (a–z)
# * Numbers (0–9)
# * Underscore (_)

# Rules:

# * Must start with a **letter or underscore**
# * Cannot start with a number

# ❌ Invalid:

# ```python
# 1age = 25
# ```

# ✅ Valid:

# ```python
# age1 = 25
# ```

# ---

# ### 3. Case Sensitive

# ```python
# age = 20
# Age = 30
# ```

# * `age` and `Age` are **different variables**

# ---

# ### 4. Cannot Use Keywords

# Python keywords already have meaning.

# ❌ Invalid:

# ```python
# print = 10
# ```

# Examples of keywords:

# * `print`
# * `if`
# * `else`
# * `for`
# * `while`

# ---

# ## Assigning & Reassigning Variables

# Variables can change values.

# ```python
# score = 50
# score = 80
# ```

# Latest value overwrites the old one.

# ---

# ## Using Variables in Calculations

# ```python
# iq = 100
# user_age = iq / 5
# print(user_age)
# ```

# ---

# ## Constants (Convention)

# * Written in **ALL CAPS**
# * Means value should not change

# ```python
# PI = 3.14
# ```

# Note: Python does NOT enforce constants — this is a convention only.

# ---

# ## Double Underscore Variables (Dunder)

# * Example: `__init__`
# * Reserved for Python internals
# * Do NOT create your own unless you know what you’re doing

# ---

# ## Multiple Assignment (Shortcut)

# ```python
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# ```

# ---

# ## Good Variable Naming

# * Be descriptive
# * Code should read like English

# ❌ Bad:

# ```python
# x = 10
# ```

# ✅ Good:

# ```python
# user_score = 10
# ```

# ---

# # Expressions vs Statements

# ## Expression

# * Produces a value

# ```python
# iq / 5
# ```

# This evaluates to a number.

# ---

# ## Statement

# * A full line that performs an action

# ```python
# user_age = iq / 5
# ```

# Action:

# * Calculate
# * Assign
# * Store value

# ---

# ## Summary

# * **Expression** → produces a value
# * **Statement** → performs an action

# ---

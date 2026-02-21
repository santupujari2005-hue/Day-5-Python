# 📘 Python Notes – Sets & Dictionaries

This file contains notes based on my practice programs covering:
- Sets in Python
- Set Methods
- Dictionaries
- Dictionary Methods
- Practice Problems

---

# 🔹 1️⃣ Sets in Python

## 📌 What is a Set?

A **set** is a collection of unique elements.

```python
collection = {1, 2, 3, 4, "Santosh", "hello", 2}
print(collection)
```

### ✅ Important Properties:
- Unordered
- No duplicate values
- Mutable
- Cannot access using index

---

## 📌 Creating an Empty Set

```python
collection = set()
```

⚠ `{}` creates an empty dictionary, NOT a set.

---

# 🔹 2️⃣ Set Methods

## 📌 add()

Adds an element to the set.

```python
collection.add(10)
```

---

## 📌 remove()

Removes a specific element.

```python
collection.remove(10)
```

⚠ Gives error if element not present.

---

## 📌 clear()

Removes all elements from set.

```python
collection.clear()
```

---

## 📌 pop()

Removes a random element.

```python
collection.pop()
```

---

## 📌 union()

Combines two sets and returns a new set.

```python
set1.union(set2)
```

---

## 📌 intersection()

Returns common elements between sets.

```python
set1.intersection(set2)
```

---

# 🔹 3️⃣ Dictionaries in Python

## 📌 What is a Dictionary?

A dictionary stores data in **key : value** pairs.

```python
dict_1 = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}
```

### ✅ Properties:
- Unordered
- Mutable
- Keys must be unique
- Access using keys

---

## 📌 Adding Data to Dictionary

```python
marks = {}
marks.update({"phy": 90})
```

---

## 📌 Accessing Values

```python
print(marks["phy"])
```

---

# 🔹 4️⃣ Practical Concepts

## 📌 Counting Unique Subjects Using Set

```python
subjects = {"python", "java", "c++", "python"}
print(len(subjects))
```

Sets automatically remove duplicates.

---

## 📌 Store 9 and 9.0 Separately in Set

```python
values = {
    ("float", 9.0),
    ("int", 9)
}
```

Using tuple helps differentiate values.

---

# 🔥 Important Learning Points

- Sets remove duplicate values automatically.
- Sets do not support indexing.
- `{}` creates dictionary, not set.
- Dictionary keys must be unique.
- Use `set()` for empty set.
- Use `update()` to add key-value pairs.

---

# 🚀 Learning Progress

- Lists ✅
- Strings ✅
- Conditional Statements ✅
- Sets ✅
- Dictionaries ✅

Next Step: Functions & DSA Basics 💪🔥

---

Santosh Pujari  
Python Learning Journey 🚀
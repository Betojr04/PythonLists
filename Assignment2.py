"""'
TASK 1:
You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.
"""

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

where_is_alice = "Alice" in submitted and "Alice" in attended

print(where_is_alice)

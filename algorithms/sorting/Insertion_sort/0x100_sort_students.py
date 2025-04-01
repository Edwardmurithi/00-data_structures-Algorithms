def insertion_sort_students(students):
    """
    Sorts students first by descending score, then by name in ascending order.
    :param students: List of tuples (name, score)
    :return: Sorted list of students
    """
    n = len(students)
    for j in range(1, n):
        key = students[j]  # (name, score)
        i = j - 1

        # Sort by descending score, and if scores are equal, sort by name (ascending)
        while i >= 0 and (students[i][1] < key[1] or (students[i][1] == key[1] and students[i][0] > key[0])):
            students[i + 1] = students[i]  # Shift element to the right
            i -= 1

        students[i + 1] = key  # Insert the key at the correct position

    return students

# Example Usage
if __name__ == "__main__":
    student_records = [
        ("Alice", 85),
        ("Bob", 90),
        ("Charlie", 85),
        ("David", 95),
        ("Eve", 90),
        ("Frank", 80)
    ]

    print("Before sorting:")
    for student in student_records:
        print(student)

    sorted_students = insertion_sort_students(student_records)

    print("\nAfter sorting:")
    for student in sorted_students:
        print(student)

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read()
        lines = text.splitlines()
        total = 0
        for line in lines:
            parts = line.split(",")
            salary = float(parts[1])
            total += salary
        if len(lines) == 0:
            return 0, 0
        average = total / len(lines)
        return total, average
    except FileNotFoundError:
        return 0, 0
    except (ValueError, IndexError):
        return 0, 0
total, average = total_salary(r"C:\project\path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
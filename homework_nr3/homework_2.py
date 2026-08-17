def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        cats_info = []
        for line in lines:
            parts = line.strip().split(",")
            cat_id = parts[0]
            name = parts[1]
            age = parts[2]
            cats_info.append({
                "id": cat_id,
                "name": name,
                "age": age
            })
        return cats_info
    except FileNotFoundError:
        return []
    except (ValueError, IndexError):
        return []
    
cats_info = get_cats_info(r"C:\project\cats.txt")

for cat in cats_info:
    print(cat)
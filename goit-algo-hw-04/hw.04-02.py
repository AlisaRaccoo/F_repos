def get_cats_info(path):
    cats_info = []  
    
   
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                cat_info = {
                    'ID': parts[0],
                    'Name': parts[1],
                    'Age': int(parts[2])  
                }
                cats_info.append(cat_info)
    
    return cats_info

path_to_file = "/Users/Raccoo/Desktop/Temp 2.txt"  
cats_info = get_cats_info(path_to_file)
for cat in cats_info:
    print(cat)

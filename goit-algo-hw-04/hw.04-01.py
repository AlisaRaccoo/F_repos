def total_salary(path):
    total_salary = 0
    employee_count = 0
    
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                salary = float(parts[1])
                total_salary += salary
                employee_count += 1
    

    average_salary = total_salary / employee_count if employee_count > 0 else 0
    
    
    return total_salary, average_salary


path_to_file = "/Users/Raccoo/Desktop/Temp.txt"  
total, average = total_salary(path_to_file)
print("Total salary:", total)
print("Average salary:", average)


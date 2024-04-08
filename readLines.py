def read_list_from_file(file_name):
    with open(file_name, 'r') as f:
        numbers = f.read().split()
        numbers = [float(num) for num in numbers]
    return numbers

def write_list_to_file(file_name, numbers):
    with open(file_name, 'w') as f:
        for num in numbers:
            f.write('%.2f\n' % num)

input_file = ".\\user_data\\24-file-time.txt"
output_file = ".\\user_data\\newFile.txt"

numbers = read_list_from_file(input_file)

sum_of_five = []
for i in range(0, len(numbers), 5):
    number = sum(numbers[i:i+5])/ 5
    sum_of_five.append(number)


write_list_to_file(output_file, sum_of_five)

# Проверка
print(sum_of_five)
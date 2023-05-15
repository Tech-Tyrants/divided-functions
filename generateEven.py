def generate_even_numbers():
    even_numbers = []
    for num in range(4, 31):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Example usage
result = generate_even_numbers()
print(result)

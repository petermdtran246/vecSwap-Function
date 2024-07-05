def vecSwap(vector):
    # Swap elements in pair
    n = len(vector)
    for i in range(0, n, 2):
        vector[i], vector[i+1] = vector[i + 1], vector[i]

def get_even_integer():
    while 1:
        try:
            num = int(input('Enter an even integer between 9 and 21: '))
            if 9 <= num <= 21 and num % 2 == 0:
                return num
            else:
                print('Invalid input. Please enter an even integer between 9 and 21')
        except ValueError:
            print('Invalid input. Please enter an even integer between 9 and 21')

# Get even integer from the user
even_integer = get_even_integer()
# Create a vector with the specified size and convert this sequence into a list
vector = list(range(even_integer))
# Print Original Vector
print(f'Original vector: {vector}')
# Swap element in pairs
vecSwap(vector)
# Print Swapped Vector
print(f'Swapped vector: {vector}')





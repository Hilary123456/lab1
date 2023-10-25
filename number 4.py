def esc(code):
    return f'\u001b[{code}m'

RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)

# Read the sequence from sequence.txt
with open('sequence.txt', 'r') as sequence_file:
    sequence = [float(line.strip()) for line in sequence_file]


filtered_sequence = [x for x in sequence if x > 5 or x < -5]

# Create the histogram
histogram = [0] * 10 

for value in filtered_sequence:
    bin_index = int(value)  
    histogram[bin_index] += 1

# Print the histogram using escape sequences
for i, count in enumerate(histogram):
    bin_range = f'{i}-{i + 1}'  
    bar = f'{BLUE}{"*" * count}{END}'  
    print(f'{bin_range}: {bar}')

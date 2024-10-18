colours = []
leng = int(input("Enter the numbers of colours to enter:\n"))
print(f"Enter {leng} colours:")
for i in range(leng):
    temp = input()
    colours.append(temp)
print(f"Colour list:{colours}")
print(f"First colour in the list:{colours[0]}\nLast colour in the list:{colours[leng-1]}")

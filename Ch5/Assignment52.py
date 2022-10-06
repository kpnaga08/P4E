largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        val = int(num)
        if largest is None or largest < val:
            largest = val
        elif smallest is None or smallest > val :
            smallest = val
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
    
print("Minimum is", smallest)
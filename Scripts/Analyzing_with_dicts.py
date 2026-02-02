#pure winging this one
#this has caused irreversible psychological damage

raw_numbers = input("Please enter all numbers separated by space: ")
parts = raw_numbers.split()
numbers = []


def analyze_dict(numbers):
    amount = 0
    min_count = None
    max_count = None
    average = 0
    even_count = 0
    odd_count = 0

    for p in parts:
        try:
            value = int(p)
            numbers.append(value)
        except:
            print(f"{p} is not a valid number")
            continue

        amount += value

        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if min_count is None:
            min_count = value
        else:
            if value < min_count:
                min_count = value

        if max_count is None:
            max_count = value
        else:
            if value > max_count:
                max_count = value

    average = amount / len(numbers)

    results = {
        "amount": amount,
        "min": min_count,
        "max": max_count,
        "average": average,
        "even_count": even_count,
        "odd_count": odd_count
    }

    return results


print(analyze_dict(numbers))
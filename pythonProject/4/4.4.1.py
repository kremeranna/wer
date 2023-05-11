def lucky(num):
    half_len = len(num) // 2
    first_half = num[:half_len]
    second_half = num[half_len:]
    return sum(map(int, first_half)) == sum(map(int, second_half))

ticket1 = '385916'
ticket2 = '231002'

print(lucky(ticket1))
print(lucky(ticket2))
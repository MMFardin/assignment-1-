def  num_li(number):
    even_sum=0
    odd_sum=0
    for i in number:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i

    return even_sum, odd_sum


number=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum,odd_sum=num_li(number)
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
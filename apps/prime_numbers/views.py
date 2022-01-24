from ast import arg
from django.shortcuts import render
from django.http import HttpResponse

from apps import prime_numbers


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    return True


 
def get_prime_numbers(request):
    
    number = int(request.GET.get('number'))
    list_numbers = list(range(2, number + 1))
    two_and_odd_numbers = [i for i in list_numbers if i % 2 != 0 or i == 2]
    prime_numbers = list()
    
    for i in two_and_odd_numbers:
        if (is_prime(i)):
            prime_numbers.append(f', {i}')
            
    
            
    return HttpResponse(prime_numbers)
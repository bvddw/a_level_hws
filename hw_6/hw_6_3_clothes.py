def correct_size(size, country):
    return underwear[size][country]

underwear = {
    'XXS': {'Ukraine': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'Great Britain': 24},
    'XS': {'Ukraine': 44, 'Germany': 38, 'USA': 10, 'France': 40, 'Great Britain': 26},
    'S': {'Ukraine': 46, 'Germany': 40, 'USA': 12, 'France': 42, 'Great Britain': 28},
    'M': {'Ukraine': 48, 'Germany': 42, 'USA': 14, 'France': 44, 'Great Britain': 30},
    'L': {'Ukraine': 50, 'Germany': 44, 'USA': 16, 'France': 46, 'Great Britain': 32},
    'XL': {'Ukraine': 52, 'Germany': 46, 'USA': 18, 'France': 48, 'Great Britain': 34},
    'XXL': {'Ukraine': 54, 'Germany': 48, 'USA': 20, 'France': 50, 'Great Britain': 36},
    'XXXL': {'Ukraine': 56, 'Germany': 50, 'USA': 22, 'France': 52, 'Great Britain': 38},
}
size = input('Choose your size: (XXS, XS, S, M, L, XL, XXL, XXXl): ')
country = input('Enter country: (Ukraine, Germany, USA, France, Great Britain): ')
print(f'Correct size for your country: {correct_size(size, country)}.')
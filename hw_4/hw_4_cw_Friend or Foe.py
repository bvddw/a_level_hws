# https://www.codewars.com/kata/55b42574ff091733d900002f

# Friend or Foe?

def friend(x):
    return [name for name in x if len(name) == 4]  # виводимо тільки ті імена, в яких рівно 4 букви
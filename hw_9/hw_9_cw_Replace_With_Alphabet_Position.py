# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    return ' '.join([str(ord(i.lower()) - 96) for i in ''.join(text.split()) if i.isalpha()])

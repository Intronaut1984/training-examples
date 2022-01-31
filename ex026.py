phrase=str(input('Write a phrase')).lower().strip()

count=(phrase.count('a'))
count2=(phrase.find('a')+1)
count3=(phrase.rfind('a')+1)

print('Your Phrase has {} "a" words. The first letter is the caracter {} and the last "a" letter is the caracter {}'.format(count, count2, count3))
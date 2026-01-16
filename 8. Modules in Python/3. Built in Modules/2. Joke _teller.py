import pyjokes

res = input('Would you like to listen joke(y/n) : ')

if res == 'y':
 lang_input = input('Which language (en, cs, de, etc): ')
 joke_type = input('Which type (all, chuck, neutral): ')
 joke = pyjokes.get_joke(lang_input, joke_type)
 print(joke)
else:
 print('No problem!') 
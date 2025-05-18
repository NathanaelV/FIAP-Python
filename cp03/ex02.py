def vowel_counter(text):
    vowels_count = 0

    for ch in text:
        if ch.lower() in 'aeiou':
            vowels_count += 1


text = input('Digite a frase: ')

vowels_count = vowel_counter(text)

print(f'A frase tem {vowels_count} vogais')

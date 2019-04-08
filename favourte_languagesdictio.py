favourite_languages {
    'william':'python',
    'wendy':'javascript',
    'jimmy':'java',
}
friends = ['william','wendy']
for name in favourite_languages.key():
    print(name.title())

    if name in friends:
        print(" Hi"+ name.title() + ", I see your favourite language is " + favourite_languages[name].title() + "!")

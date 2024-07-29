countries = ['ISRAEL', 'Singapore', 'engLand', 'Brazil']

def starts_with(name_of_country):
    return name_of_country[0] in ["I","S"] or name_of_country[-1] in ["d","m"]

print([word.capitalize() for word in list(filter(starts_with, countries))])
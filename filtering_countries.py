countries = ['ISRAEL', 'Singapore', 'engLand', 'Brazil']

def filtered_world_map(countries):
    # Filter countries that start with "I" or "S" or end with "d" or "m"
    filtered_countries = filter(lambda country: country[0] in ["I", "S"] or country[-1] in ["d", "m"], countries)
    
    capitalized_countries = map(str.capitalize, filtered_countries)
    
    return list(capitalized_countries)

result = filtered_world_map(countries)
print(result)


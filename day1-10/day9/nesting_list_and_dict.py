#Basically here we will create a nested list in a dictionary.
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

cars_list = {
    "mercedes": ["c-class", "e-class", "s-class"],
    "bmw": ["3-series", "5-series", "7-series"],
    "audi": ["a3", "a4", "a5"]
}


  

# Nesting Dictionary in a Dictionary
travels = {
    "France": {
        "cities_visited": ["Lille", "Paris", "Nantes"],
        "total_visits": 12
    },
    "Nigeria": {
        "cities_visited": ["Lagos", "Abuja", "Kano"],
        "total_visits": 12
    }
}



# Nesting Dictionaries in Lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    }
]
print(travel_log[0]["cities_visited"][0])
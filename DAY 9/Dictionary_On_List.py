travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, visits_count, cities_visited):
    country = {}
    country["country"] = country_visited
    country["visits"] = visits_count
    country["cities"] = cities_visited
    travel_log.append(country)


add_new_country("Russia", 2, ["Moscow", "Cyka Blyat"])
print(travel_log)

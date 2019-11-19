cars = {
    "car1": {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2009
    },
    "car2": {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1969
    },
    "car3": {
        "brand": "BMW",
        "model": "i8",
        "year": 2014
    }
}
for i in cars.values():
    if i["year"] == 2009:
        print(i["brand"] + ' ' + i["model"])
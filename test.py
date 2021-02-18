import requests


def map_pos(toponym_to_find):
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get("http://geocode-maps.yandex.ru/1.x/", params=geocoder_params)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    top_pos1 = float(toponym['boundedBy']['Envelope']['upperCorner'].split()[0]) - \
               float(toponym['boundedBy']['Envelope']['lowerCorner'].split()[0])
    top_pos2 = float(toponym['boundedBy']['Envelope']['upperCorner'].split()[1]) - \
               float(toponym['boundedBy']['Envelope']['lowerCorner'].split()[1])
    return top_pos1, top_pos2
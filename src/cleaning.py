import re

def moneyRaise(value):
    dicc_coin = {'CAD': 0.71, 'RUB': 0.013, '€': 1.09, '£': 1.25}
    values_money = {'K': 1000, 'M': 1000000, 'B': 100000000000}
    value_number = float(re.search('[+-]?([0-9]*[.])?[0-9]+', value)[0])
    if value.endswith('B'):
        exchange = value_number*(values_money['B'])
    elif value.endswith('K[k]'):
        exchange = value_number*(values_money['K'])
    elif value.endswith('M'):
        exchange = value_number*(values_money['M'])
    elif value.startswith("C"):
        exchange = value_number*(dicc_coin['CAD'])
    elif value.startswith("$"):
        exchange = value_number
    elif value.startswith("€"):
        exchange = value_number*(dicc_coin['€'])
    elif value.startswith("£"):
        exchange = value_number*(dicc_coin['£'])
    elif value.startswith("r"):
        exchange = value_number*(dicc_coin['RUB'])
    else:
        exchange = value_number
    return int(exchange)

def officeToGeoPoint(row):
    office = row.offices
    if type(office) == dict:
        if 'latitude' in office and 'longitude' in office:
            if(type(office["latitude"])) == float and type(office["longitude"]) == float:
                return ({
                    "type":"Point",
                    "coordinates":[office["longitude"],office["latitude"]]
                },"success")
            else:
                return(None,"Invalid lat and long")
        else:
            return (None,"No lat and long keys in office dict")
    return (None,"No office")

def getLoc(long, lat):
    loc = {
        'type': 'Point',
        'coordinates': [long, lat]
    }
    return loc

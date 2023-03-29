import pymongo

# Verbindung zur MongoDB-Instanz herstellen
client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")

# Datenbank "Music" auswählen
db = client['Music']

# Kollektion "Interpret" erstellen und Daten einfügen
interpret = db['Interpret']
interpret_data = {
    'name': 'Eisbrecher',
    'genre': 'NDH',
    'origin': 'München'
}
interpret.insert_one(interpret_data)
# Kollektion "Musikstück" erstellen und Daten einfügen
musikstueck = db['Musikstück']
musikstuecke_data = [
    {
        'title': 'Die Hölle muss warten',
        'year': '2012',
        'album': 'Die Hölle muss warten',
        'interpret': interpret_data['_id']
    },
    {
        'title': 'Verrückt',
        'year': '2012',
        'album': 'Die Hölle muss warten',
        'interpret': interpret_data['_id']
    },
    {
        'title': 'In einem Boot',
        'year': '2017',
        'album': 'Sturmfahrt',
        'interpret': interpret_data['_id']
    },
    {
        'title': 'Skandal im Sperrbezirk',
        'year': '2020',
        'album': 'Schicksalsmelodien',
        'interpret': interpret_data['_id']
    },
    {
        'title': 'Süßwasserfisch',
        'year': '2018',
        'album': 'Ewiges Eis - 15 Jahre Eisbrecher',
        'interpret': interpret_data['_id']
    },
    {
        'title': 'Stossgebet',
        'year': '2020',
        'album': 'Schicksalsmelodien',
        'interpret': interpret_data['_id']
    }
]
musikstueck.insert_many(musikstuecke_data)

# Verknüpfung der Kollektionen
musikstueck.create_index([('interpret', 1)])

print('Daten erfolgreich in MongoDB eingefügt.')
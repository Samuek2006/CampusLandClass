import util.corefiles as corefiles

DB_BooksKnowledgeLand = 'data/BooksKnowledgeLand.json'

corefiles.initialize_json(DB_BooksKnowledgeLand, {
    'BooksLibrary': {}
})

def addBooks():
    nameBook = input('Ingresa el Nombre del Libro: ')
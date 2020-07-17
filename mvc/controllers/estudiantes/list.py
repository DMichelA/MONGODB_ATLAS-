import web

render = web.template.render("mvc/views/estudiantes/", base="template")

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:DzxlMsAPoHSILCGd@cluster0.nmnzs.mongodb.net/<dbname>?retryWrites=true&w=majority")

database = client.get_database('utec')

collection = database.estudiantes

class List():

    def GET(self):
        try:
            query = list(collection.find())
            lenght = collection.count_documents({})
            print(query)
            print(lenght)
            return render.list(query, lenght) # renderizando list.html
        except Exception as e:
            return "Error " + str(e.args)
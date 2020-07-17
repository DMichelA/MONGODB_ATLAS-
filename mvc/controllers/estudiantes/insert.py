import web

render = web.template.render("mvc/views/estudiantes/", base="template")

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:DzxlMsAPoHSILCGd@cluster0.nmnzs.mongodb.net/<dbname>?retryWrites=true&w=majority")

database = client.get_database('utec')

collection = database.estudiantes

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando insert.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            data = web.input()
            new_document = {
                'nombre': data.nombre,
                'ape_pat': data.ape_pat,
                'ape_mat': data.ape_mat
            }
            collection.insert_one(new_document)
            return render.insert()
        except Exception as e:
            return "Error " + str(e.args)
import web

render = web.template.render("mvc/views/estudiantes/", base="template")

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:DzxlMsAPoHSILCGd@cluster0.nmnzs.mongodb.net/<dbname>?retryWrites=true&w=majority")

database = client.get_database('utec')

collection = database.estudiantes

class Delete():

    def GET(self):
        try:
            return render.delete() # renderizando delete.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            form = web.input()
            print(form.nombre)
            collection.delete_one({'nombre': form.nombre})
            return render.delete()
        except Exception as e:
            return "Error " + str(e.args)
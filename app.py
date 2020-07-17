import web

urls = (
    '/', 'mvc.controllers.index.Index',
    
    '/estudiantes_insert', 'mvc.controllers.estudiantes.insert.Insert',
    '/estudiantes_list', 'mvc.controllers.estudiantes.list.List',
    '/estudiantes_delete', 'mvc.controllers.estudiantes.delete.Delete',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
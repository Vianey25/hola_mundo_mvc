import web

urls = (
    '/', 'mvc.controllers.public.index.Index' ,
    "/sensores", "mvc.controllers.sensores.Sensores"
    
    
)
app = web.application(urls, globals()) 

if __name__ == "__main__":
    app.run()
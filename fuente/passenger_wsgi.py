def application(environ, start_response):   
    start_response('200 OK', [('Content-Type', 'text/html')])   
    rta='<h2>Seguros Clásicos. Sitio en Construcción.</h2> <a href="nuevo.segurosclasicos.com">Ver sitio.</a>\n<div style="display:none;">'+str(environ)+'</div>'
    yield rta


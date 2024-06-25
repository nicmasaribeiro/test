import threading
from app import create_app, socketio
from gevent import monkey
from eventlet import monkey_patch
import eventlet
import asyncio
import logging
app = create_app()
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
    
#       run_app()
#   server_thread = threading.Thread(target=run_app)
#   server_thread.start()/
#   socket_thread = threading.Thread(socketio.run,args=(app))
#   socket_thread.start()
##   monkey_
#   server_thread.join()
#   socket_thread.join()
    
        
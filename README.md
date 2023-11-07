# Python-Basic-Keylogger
Un keylogger non è altro che un programma che registra i tasti premuti (sia da mouse che tastiera) e li memorizza in un log_file.

Il codice è spiegato completamente dai commenti all'interno del file KeyLogger.py


# FAQ


<h4>Che significa che vengono registrati tutti i livelli di log?</h4>
Quando si imposta il livello di log su DEBUG, come nel codice fornito (level=logging.DEBUG), si registra ogni evento di log, indipendentemente dal livello. Questo significa che verranno registrati messaggi di tutti i livelli di gravità, come DEBUG, INFO, WARNING, ERROR e CRITICAL. Questo offre una registrazione completa di ogni evento nel file di log.

<h4>Perché scriviamo data e messaggio come %(asctime)s e %(message)s?</h4>
 Nel formato '%(asctime)s: %(message)s', %(asctime)s rappresenta il timestamp dell'evento di log (la data e l'ora) e %(message)s rappresenta il messaggio effettivo che viene registrato nel log. Utilizzando questo formato, ogni riga nel file di log conterrà un timestamp seguito dal messaggio associato a quell'evento (nel tuo caso, il tasto premuto).

<h4>A cosa serve scrivere on_press = on_press ?</h4>
In Listener(on_press=on_press), si passa la funzione on_press al parametro on_press dell'oggetto Listener. Questo specifica che quando un tasto viene premuto e l'evento viene catturato, la funzione on_press sarà chiamata per gestire quell'evento. In sostanza, on_press=on_press imposta la funzione da eseguire quando viene rilevato un evento di pressione del tasto. Il primo "on_press" è il nome del parametro utilizzato nel costruttore del Listener, mentre il secondo "on_press" è il nome della funzione definita precedentemente che gestisce l'evento di pressione del tasto.

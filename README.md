# Corso di Pandas

Questo progetto contiene il corso di Pandas, una libreria essenziale per l'analisi e la manipolazione dei dati in Python. Nel corso, esplorerai le funzionalità principali di Pandas, come la gestione di DataFrame e Series, l'importazione e l'esportazione di dati, e le operazioni di pulizia e analisi.

## Prerequisiti

- Python 3.x
- Conoscenze di base di Python

## Installazione

Per installare Pandas, usa il seguente comando:

```
pip install pandas
```

Oppure, se stai usando uv come nel progetto:

```
uv add pandas
```

## Struttura del Corso

Il corso è organizzato utilizzando rami Git (branch), dove ogni ramo rappresenta una parte specifica del corso. Questo permette di esplorare gli argomenti in modo modulare.

- **Ramo principale (`main`)**: Contiene la configurazione di base del progetto (`pyproject.toml`, `README.md`, `.gitignore`, ecc.) e le dipendenze necessarie.
- **Rami tematici**: Ogni ramo corrisponde a un argomento del corso, contenendo il codice specifico (`parteX.py`) e dati di esempio.

### Rami Disponibili
1. **`import`**: Importazione dei dati (es. da CSV, Excel).
2. **`Series`**: Operazioni sulle Series.
3. **`DataFrame`**: Operazioni sui DataFrame.
4. **`Selection`**: Selezione dei dati.
5. **`Filtering`**: Filtraggio dei dati.
6. **`Aggregation-and-dataclinig`**: Aggregazione e pulizia dei dati.

Per esplorare una parte, fai checkout al ramo corrispondente: `git checkout <nome-ramo>`, quindi esegui i file con `uv run parteX.py`.

## Come iniziare

Clona il repository e inizia a esplorare i file!

## Riferimenti

- [Corso di Pandas su YouTube](https://www.youtube.com/watch?v=VXtjG_GzO7Q)
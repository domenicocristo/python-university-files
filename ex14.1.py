"""
Scrivete una funzione di nome sed che richieda come argomenti una stringa modello,
una stringa di sostituzione, e due nomi di file. La funzione deve leggere il primo file 
e scriverne il contenuto nel secondo file (creandolo se necessario).
Se la stringa modello compare da qualche parte nel testo del file, la funzione 
deve sostituirla con la seconda stringa.

Se si verifica un errore in apertura, lettura, scrittura, chiusura del file, il vostro
programma deve gestire l'eccezione, stampare un messaggio di errore e terminare.
"""

def sed(model_str, replace_str, input_file, output_file):
    try:
        fin = open(input_file, 'r')
        fout = open(output_file, 'w')
        for line in fin:
            new_line = line.replace(model_str, replace_str)
            fout.write(new_line)
        fin.close()
        fout.close()
    except IOError as e:
        print("Error: {}".format(e))

def main():
    model_str = 'Sed'
    replace_str = 'Python'
    input_file = 'input.txt'
    output_file = 'output.txt'
    sed(model_str, replace_str, input_file, output_file)

main()
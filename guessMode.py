import sys
import random
from constants import DICTIONARY
from utils import clear_terminal, get_exit, strip_accents
from terminalPrints import print_title, print_colored_text

def guess_mode():
    remaining_words = DICTIONARY.copy()
    total_dictionary_lenght = len(DICTIONARY);
    status_vector = []
    wrong_words = []
    for i in range(total_dictionary_lenght):
        status_vector.append("clear")
    status_index = 0

    while True:
        clear_terminal();
        print_title ("MODO ADIVINANZA")

        print_progress(status_vector, status_index, total_dictionary_lenght);

        if (len(remaining_words) == 0):
            print("Ya se han mostrado todas las palabras");
            break;

        word = remaining_words.pop(random.randrange(len(remaining_words)));
        print("DEFINICION:  ", word["definition"]);
        print("CONCEPTO:     ");
        word_concept = strip_accents(word['concept']).lower();

        while True:
            wordSchema = get_schema(word["concept"]);
            guessedWord = strip_accents(input(wordSchema).lower());
            if (len(guessedWord) == len(word_concept)):
                break;
            # Go one line up and remove the line
            sys.stdout.write("\033[F");
            sys.stdout.write("\033[K");
            sys.stdout.flush()

        if (guessedWord == word_concept):
            print_colored_text("¡Correcto!", "green")
            status_vector[status_index] = "correct";
        else:
            print_colored_text("Incorrecto", "red", "");
            print (" - La palabra era: ", word["concept"])
            status_vector[status_index] = "incorrect";
            wrong_words.append(word);

        status_index += 1;

        if get_exit():
            break;

    show_wrong_words(wrong_words);


def show_wrong_words (wrong_words):
    print("\nPalabras falladas:")
    for word in wrong_words:
        print("\nCONCEPTO: ", word["concept"]);
        print("DEFINICIÓN: ", word["definition"]);

    get_exit();

def print_progress(status_vector, status_index, total_lenght):
    print("Progreso: ", end="");
    for status in status_vector:
        if status == "clear":
            print("■", end="");
        elif status == "correct":
            print_colored_text("■", "green", end="")
        elif status == "incorrect":
            print_colored_text("■", "red", end="")
    print(f" {status_index}/{total_lenght}\n");

def get_schema(word):
    schema = "";
    for letter in word:
        if letter in ["/", "-", "_", " ", "(", ")"]:
            schema += letter;
        else:
            schema += "#";
    schema+= "\r"
    return schema;




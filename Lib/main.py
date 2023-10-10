from colorama import Fore, Style

def neotext(text1, text2, text3):
    formatted_text1 = f"{Fore.LIGHTBLACK_EX}\"{text1}"
    formatted_text2 = f"{text2}\"{Style.RESET_ALL}"
    formatted_text3 = f"{Fore.YELLOW}{text3}{Style.RESET_ALL}"

    formatted_text = f"{formatted_text1}\n{formatted_text2}\n{formatted_text3}"
    return formatted_text

text1 = "Don't let the noise of others' opinions"
text2 = "drown out your own inner voice."
text3 = "Steve Jobs"

formatted_text = neotext(text1, text2, text3)
print(formatted_text)
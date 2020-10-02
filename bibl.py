from collections import Counter

class Library:

    def alphabet_len(self, alphabet):
        alph_count = []
        over_symb = []
        for i in range(26):
            alph_count.append(0)
        i = 0
        for symb in alphabet:
            for j in alphabet:
                if(symb == j): # ищем одинаковые символы в алфавите
                    alph_count[i] += 1
            if(alph_count[i] > 1):
                over_symb.append(symb) # записываем их в группу "черезменых"
                alphabet = alphabet.replace(symb, '', alph_count[i] - 1) # удаляем лишние похожие символы
            i += 1
        print('Алфавит перегружен символами:', over_symb)
        print('Удаляем лишние символы из алфавита')
        return alphabet

    def palindrom(self, alphabet, length):
        if (len(alphabet) * 2 < length): # длина палиндрома не больше удвоенной длины алфавита
            return 0
        else:
            palindrom_base = alphabet[:length // 2] # база палиндрома
            new_palindrom = palindrom_base
            if(length % 2 != 0): # если длина палиндрома нечетная, то одна буква не должна повторяться
                new_palindrom += alphabet[length // 2 : (length // 2) + 1]
            new_palindrom += palindrom_base[::-1] # реверсируем базу палиндрома и складываем с начальной частью
        print(new_palindrom)
        return new_palindrom

    def common_symb(self, text):
        ct = Counter(text)
        most_commons = ct.most_common(1) # находим самую частую букву
        most_frequent = most_commons[0]
        return most_frequent

    def common_word(self, text):
        text = text.split()  # делим по пробелам
        ct = Counter(text)
        max_encounters = max(ct.values())  # нахождение максимума
        most_common_word = min(word for word, count in ct.items() if count == max_encounters)  # нахождение минимального из максимально частых слов
        return(most_common_word)  # получаем слово "in"


    def text_fun(self, text):
        common_word = self.common_word(text.lower())
        common_symb = self.common_symb(text.lower().replace(' ', ''))
        text_fun = [common_word, common_symb[0], common_symb[1]]
        return text_fun

if __name__ == '__main__':
    lib = Library()
    alphabet = lib.alphabet_len('abcdef')
    palindrom = lib.palindrom(alphabet, 7)
    text = """Meet my family. There are five of us – my parents, my elder brother, my baby sister and me. 
    First, meet my mum and dad, Jane and Michael. My mum enjoys reading and my dad enjoys playing chess with my 
    brother Ken. My mum is slim and rather tall. She has long red hair and big brown eyes. She has a very pleasant 
    smile and a soft voice. My mother is very kind and understanding. We are real friends. She is a housewife. 
    As she has three children, she is always busy around the house. She takes care of my baby sister Meg, who is
     only three months old. My sister is very small and funny. She sleeps, eats and sometimes cries. We 
     all help our mother and let her have a rest in the evening. Then she usually reads a book or just watches TV. 
     My father is a doctor. He is tall and handsome. He has short dark hair and gray eyes. He is a very hardworking 
     man. He is rather strict with us, but always fair. My elder brother Ken is thirteen, and he is very clever. 
     He is good at Maths and always helps me with it, because I can hardly understand all these sums and problems. 
     Ken has red hair and brown eyes. My name is Jessica. I am eleven. I have long dark hair and brown eyes. 
     I am not as clever as my brother, though I try to do my best at school too. I am fond of dancing. 
     Our dancing studio won The Best Dancing Studio 2015 competition last month. I am very proud of it. 
     I also like to help my mother with my little sister very much. Our family is very united. 
     We love each other and always try to spend more time together."""
    print(lib.text_fun(text))


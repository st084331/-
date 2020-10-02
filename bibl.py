class Library:

    def alphabet_len(self, alphabet):
        alph_count = []
        over_symb = []
        for i in range(26):
            alph_count.append(0)
        i = 0
        for symb in alphabet:
            for j in alphabet:
                if(symb == j):
                    alph_count[i] += 1
            if(alph_count[i] > 1):
                over_symb.append(symb)
                alphabet = alphabet.replace(symb, '', alph_count[i] - 1)
            i += 1
        print('Алфавит перегружен символами:', over_symb)
        print('Удаляем лишние символы из алфавита')
        return alphabet

    def palindrom(self, alphabet, length):
        if (len(alphabet) * 2 < length):
            return 0
        else:
            palindrom_base = alphabet[:length // 2]
            new_palindrom = palindrom_base
            if(length % 2 != 0):
                new_palindrom += alphabet[length // 2 : (length // 2) + 1]
            new_palindrom += palindrom_base[::-1]
        print(new_palindrom)
        return new_palindrom


if __name__ == '__main__':
    lib = Library()
    alphabet = lib.alphabet_len('abcdef')
    palindrom = lib.palindrom(alphabet, 7)


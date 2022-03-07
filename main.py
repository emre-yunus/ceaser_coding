# Het script zal een text encoden of decoden volgens de ceaser cipher. Hiervoor geeft men een offset waarde.
# Spaties worden "[", alle letters worden uiteindelijk hoofdletters en alle andere tekens blijven hetzelfde.

text1 = "aa ..456"
offset = "T"

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]


def process(text_to_process, process_type="encode"):
    result = ""
    for i in text_to_process:
        if i.capitalize() in alphabet:
            for j in alphabet:
                if i.capitalize() == j:
                    index_of_i = alphabet.index(j) + 1

                    # ENCODE: normale text --> ciphertext
                    # DECODE: ciphertext --> normale text
                    if process_type == "decode":
                        index_of_encoded_i = index_of_i - (alphabet.index(offset.capitalize()) + 1)
                        if index_of_encoded_i < 1:
                            index_of_encoded_i += 26

                    # process_type moet hier niet perse "encode zijn". Zolang dat process_type niet "decode" is zal het
                    # encoden.
                    else:
                        index_of_encoded_i = index_of_i + alphabet.index(offset.capitalize()) + 1
                        if index_of_encoded_i > 26:
                            index_of_encoded_i -= 26

                    encoded_letter = alphabet.__getitem__(index_of_encoded_i - 1)
                    result += encoded_letter
        elif i == " ":
            result += "["
        else:
            result += i

    print(result)


process(text1)

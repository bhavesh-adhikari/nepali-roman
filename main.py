consonants ={ 
    'क' : 'ka',
    'ख' : 'kha',
    'ग' : 'ga',
    'घ' : 'gha',
    'ङ' : 'n',
    'च' : 'cha', 
    'छ' : 'chha',
    'ज' : 'ja',
    'झ' : 'jha',
    'ञ' : 'n',
    'ट' : 'ta',
    'ठ' : 'tha',
    'ड' : 'da',
    'ढ' : 'dha',
    'ण' : 'na',
    'त' : 'ta',
    'थ' : 'tha',
    'द' : 'da',
    'ध' : 'dha',
    'न' : 'na',
    'प' : 'pa',
    'फ' : 'ha',
    'ब' : 'ba',
    'भ' : 'bha',
    'म' : 'ma',
    'य' : 'ya',
    'र' : 'ra',
    'ल' : 'la',
    'व' : 'wa',
    'श' : 'sha',
    'ष' : 'sha',
    'स' : 'sa',  
    'ह' : 'ha',
    'क्ष' : 'ksh',
    'त्र' : 'tra',
    'ज्ञ' : 'gya',
    'श्र' : 'sra'
}

vowels = {
    'अ' : 'a',
    'आ' : 'aa',
    'इ' : 'i',
    'ई' : 'i',
    'उ' : 'u',
    'ऊ' : 'u',
    'ए' : 'e',
    'ऐ' : 'ai',
    'ओ' : 'o',
    'औ' : 'au',
    'ऋ' : 'ri',
    'ं': 'm'   
    }

barakhari = {
    'ा' : 'a',
    'ि' : 'i',
    'ी' : 'i',
    'ु' : 'u',
    'ू' : 'u',
    'े' : 'e',
    'ै' : 'ai',
    'ो' : 'o',
    'ौ' : 'au'
}

halves = { 
    'क्' : 'k',
    'ख्' : 'kh',
    'ग्' : 'g',
    'घ्' : 'gh',
    'ङ्' : 'n',
    'च्' : 'ch',
    'छ्' : 'chh',
    'ज्' : 'j',
    'झ्' : 'jh',
    'ञ्' : 'n',
    'ट्' : 't',
    'ठ्' : 'th',
    'ड्' : 'd',
    'ढ्' : 'dh',
    'ण्' : 'n',
    'त्' : 't',
    'थ्' : 'th',
    'द्' : 'd',
    'ध्' : 'dh',
    'न्' : 'n',
    'प्' : 'p',
    'फ्' : 'f',
    'ब्' : 'b',
    'भ्' : 'bh',
    'म्' : 'm',
    'य्' : 'y',
    'र्' : 'r',
    'ल्' : 'l',
    'व्' : 'w',
    'श्' : 'sh',
    'ष्' : 'sh',
    'स्' : 's',
    'ह्' : 'h',
}

while True:
    string = input("Nepali: ")
    output = []
    previous_letter = ""
    for character in string:
        if character == "्":
            previous_letter += character
            output[-1] = previous_letter
        else:
            previous_letter = character
            output.append(previous_letter)
    
    for i in range(len(output)):
        if output[i] in consonants:
            output[i]= consonants[output[i]]
        if  ( i+1 < len(output) and output[i].upper() != output[i].lower()):
            if output[i+1] in barakhari:
                output[i] = output[i][:-1]
        if output[i] in barakhari:
            output[i]= barakhari[output[i]]
        if output[i] in vowels:
            output[i]= vowels[output[i]]
        if output[i] in halves:
            output[i]= halves[output[i]]
    
    # print(output)        
    transliterated = "".join(output)
    print("Roman: ", transliterated)
    

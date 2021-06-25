def find_most_freq_char(word):
    maxIs=0
    maxHarf=""
    for harf in word:
        if maxIs<word.count(harf):
            maxHarf=harf
            maxIs=word.count(harf)
    return maxHarf
    
def encrypt_message(message):
    wordList=message.split()
    parol=""
    for word in wordList:
        mod=find_most_freq_char(word)
        newWord=word.replace(mod,"")
        parol=parol+newWord
        if word is not wordList[-1]:
            parol=parol+"#"
        
    return parol
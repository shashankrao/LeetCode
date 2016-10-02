def validWordAbbreviation(word, abbr):
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """
    wordPtr = 0
    abbrPtr = 0
    while abbrPtr < len(abbr) and wordPtr < len(word):
        if abbr[abbrPtr].isalpha() or abbr[abbrPtr] == "0":
            if abbr[abbrPtr] == word[wordPtr]:
                wordPtr = wordPtr + 1
                abbrPtr = abbrPtr + 1
                continue
            return False
        extractedNo = ""
        while abbrPtr < len(abbr) and (abbr[abbrPtr].isalpha() == False):
            extractedNo += abbr[abbrPtr]
            abbrPtr = abbrPtr + 1
        if len(extractedNo) >0:
            wordPtr+=int(extractedNo)
    if wordPtr == len(word) and abbrPtr == len(abbr):
        return True
    return False


print validWordAbbreviation("internationalization","i5a11o1")
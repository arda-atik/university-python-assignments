def speech_to_words(speech):
    """
    Convert a speech into a list of words.
    Removes punctuation, converts to lowercase, and keeps original order.
    """
    cleaned = ""
    for ch in speech:
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            cleaned += ch.lower()
        elif ch.isspace():
            cleaned += " "
        else:
            continue

    words = cleaned.split()
    return words


def parrot_vocabularies(speeches):
    """
    Find parrots' vocabularies. 
    Returns a sorted list of tuples (name, vocabulary_set).
    """
    result = []
    for name, speech in speeches.items():
        words = speech_to_words(speech)
        vocab = set(words)
        result.append((name, vocab))

    # Sort alphabetically by name first, then descending by vocabulary size
    result.sort(key=lambda item: item[0])
    result.sort(key=lambda item: len(item[1]), reverse=True)

    return result


def who_knows_word(speeches, word):
    """
    Find parrots that used the given `word` at least once.
    Returns a sorted list of tuples (name, count).
    """
    target = word.lower()
    result = []

    for name, speech in speeches.items():
        words = speech_to_words(speech)
        
        count = 0
        for w in words:
            if w == target:
                count += 1
        if count > 0:
            result.append((name, count))

    # Sort alphabetically by name first, then descending by count
    result.sort(key=lambda item: item[0])
    result.sort(key=lambda item: item[1], reverse=True)

    return result


def pairs_with_shared_vocabulary(speeches, min_shared):
    """
    Find all pairs of parrots that share at least `min_shared` words.
    Returns a dictionary mapping (name1, name2) to their shared words set.
    """
    vocabularies = {}
    for name, speech in speeches.items():
        words = speech_to_words(speech)
        vocabularies[name] = set(words)

    names = sorted(vocabularies.keys())
    result = {}

    # Iterate through pairs without duplicating or comparing a parrot to itself
    for k in range(len(names)):
        for j in range(k + 1, len(names)):
            name1 = names[k]
            name2 = names[j]

            shared = set()
            for w in vocabularies[name1]:
                if w in vocabularies[name2]:
                    shared.add(w)
            
            if len(shared) >= min_shared:
                result[(name1, name2)] = shared

    return result

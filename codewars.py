
# maximum subarray sum problem
s = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSequence(A):
    max_global = A[0]
    max_current = A[0]

    for i in range(len(A)-1):
        max_current = max(max_current+A[i],A[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


def top_3_words(text):
    split_words = text.lower().split(" ")
    for word in split_words: word.replace("//", "")
    split_words = filter(None, split_words)
    word_counts = {}
    # create a count index
    for word in split_words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    word_tuples = [(word, word_counts[word]) for word in word_counts.keys()]

    return [x[0] for x in list(sorted(word_tuples, key=lambda x: x[1], reverse=True)[:3])]

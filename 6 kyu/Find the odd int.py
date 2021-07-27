def find_it(seq):
    seq_size = len(seq)
    for i in range (0, seq_size):
        count = 0
        for j in range (0, seq_size):
            if seq[i] == seq[j]:
                count += 1
        if count % 2 != 0:
            return seq[i]
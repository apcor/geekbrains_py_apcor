def proteins(strand):
    if strand and all(i in ['A', 'C', 'G','U'] for i in strand):
        strand_parsed = [strand[i:i+3] for i in range(0, len(strand), 3)]
        result = []
        for chunk in strand_parsed:
            if chunk == 'AUG':
                result.append('Methionine')
            elif chunk in ['UUU', 'UUC']:
                result.append('Phenylalanine')
            elif chunk in ['UUA', 'UUG']:
                result.append('Leucine')
            elif chunk in ['UCU', 'UCC', 'UCA', 'UCG']:
                result.append('Serine')
            elif chunk in ['UAU', 'UAC']:
                result.append('Tyrosine')
            elif chunk in ['UGU', 'UGC']:
                result.append('Cysteine')
            if chunk == 'UGG':
                result.append('Tryptophan')
            elif chunk in ['UAA', 'UAG', 'UGA']:
                break
        return result
    else:
        raise Exception('Please enter a valid RNA sequence')


print(proteins('AUGUUUKUCU'))
def has_english(filename, threshold=9):
    file = open(filename, "r")
    vocab = set(['the', 'The', 'and', 'you', 'there', 'have', 'that', 'from'])
    found = 0
    for line in file:
        for word in line.split():
            if word in vocab:
                found += 1
    file.close()
    if found >= threshold:
        return True
    return False

def decrypt(cipher, key, outname=None):
    f = open(cipher, "r")
    outfile = None
    if not outname:
        outfile = open(f.name + ".decrypted", "w")
    else:
        outfile = open(outname, "w")
    i = 0
    for line in f:
        codes = line.split(",")
        for code in codes:
            dcrptd_byte = int(code)^ord(key[i])
            outfile.write(chr(dcrptd_byte))
            i += 1
            if i == len(key):
                i = 0
    outfile.close()
    f.close()

def main():
    cipher = INPUT_DIR + "cipher1.txt"
    outname = "decrypted.out"
    all_letters = ""
    done = False
    key_len = 3

    for c in xrange(97, 97 + 26):
        for _ in xrange(0, key_len): # include keys with repeating characters, e.g. 'aaa'
            all_letters += chr(c)
    for combo in e_util.get_combos(all_letters, key_len):
        for key in e_util.get_perms(combo):
            decrypt(cipher, key, outname)
            if has_english(outname):
                print key
                return
                
    print "FAILED"

class _RepeatValsResult:
    """ 
    Container for find_repeat_vals result 
    """
    def __init__(self):
        self.is_four_kind = self.is_three_kind = self.is_two_pair = self.is_pair = False
        # value of a {3,4}-of-a-kind, pair vals
        self.val = self.pair1_val = self.pair2_val = None
        self.remainder = []
   
if __name__ == '__main__':
    main()

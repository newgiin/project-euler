def find_repeat_vals(hand):
    """ Determines if a hand contains pairs, or a {3,4}-of-a-kind """ 
    vals = {} # Map: val -> # of cards with value of 'val' in hand
    result = _RepeatValsResult()

    for card in hand:
        if card.val in vals:
            vals[card.val] += 1
        else:
            vals[card.val] = 1

    for val in vals:
        if vals[val] == 4:
            result.is_four_kind = True
            result.val = val
        elif vals[val] == 3:
            result.is_three_kind = True
            result.val = val
        elif vals[val] == 2:
            if result.pair1_val is None:
                result.is_pair = True
                result.pair1_val = val
            else:
                result.is_two_pair = True
                result.pair2_val = val
        else:
            result.remainder.append(val)
    return result

class _FindStr8Result:
    """ 
    Container for find_str8() result. Also stores high - card since find_str8() sorts the 
    hand allowing easy access to highcard.
    """    
    def __init__(self):
        self.high_card = None
        self.has_str8 = False
            
def find_str8(hand):
    result = _FindStr8Result()
    srted = [card.val for card in hand]
    srted.sort()
    result.high_card = srted[-1]
    for i in xrange(0, len(srted) - 1):
        if srted[i] + 1 !=  srted[i + 1]:
            return result
    result.has_str8 = True
    return result

def has_flush(hand):
    suit = hand[0].suit
    for i in xrange(1, len(hand)):
        if hand[i].suit != suit:
            return False
    return True  

class _Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        
    def __init__(self, s):
        try:
            self.val = int(s[0])
        except ValueError:
            if s[0] == "T":
                self.val = 10
            elif s[0] == "J":
                self.val = 11
            elif s[0] == "Q":
                self.val = 12
            elif s[0] == "K":
                self.val = 13
            else:
                self.val = 14
        self.suit = s[1]
        
    def __repr__(self):
        return self.suit + " - " + str(self.val)
        
class _HandRank:
    HIGH_CARD, PAIR, TWO_PAIR, THREE_KIND, STR8, FLUSH\
    , FULL_HOUSE, FOUR_KIND, STR8_FLUSH = xrange(9)

def print_rank(rank):
    ranks = ["HIGH_CARD", "PAIR", "TWO_PAIR", "THREE_KIND", "STR8", "FLUSH"\
    , "FULL_HOUSE", "FOUR_KIND", "STR8_FLUSH"]
    return ranks[rank]
       
def rank_hand(hand_info):
    rank = _HandRank.HIGH_CARD
    
    rep_result = hand_info.rep_result
    str8_result =  hand_info.str8_result
    is_flush =  hand_info.is_flush   
    
    if rep_result.is_two_pair:
        rank = _HandRank.TWO_PAIR
    elif rep_result.is_pair:
        rank = _HandRank.PAIR
        if rep_result.is_three_kind:
            rank = _HandRank.FULL_HOUSE
    elif rep_result.is_three_kind:
        rank = _HandRank.THREE_KIND
    elif rep_result.is_four_kind:
        rank = _HandRank.FOUR_KIND
    elif str8_result.has_str8:
        rank = _HandRank.STR8
        if is_flush:
            rank = _HandRank.STR8_FLUSH
    elif is_flush:
        rank = _HandRank.FLUSH
        
    return rank    

class _HandInfo:
    """
    Wrapper containing all the information you need about a poker hand.
    """
    def __init__(self, hand):
        self.rep_result = find_repeat_vals(hand)
        self.str8_result = find_str8(hand)
        self.is_flush = has_flush(hand)
        self.rank = rank_hand(self)
            
def is_winning_hand(h1_info, h2_info):
    """ Returns True iff hand 1 is the winning hand """    
    if h1_info.rank != h2_info.rank:
        return h1_info.rank > h2_info.rank
    # resolve tie
    if h1_info.rank == _HandRank.PAIR or h1_info.rank == _HandRank.TWO_PAIR:
        h1_pair_val = max(h1_info.rep_result.pair1_val, h1_info.rep_result.pair2_val)
        h2_pair_val = max(h2_info.rep_result.pair1_val, h2_info.rep_result.pair2_val)
        if h1_pair_val > h2_pair_val:
            return True
        elif h1_pair_val < h2_pair_val:
            return False
        else:
            return max(h1_info.rep_result.remainder) > max(h2_info.rep_result.remainder)
    elif (h1_info.rank == _HandRank.THREE_KIND or h1_info.rank == _HandRank.FOUR_KIND or\
            h1_info.rank == _HandRank.FULL_HOUSE):
        if h1_info.rep_result.val > h2_info.rep_result.val:
            return True
        elif h1_info.rep_result.val < h2_info.rep_result.val:
            return False
    if h1_info.str8_result.high_card == h2_info.str8_result.high_card:
        raise Exception("NO CLEAR WINNER")
        
    return h1_info.str8_result.high_card > h2_info.str8_result.high_card

def main():
    result = 0
    f = open(INPUT_DIR + "poker.txt", "r")
    #f = open(INPUT_DIR + "my.test", "r")
    for line in f:
        cards = line.split()
        p1_hand = []
        p2_hand = []
        # populate hands
        for i in xrange(0, 5):
            p1_hand.append(_Card(cards[i]))
        for i in xrange(5, 10):
            p2_hand.append(_Card(cards[i]))
        
        hand_info_1 = _HandInfo(p1_hand)
        hand_info_2 = _HandInfo(p2_hand)
        # determine winner
        if is_winning_hand(hand_info_1, hand_info_2):
            result += 1
    print result

if __name__ == '__main__':
    main()

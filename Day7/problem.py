import numpy as np

def parseInput(file):
    cards, bids = [], []
    for line in file:
        clean = line.strip()
        cards.append(clean.split(' ')[0])
        bids.append(clean.split(' ')[1])
    for i in range(len(bids)):
        bids[i] = int(bids[i])
    return cards, bids

def getKind(cards, bids, kind):
    cards_kind, bids_kind = [], []
    for c,b in zip(cards, bids):
        values, counts = np.unique([*c], return_counts=True)
        if kind=="five-of-a-kind":
            if 5 in counts:
                cards_kind.append(c)
                bids_kind.append(b)
        elif kind=="four-of-a-kind":
            if 4 in counts:
                cards_kind.append(c)
                bids_kind.append(b)
        elif kind=="full-house":
            if 3 in counts and 2 in counts:
                cards_kind.append(c)
                bids_kind.append(b)
        elif kind=="three-of-a-kind":
            if 3 in counts and 2 not in counts:
                cards_kind.append(c)
                bids_kind.append(b)
        elif kind=="two-pairs":
            if 2 in counts and len(counts)==3:
                cards_kind.append(c)
                bids_kind.append(b)
        elif kind=="one-pair":
            if 2 in counts and len(counts)==4:
                cards_kind.append(c)
                bids_kind.append(b)
        elif kind=="highest-card":
            if len(counts)==5:
                cards_kind.append(c)
                bids_kind.append(b)
    return cards_kind, bids_kind

def getKind2(cards, bids, kind):
    cards_kind, bids_kind = [], []
    for c,b in zip(cards, bids):
        can_add = False
        had_J = False
        values, counts = np.unique([*c], return_counts=True)
        if 'J' in values and len(values)>1:
            had_J = True
            # max counts index not considering J
            max_counts_index = 0
            if values[0]=='J':
                max_counts_index = 1
            for i in range(len(counts)):
                if counts[i]>counts[max_counts_index] and values[i]!='J':
                    max_counts_index = i
            j_index = np.where(values=='J')[0][0]
            counts[max_counts_index] += counts[j_index]
            values = np.delete(values,j_index)
            counts = np.delete(counts,j_index)
        if kind=="five-of-a-kind":
            if 5 in counts:
                can_add = True
        elif kind=="four-of-a-kind":
            if 4 in counts:
                can_add = True
        elif kind=="full-house":
            if 3 in counts and 2 in counts:
                can_add = True
        elif kind=="three-of-a-kind":
            if 3 in counts and 2 not in counts:
                can_add = True
        elif kind=="two-pairs":
            if 2 in counts and len(counts)==3:
                can_add = True
        elif kind=="one-pair":
            if 2 in counts and len(counts)==4:
                can_add = True
        elif kind=="highest-card":
            if len(counts)==5:
                can_add = True
        if had_J and not can_add and kind=="full-house":
            print("Had J but not", kind, "with", c)
        if can_add:
            cards_kind.append(c)
            bids_kind.append(b)
    return cards_kind, bids_kind

def isGreater(card1, card2):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J','Q','K','A']
    for c1,c2 in zip(card1, card2):
        if order.index(c1)>order.index(c2):
            return True
        elif order.index(c1)<order.index(c2):
            return False
    return False

def isGreater2(card1, card2):
    order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T','Q','K','A']
    for c1,c2 in zip(card1, card2):
        if order.index(c1)>order.index(c2):
            return True
        elif order.index(c1)<order.index(c2):
            return False
    return False

def rankCard(card,cards):
    cont = 1
    for c in cards:
        if isGreater2(card,c):
            cont += 1
    return cont
        

def rankCards(cards,bids):
    ranks = []
    final_bids = []
    all_cards_added = []
    for kind in ["highest-card","one-pair","two-pairs","three-of-a-kind","full-house","four-of-a-kind","five-of-a-kind"]:
        cards_kind, bids_kind = getKind2(cards, bids, kind)
        all_cards_added += cards_kind
        if len(cards_kind)==0:
            print("No cards of kind", kind)
        final_bids += bids_kind
        ad = len(ranks)
        for c in cards_kind:
            ranks.append(rankCard(c,cards_kind)+ad)
    # print the cards that were not added
    for c in cards:
        if c not in all_cards_added:
            print("Card", c, "was not added")
    return ranks, final_bids

def getWinnings(cards, bids):
    ranks, new_bids = rankCards(cards, bids)
    print(len(ranks), len(new_bids))
    result = 0
    for r,b in zip(ranks, new_bids):
        result += r*b
    return result


if __name__ == '__main__':
    cards, bids = parseInput(open('input.txt', 'r'))
    print(getWinnings(cards, bids))
    
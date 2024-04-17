import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
  if not S:
    return len(T)
  elif not T:
    return len(S)
  else:
    if S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
    else:
        result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:], T[1:], MED))
    MED[(S, T)] = result
    return result
    # TODO -  implement top-down memoization
    

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
  if (len(S) == 0):
    return ("-" * len(T), T)
  if (len(T) == 0):
    return (S, "-" * len(S))
  if (S[-1] == T[-1]):
    return fast_align_MED(S[:-1], T[:-1])
  else:
    return 1 + min(fast_align_MED(S[:-1], T[:-1]), fast_align_MED(S[:-1], T), fast_align_MED(S, T[:-1]))
  


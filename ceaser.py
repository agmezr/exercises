def Caesar(t, s):
    return ''.join([ ord(l) in range(97,122) and  chr((ord(l) - 97 + s )% 26 + 97)  or l for l in t  ]).upper()
    
p = Caesar("underscore_js",8)
print p
#answer to underscore_js with 8 shift:  CVLMZAKWZM_RA
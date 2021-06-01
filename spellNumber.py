# spellnum() function version 2.0
# Author: Chalermsak Chatdokmaiprai chalermsak.c@ku.th
# Date: June 1, 2021
#

def spellnum(n):
    '''Assuming n is a nonnegative integer
    returns its English spelling
    '''
    assert n >= 0
    nmillion, rem = divmod(n, 1_000_000)
    result = ''
    if nmillion > 0:
        result += spellnum(nmillion) + ' million'
        if rem > 0:
            if rem >= 100:
                result += ' ' + spell_submillion(rem)
            else:
                result += ' and ' + spell_10(rem)
    else: # no millions
        if rem > 0:
            result = spell_submillion(rem)
        else:
            result = 'zero'
    return result

def spell_submillion(n):
    '''Assume nonnegative integer n <= 999_999
    returns its English spelling
    '''
    assert 0 <= n <= 999_999
    nthousand, rem = divmod(n, 1000)
    result = ''
    assert nthousand <= 999
    if nthousand > 0:
        result += spell_100(nthousand) + ' thousand'
        if rem > 0:
            if rem >= 100:
                result += ' ' + spell_100(rem)
            else:
                result += ' and ' + spell_10(rem)
    else:  # no thousands
        if rem > 0:
            result = spell_100(rem)
        else:
            result = 'zero'
    return result

sayDigit = {
    0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
    5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine' 
}
def spell_100(n):
    '''Assume nonnegative integer n <= 999
    returns its English spelling
    '''
    nhundred, rem = divmod(n, 100)
    result = ''
    assert nhundred <= 9
    if nhundred > 0:
        result += sayDigit[nhundred] + ' hundred'
        if rem > 0:
            result += ' and ' + spell_10(rem)
    else: # no hundreds
        if rem > 0:
            result = spell_10(rem)
        else:
            result = 'zero'
    return result

sayTeen = {
    10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
    15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 
    19:'nineteen' 
}
sayTenty = {
    2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 
    6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety' 
}
def spell_10(n):
    '''Assume nonnegative integer n <= 99
    returns its English spelling
    '''
    if n <= 9:
        return sayDigit[n]
    if n <= 19:
        return sayTeen[n]
    nten, rem = divmod(n, 10)
    result = ''
    assert 2 <= nten <= 9
    if nten > 0:
        result += sayTenty[nten]
        if rem > 0:
            result += ' ' + sayDigit[rem]
    else: # no tens
        result = sayDigit[rem]
    return result

def go():
    testnumber = 98706543210587
    print(f'Calling spellnum({testnumber})')
    print(spellnum(testnumber))
    while True:
        n = int(input('?'))
        print(spellnum(n))

if __name__ == '__main__':
    go()


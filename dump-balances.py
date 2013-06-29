#!/usr/bin/env python

""" Dump balances from the ledger """

from __future__ import division

import json
import re
import sys
import urllib2

__author__      = "Hurukan"
__copyright__   = "Copyright 2013, XRP Talk"

###########
# Formats #
###########

### Set a comma in a number ###

def commafy(s):
    r = []
    for i, c in enumerate(reversed(s)):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    return ''.join(r)

### Delete trailing zeros in a number ###

def del_zeros(num):
    if num.find('.') == -1:
        return num
    j=0
    for c in reversed(num):
        if c == '0':
            j = j + 1
        elif c == '.':
            j = j + 1
            break;
        else:
            break
    if j == 0:
        return num
    return num[:-j]

### Format Numbers/Values ###

re_digits_nondigits = re.compile(r'\d+|\D+')

def format_numbers(format, value):
    parts = re_digits_nondigits.findall(format % (value,))
    for i in xrange(len(parts)):
        s = parts[i]
        if s.isdigit():
            parts[i] = commafy(s)
            break
    return del_zeros(''.join(parts))


########
# Main #
########

if __name__ == "__main__":

    # Usage

    if len(sys.argv) != 2:
        print "Usage: python dump-balances.py [url]"
        print "    -> https://s1.ripple.com:51234/"
        print "    -> https://s2.ripple.com:51234/"
        sys.exit(1)

    # JSON Request

    try:
        json_request = json.dumps({ "method" : "ledger", "params" : [ { "ledger_index" : "current", "accounts" : 1, "expand" : 1 } ] })
        request = urllib2.Request(sys.argv[1], json_request, {'Content-Type': 'application/json'})
        response = urllib2.urlopen(request)
        json_response = json.loads(response.read())
    except Exception, e:
        sys.exit("[exception] %s" % e)

    # Dump Balances

    accounts = dict()
    
    if 'result' in json_response:
        if 'ledger' in json_response['result']:
            if 'accountState' in json_response['result']['ledger']:
                for entry in json_response['result']['ledger']['accountState']:
                    if 'LedgerEntryType' in entry:
                        if entry['LedgerEntryType'] == 'AccountRoot':
                            accounts[entry['Account']] = int(entry['Balance'])
    # Print

    i=1
    for address, balance in reversed(sorted(accounts.iteritems(), key=lambda item: item[1])):
        print "%s:%s:%s" % (i, address, format_numbers('%.6f', (balance / 1000000)))
        i += 1


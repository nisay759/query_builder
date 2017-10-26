#!/usr/bin/env python
import sys
import argparse

def build_queries(data, domain, prefix, length):
    if prefix is None: prefix = ""
    if (length is None) or (not length.isdigit()) or (not int(length) in range(0, 253)):
        length = 252
    elif len(domain + prefix) + 2 > int(length):
        print("Length is less than (data + domain + prefix)")
        print("Use a different value or leave empty !")
        sys.exit(-1)
    query = ""
    rem = int(length) - len(domain)
    no_labels = int(rem / 64)
    last_label_len = (rem % 64) - 1
    while data != "":
        data = prefix + data
        for i in range(0, no_labels):
            if data == "" : break
            label = data[:63]
            data = data[63:]
            query += label + '.'
        if data == "":
            query += domain
        else:
            if last_label_len < 1: #If last label isn't large enough for holding data
                query += domain
            else:
                 label = data[:last_label_len]
                 data = data[last_label_len:]
                 query += label + '.' + domain
        print(query)
        query = ""

def main():
    parser = argparse.ArgumentParser(description='DNS query builder')
    parser.add_argument('-d', action="store", dest="data", required=True,
            help="Data to be encoded in the DNS query string")
    parser.add_argument('-D', action="store", dest="domain", required=True,
            help="Domain name for the DNS query")
    parser.add_argument('-p', action="store", dest="prefix",
            help="Prefix to prepend to DNS query strings")
    parser.add_argument('-l', action="store", dest="length",
            help="Maximum length of DNS query strings")
    results = parser.parse_args()
    build_queries(results.data, results.domain, results.prefix, results.length)

if __name__ == '__main__':
    main()

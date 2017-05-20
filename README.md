DNS Query Builder
=======

Query_builder is a tool for tailored DNS query strings generation.
It can be used to generate payloads to test against your DNS server, encode data to exfiltrate into DNS queries, or [insert your use case here].

Query_builder is RFC1034-compliant, and produces by default queries that look like:

```
|-----------------------Payload----------------------|
[63 chars].[63 chars].[63 chars].[x chars].example.com
```

# Usage

```bash
$ ./query_builder.py -h
usage: query_builder.py [-h] -d DATA -D DOMAIN [-p PREFIX] [-l LENGTH]

DNS query builder

optional arguments:
  -h, --help  show this help message and exit
  -d DATA     Data to be encoded in the DNS query string
  -D DOMAIN   Domain name for the DNS query
  -p PREFIX   Prefix to prepend to DNS query strings
  -l LENGTH   Maximum length of DNS query strings
```

# Examples
#### Generate queries of maximum length
```bash
$ ./query_builder.py -d $(python -c 'print "A"*300') -D github.com
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.github.com
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA.github.com
```

#### Generate fixed length queries
~ Except for the last query, which will contain what remains of data
```bash
$ ./query_builder.py -d exfiltration -D github.com -l 15
exfi.github.com
ltra.github.com
tion.github.com
```

#### Prepend a prefix to the queries
~ This may help you later identify the queries that you generated
```bash
$ ./query_builder.py -d payload -D github.com -p 1337 -l 19 
1337payl.github.com
1337oad.github.com
```

# Notes & contribution
I wrote this tool first with the idea of integrating it to [DET](https://github.com/conix-security/DET)'s DNS plugin. I think the tool might have usages besides data exfiltration.

Contributions are welcome. Feel free to submit your ideas by opening a PR/issue. I'll review it as soon as possible.

# License
Query_builder is under an [MIT License](https://opensource.org/licenses/MIT).

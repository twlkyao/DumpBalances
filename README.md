About
=====

A tool to dump all account balances from a ledger.

Howto
=====

        $ python dump-balances.py
        Usage: python dump-balances.py [url]
            -> https://s1.ripple.com:51234/
            -> https://s2.ripple.com:51234/
        
        $ python dump-balances.py https://s1.ripple.com:51234/ > balances.txt
        
        # more balances.txt
        1:rJipRKjL3CNAvWWMNrbXW9sCvk66PBdyMv:7,579,000,000.99995
        2:rPk69WY7GippqPj6xS4Fbm8XHin867jDVd:3,799,999,800.0001
        3:rf5bGRLFfJx1DajRsam8ZC6FG4D3F3vsPk:3,799,999,800
        4:rN1U7KEa5r58mwJd9zDjeo1DspacgfWJWZ:3,799,999,800
        5:rNfBU1f7fzXUcjqPYFc8MRg9RnGxdr14pF:3,550,000,000.0001
        6:rBHJsEvoKrvS2Ye52K88RoMt2sFmgp2FLA:3,550,000,000
        7:r4EKQxzz2XMaSBjWPfH119tj7yA37sweEQ:3,550,000,000
        8:rJUx1FCr9158mWYQ1Vm72HNXjJ9ZaVj73o:3,550,000,000
        9:rfU9THTwZtXYSnKAcUzDMPaqfrn6LyTydU:3,550,000,000
        10:rfSQFNYVT3YWbfAyYHC2osFwXiYTqnFmoU:3,550,000,000
        11:r9UqbHHrwEfMTsCjqz8WCiXqQLfEUGVb7i:3,550,000,000
        12:rEXgXkdfvAGtYoywDxQnemfhWK7i7WD7go:3,550,000,000
        13:rpHNBAVgioi1KDsCAR3NSTakC31pa3hsrV:3,550,000,000
        14:rnXJRRGKBo6bh4hxCYBFgY9HhwdJ73nND9:3,550,000,000
        15:rnbNxpfRRXCnYY7J8jsapexWnLLvot4ZUF:3,550,000,000
        16:rU6RMNxos6mJ5hTEjS8Lm2fcLS1k75w1yM:3,550,000,000
        17:rETp9RCkB5PB731ULeJf14HQkVrWbRbaKp:3,550,000,000
        18:rfc1mvj7x2FdFWPdLQnfiPbhF4XpChiMdV:3,550,000,000
        19:rPR3P66KXby736oSuDhwYfyS5wMVhfuAaJ:3,550,000,000
        20:ra4G8dkb7efnaUrc83x4CRt3Tpd9AvZWwJ:3,550,000,000
        21:rfqqfT3kYVFJv2SNwvcaVauCaMgUJ9ZpUV:2,799,999,800
        22:rhWnKQ79moM7wkk2b9RpufDzhbHw7YLc6d:2,000,000,000
        23:rB6SbJ5gP8WM8io8Q9eXepHv4jijhHURLs:2,000,000,000
        24:rBtVhMKcyiJJqyLTKqJdZSZrLEA5JAXjB1:1,910,000,000
        25:rsjB6kHDBDUw7iB5A1EVDK1WmgmR6yFKpB:1,000,000,000
        26:rUzSNPtxrmeSTpnjsvaTuQvF2SQFPFSvLn:1,000,000,000
        27:rNRG8YAUqgsqoE5HSNPHTYqEGoKzMd7DJr:1,000,000,000
        28:rGRGYWLmSvPuhKm4rQV287PpJUgTB1VeD7:999,999,999.99999
        29:rJE8YtJnAyFSVvjtEhPCFngVC4hWmZfRcn:500,000,000
        30:r476293LUcDqtjiSGJ5Dh44J1xBCDWeX3:500,000,000
        31:rhgovzKYmuVaRB6xnVxGL4mGi6skxA31FN:500,000,000
        32:rhmwTvfuTZ1KYyXFtKLUGyB3L1JXNzPRY4:500,000,000
        33:rwAzZQgYHfrVYsRoUG1g4gpdKssPUEmNDP:500,000,000
        34:rU1bPM4q2rVhC73F7znm7Lt5QnYzZsV35q:500,000,000
        35:r44CNwMWyJf4MEA1eHVMLPTkZ1LSv4Bzrv:500,000,000
        36:rMErERn4aHWmLT9NU2muvEpDg1vpRX11Z:500,000,000
        37:rhREXVHV938ToGkdJQ9NCYEY4x8kSEtjna:500,000,000
        38:rD6tdgGHG7hwGTA6P39aE7W89fbqxXRjzk:500,000,000
        39:rMLnwJF3FGpGT5kuoQWkwSLQX9NQQkAHH4:500,000,000
        40:rH8MH25kFERugNYA5LtCV9tp53zpWngcBV:500,000,000
        41:rPNoY3puAWywNA5CEDxirZ2BDYHG5du8Xf:500,000,000
        42:rPoJNiCk7XSFLR28nH2hAbkYqjtMC3hK2k:500,000,000
        43:rLt5hnUwhTPfCNBmJFLb5jFNiKpUkyKi1h:500,000,000
        44:rDfrrrBJZshSQDvfT2kmL9oUBdish52unH:500,000,000
        45:rUAFP2TArpubjUZfD965AR2xq7GwNi1Uzy:406,665,083.98958
        46:r43mpEMKY1cVUX8k6zKXnRhZMEyPU9aHzR:200,000,000
        47:r9ssnjg97d86PxMrjVsCAX1xE9qg8czZTu:200,000,000
        48:rppWupV826yJUFd2zcpRGSjQHnAHXqe7Ny:200,000,000
        49:rf7phSp1ABzXhBvEwgSA7nRzWv2F7K5VM7:150,000,000
        50:rB59DESmVnTwXd2SCy1G4ReVkP5UM7ZYcN:150,000,000
        [...]

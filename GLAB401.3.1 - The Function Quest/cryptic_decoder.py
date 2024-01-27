# just going to adapt a previous one
def encrypt_message(message, key):

    encrypted_message = ''

    for letter in message:
        if letter in key:
            encrypted_message += key[letter]
        else:
            encrypted_message += letter

    return encrypted_message

def decrypt_message(message, key):
    # swap the keys and values
    # not doing this manually
    key = dict(zip(key.values(), key.keys()))

    # once the key is swapped the function
    # to decrypt is the same as encrypt
    return encrypt_message(message,key)

# Define the encryption key here:
key = {'a':'q','b':'g','c':'d','d':'e','e':'p',
       'f':'r','g':'t','h':'y','i':'k','j':'u',
       'k':'i','l':'o','m':'j','n':'h','o':'l',
       'p':'z','q':'a','r':'f','s':'w','t':'v',
       'u':'m','v':'x','w':'s','x':'b','y':'n',
       'z':'c'}

# beginning of Caesar's Gallic War
text = 'Gallia est omnis divisa in partes tres, quarum unam incolunt Belgae, aliam Aquitani, \
        tertiam qui ipsorum lingua Celtae, nostra Galli appellantur. 2 Hi omnes lingua, \
        institutis, legibus inter se differunt. Gallos ab Aquitanis Garumna flumen, a Belgis \
        Matrona et Sequana dividit. 3 Horum omnium fortissimi sunt Belgae, propterea quod \
        a cultu atque humanitate provinciae longissime absunt, minimeque ad eos mercatores \
        saepe commeant atque ea quae ad effeminandos animos pertinent important, 4 proximique \
        sunt Germanis, qui trans Rhenum incolunt, quibuscum continenter bellum gerunt. \
        Qua de causa Helvetii quoque reliquos Gallos virtute praecedunt, quod fere cotidianis \
        proeliis cum Germanis contendunt, cum aut suis finibus eos prohibent aut ipsi in eorum \
        finibus bellum gerunt. 5 [Eorum una, pars, quam Gallos obtinere dictum est, initium \
        capit a flumine Rhodano, continetur Garumna flumine, Oceano, finibus Belgarum, attingit \
        etiam ab Sequanis et Helvetiis flumen Rhenum, vergit ad septentriones. 6 Belgae ab \
        extremis Galliae finibus oriuntur, pertinent ad inferiorem partem fluminis Rheni,\
        spectant in septentrionem et orientem solem. 7 Aquitania a Garumna flumine ad \
        Pyrenaeos montes et eam partem Oceani quae est ad Hispaniam pertinet; spectat \
        inter occasum solis et septentriones.'

encoded = encrypt_message(text,key)
print(encoded)

decoded =decrypt_message(encoded,key)
print(decoded)


 
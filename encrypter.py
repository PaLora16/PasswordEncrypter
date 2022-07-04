from optparse import OptionParser

from encrypter_helper import LetsEncrypt

# Helper class
letEnc = LetsEncrypt()

parser = OptionParser()

# generate key value
parser.add_option(
    "-g",
    "--generatekey",
    action="store_true",
    dest="generate_key",
    default=False,
    help="generate encryption key",
)
# save key into pickle file
parser.add_option(
    "--savekey",
    "-s",
    action="store_true",
    dest="save_key",
    default=False,
    help="save key into file",
)
# read key from pickle and print
parser.add_option(
    "-r",
    "--readkey",
    action="store_true",
    dest="read_key",
    default=False,
    help="restore key into file",
)

# encrypt and print supplied string
parser.add_option("-e", "--encrypt", dest="to_be_encrypted",
                help="encrypt string")
# decrypt and print supplied string
parser.add_option("-d", "--decrypt", dest="to_be_decrypted",
                help="decrypt string")
# optional key for encrypt/decrypt string
parser.add_option("-k", "--key", dest="key", help="encyption/decryption key")

# parse arguments into oprion dictionary
(options, args) = parser.parse_args()

# get values of line parameters
_generate_key = options.generate_key
_save_key = options.save_key
_read_key = options.read_key
_to_be_encrypted = options.to_be_encrypted
_to_be_decrypted = options.to_be_decrypted
_key = options.key

# The** Business logic **

# if generate file -> only accepted par is -s
if _generate_key:
    letEnc.generate_key()
    if _save_key:
        letEnc.serialize_key()
    exit(0)

# readkey is single allowed parameter too
if _read_key:
    letEnc.read_key()
    exit(0)

# if supplied external key, use it, else use saved key
if _to_be_encrypted:
    if _key:
        letEnc.store_key(_key)
    letEnc.encrypt(_to_be_encrypted)
    exit(0)

# if supplied external key, use it, else use saved key
if _to_be_decrypted:
    if _key:
        letEnc.store_key(_key)
    letEnc.decrypt(_to_be_decrypted)
    exit(0)

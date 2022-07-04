# Sensitive data encrypter/decrypter

## Instalation

----------------------------------------------------------------

1. Save downloaded scripts into any folder
2. Cd to script folder
3. Create and activate venv environment
4. Install dependencies from requirements.txt

`pip install -r requirements.txt`

5. Run script to see all CLI options

`py encrypter.py -h`

## Encrypter options

----------------------------------------------------------------
-g :  generate encryption key

-s :  permanently save key, if omitted generated encryption key is just printed on console

-r :  read and print key saved with -s

-e :  value - value to be encrypted

-d :  value - value to be decrypted

-k :  optional encryption key, can be used in combination with -e -d

#### REMARKS

    if -k is omitted, key is read from a pickle file
    if -g is given, remaining parameters are ignored, except -s
    if -r is given, other parameters are ignored 
    -s without -g is ignored  

#### EXAMPLE

`py encrypter.py -g -s` Generate and save key into file & print key onto console

`py encrypter.py -e my_secret_password` Encrypt _my_secret_password_ using saved key & print

`py encrypter.py -d enrypred_value -k key` Print on console decrypred value using supplied key

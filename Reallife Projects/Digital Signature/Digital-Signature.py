import sys
import os
import base64
import logging

from cryptography.exceptions import InvalidSignature
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# If the signature of the file matches then we print the contents of the file
def File(file_content):
    print("\nHere is your file content\n")
    print("///////////////////////////\n")
    print(file_content)

    """
    Example for cryptographic signing of a string in one method.
    - Generation of public and private RSA 4096 bit keypair
    - SHA-512 with RSA signature of text using PSS and MGF1 padding
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings

    """

# @ Creating a global function generate() to generate the Signature

global generate 
def generate(plain_text):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend())

    '''
    Declaring public_key as global so only we can access this 
    key to verify 

    ''' 
    global public_key
    public_key = private_key.public_key()

    global signature
    signature = private_key.sign(
        data=plain_text.encode('utf-8'),
        padding=padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
        algorithm=hashes.SHA256())

    print("Generating signature")
    print("loading.....")

    # Here we print the generated key
    logger.info("Signature: %s", base64.urlsafe_b64encode(signature))
    print("\nSignature Generated")

def verify(plain_text):
    try:
        print("Verifying the signature")
        print("loading.....")
        
        # Verifying the this file key with the previous file key
        public_key.verify(
            signature=signature,
            data=plain_text.encode('utf-8'),
            padding=padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
            algorithm=hashes.SHA256())
        
        is_signature_correct = True
        File(plain_text)
    except InvalidSignature:
        is_signature_correct = False
    
    if is_signature_correct:
        logger.info("Signature matched: %s", is_signature_correct)
    else:
        logger.info("Signature not matched")

# Performs two operation (generate  &  verify)
def choose(n,plain_text):
    if n == 1:
        generate(plain_text)
    else:
        verify(plain_text)

if __name__ == '__main__':
    loop = 1
    while loop:
        print("\nPaste your file location here")
        file = str(input())
        f = open(r"{}".format(file), "r") 
        print("\n1.Generate Signature")
        print("2.Verify Signature")
        n = int(input("\nEnter your choice: "))
        choose(n,f.read())
        if n == 2:
            loop = 0

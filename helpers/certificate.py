from OpenSSL import crypto
from socket import gethostname

CERT_FILE = "./self_signed.crt"
KEY_FILE = "./private.key"


def create_self_signed_cert():
    """
    Create self signed certificate which will be used by the
    server to establish an ssl connection with the clients
    """

    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 1024)

    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = "GP"
    cert.get_subject().ST = "GRAD_PROJECT"
    cert.get_subject().L = "GRAD_PROJECT"
    cert.get_subject().OU = "GRAD_PROJECT"
    cert.get_subject().CN = gethostname()
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha1')

    cert_file = open(CERT_FILE, "wb")
    cert_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    cert_file.close()

    key_file = open(KEY_FILE, "wb")
    key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    key_file.close()

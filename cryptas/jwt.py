import base64

class Jwt():

    BS64_SUFFIX = ("=","==")
    BS64_TRANS = ('+/', '-_')
    SIGN_ALGO = {
        "RS256":"RSA SHA256",
        "HS256":"HMAC SHA256",
    }

    @staticmethod
    def url_decode(words):
        last = len(Jwt.BS64_SUFFIX) -1
        for i, suffix in enumerate(Jwt.BS64_SUFFIX):
            try :
                base64_str = words.translate(str.maketrans(*Jwt.BS64_TRANS)) + suffix
                return base64.b64decode(base64_str.encode()).decode('utf-8')
            except Exception as e:
                if i >= last:
                    raise e
    def __init__(self, jwt):
        self.jwt = jwt

    def analyze(self):
        try:
            header, payloads, signature = self.jwt.split(".")
            jwt_decoded =  {
                "header": Jwt.url_decode(header),
                "payloads":Jwt.url_decode(payloads),
                # TODO: hmac + sha256 decoding how to do that?
                "signature": '', # put code here.
            }
            header + '.' + payloads
            """
            echo -n "eyJraWQiOiJrZXlzLzNjM2MyZWExYzNmMTEzZjY0OWRjOTM4OWRkNzFiODUxIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkdWJoZTEyMyJ9" | openssl dgst -binary -hmac -rsa "{client_secret}" > hr256_sign.txt
            or
            wher RS256 find rsa public key by metadata url.
            """
            return jwt_decoded
        except Exception as e:
            raise e

# sample code.
jwt="eyJraWQiOiJrZXlzLzNjM2MyZWExYzNmMTEzZjY0OWRjOTM4OWRkNzFiODUxIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkdWJoZTEyMyJ9.XicP4pq_WIF2bAVtPmAlWIvAUad_eeBhDOQe2MXwHrE8a7930LlfQq1lFqBs0wLMhht6Z9BQXBRos9jvQ7eumEUFWFYKRZfu9POTOEE79wxNwTxGdHc5VidvrwiytkRMtGKIyhbv68duFPI68Qnzh0z0M7t5LkEDvNivfOrxdxwb7IQsAuenKzF67Z6UArbZE8odNZAA9IYaWHeh1b4OUG0OPM3saXYSG-Q1R5X_5nlWogHHYwy2kD9v4nk1BaQ5kHJIl8B3Nc77gVIIVvzI9N_klPcX5xsuw9SsUfr9d99kaKyMUSXxeiZVM-7os_dw3ttz2f-TJSNI0DYprHHLFw"
jwt = Jwt(jwt)
ret = jwt.analyze()
print(ret)

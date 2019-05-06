

#!/bin/bash

token='XXXX'
secret='YYYY'

date=`date -u +'%Y-%m-%dT%H:%M:%SZ'`

signature=`echo -n "date: $date" | openssl dgst -sha256 -binary -hmac "$secret" | base64`

curl -H "Authorization: Bearer $token" -H "Date: $date" -H "Signature: keyId=\"$token\",algorithm=\"hmac-sha256\",headers=\"date\",signature=\"$signature\"" 'https://api.guasfcu.com/v1/accounts/FROM_ACCT_ID/transactions/'

#!/bin/bash

token='XXXX'
echo $token

secret='YYYY'
echo $secret

date=`date -u +'%Y-%m-%dT%H:%M:%SZ'`
echo $date

signature=`echo -n "date: $date" | openssl dgst -sha256 -binary -hmac "$secret" | base64`
echo $signature

#curl -H "Authorization: Bearer $token" -H "Date: $date" -H "Signature: keyId=\"$token\",algorithm=\"hmac-sha256\",headers=\"date\",signature=\"$signature\"" 'https://api.guasfcu.com/v1/accounts/'
#> {"id":"authentication_failed","message":"Incorrect authentication credentials."}

#curl -H "Authorization: Bearer $token" -H "Date: $date" -H "Signature: keyId=\"$token\",algorithm=\"hmac-sha256\",headers=\"date\",signature=\"$signature\"" 'https://api.banksite.com/v1/accounts'
#> {"id":"authentication_failed","message":"Incorrect authentication credentials."}curl: (6) Could not resolve host: api.banksite.com

curl -H "Authorization: Bearer $token" -H "Date: $date" -H "Signature: keyId=\"$token\",algorithm=\"hmac-sha256\",headers=\"date\",signature=\"$signature\"" 'https://api.demo.narmitech.com/v1/accounts/'

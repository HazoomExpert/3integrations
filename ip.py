from requests import get

ip = get('https://api.ipify.org').text
print ('My public IP address is 123123123:', ip)

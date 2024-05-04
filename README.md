# captcha-bypass
A tool that automates work using known captcha bypass methods.

## INSTALL

1. git clone
2. pip3 install -r requirements.txt

## Descriptions of Bypass Methods

1. Captcha param None method is success: It can be bypassed by completely deleting the parameter containing the Captcha Token.
2. Captcha param Null method is success: It can be bypassed by leaving the value of the parameter containing the Captcha Token blank.
3. Add Header method is success: bypass by adding X-Forwarded-Host, X-Forwarded-For, X-Originating-IP, X-Remote-IP, X-Remote-Addr, can be done.
4. POST->GET method is potentially success: It can be bypassed by turning the POST method into a GET method. **Manual control may be required!**
5. POST->PUT method is potentially success: It can be bypassed by converting the POST method to the PUT method. **Manual control may be required!**
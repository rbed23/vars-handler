# Show Attributes Handler

Often, when working with new package modules, I want to know the attributes available when using an object I am unfamiliar with. 

The built-in Python modules vars() and dir() will display these attributes; however, in a difficult to read-and-parse manner. 

This module 'prettifies' the output from vars() and dir() call to display an object's attributes in a more human-readable format.

## Examples

The following sections provides example output from the function calls... we will be using the object {r} from the requests library for these examples.

```
>>> from vars_handler import show_attrs, dump_dir, dump_vars
>>> import requests
>>> r = requests.get('https://www.github.com/rbed23')
```

#### show_attrs(object, trunc: int, keys: bool)

Displays the object's locally-scoped attributes, *in addition to* its parent attributes, if any.

- **object:** the object attributes to be shown

- **trunc:** argument of type :int: that truncates the displayed output if over a number of chars (defaults to 50 chars)

- **keys:** argument of type :bool: that displays only the attribute keys (True) or full key-value pairs (False \[default\])

```
>>> show_attrs(r)

Scoped Attributes
------------------
{
    "_next": "None",
    "_content_consumed": "True",
    "_content": "b'\\n<!DOCTYPE html>\\n<html lang=\"en\">\\n  <head>\\n  (<<<---truncated)",
    "connection": "<requests.adapters.HTTPAdapter object at 0x7f37e3e (<<<---truncated)",
    "cookies": "<RequestsCookieJar[<Cookie _octo=GH1.1.1678721293. (<<<---truncated)",
    "elapsed": "0:00:00.934239",
    "encoding": "utf-8",
    "headers": "{'date': 'Thu, 09 Jul 2020 08:30:23 GMT', 'content (<<<---truncated)",
    "history": "[<Response [301]>]",
    "raw": "<urllib3.response.HTTPResponse object at 0x7f37e49 (<<<---truncated)",
    "reason": "OK",
    "request": "<PreparedRequest [GET]>",
    "status_code": "200",
    "url": "https://github.com/rbed23"
}

Attributes Scoped from Parent
------------------------------
[
  "__attrs__",
  "__bool__",
  "__class__",
  "__delattr__",
  "__dict__",
  "__dir__",
  "__doc__",
  "__enter__",
  "__eq__",
  "__exit__",
  "__format__",
  "__ge__",
  "__getattribute__",
  "__getstate__",
  "__gt__",
  "__hash__",
  "__init__",
  "__init_subclass__",
  "__iter__",
  "__le__",
  "__lt__",
  "__module__",
  "__ne__",
  "__new__",
  "__nonzero__",
  "__reduce__",
  "__reduce_ex__",
  "__repr__",
  "__setattr__",
  "__setstate__",
  "__sizeof__",
  "__str__",
  "__subclasshook__",
  "__weakref__",
  "apparent_encoding",
  "close",
  "content",
  "is_permanent_redirect",
  "is_redirect",
  "iter_content",
  "iter_lines",
  "json",
  "links",
  "next",
  "ok",
  "raise_for_status",
  "text"
]
```

#### dump_dir(object)

Displays the object's fully-scoped attributes as a list of named keys. For more information on the dir() function call, [click here](https://www.geeksforgeeks.org/python-dir-function/)

- **object:** the object attributes to be shown

Using the Python built-in dir() call...
```
>>> dir(r)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
```

Versus using this module's dump_dir() call...
```
>>> dump_dir(r)
[
  "__attrs__",
  "__bool__",
  "__class__",
  "__delattr__",
  "__dict__",
  "__dir__",
  "__doc__",
  "__enter__",
  "__eq__",
  "__exit__",
  "__format__",
  "__ge__",
  "__getattribute__",
  "__getstate__",
  "__gt__",
  "__hash__",
  "__init__",
  "__init_subclass__",
  "__iter__",
  "__le__",
  "__lt__",
  "__module__",
  "__ne__",
  "__new__",
  "__nonzero__",
  "__reduce__",
  "__reduce_ex__",
  "__repr__",
  "__setattr__",
  "__setstate__",
  "__sizeof__",
  "__str__",
  "__subclasshook__",
  "__weakref__",
  "_content",
  "_content_consumed",
  "_next",
  "apparent_encoding",
  "close",
  "connection",
  "content",
  "cookies",
  "elapsed",
  "encoding",
  "headers",
  "history",
  "is_permanent_redirect",
  "is_redirect",
  "iter_content",
  "iter_lines",
  "json",
  "links",
  "next",
  "ok",
  "raise_for_status",
  "raw",
  "reason",
  "request",
  "status_code",
  "text",
  "url"
]
```


#### dump_vars(object, trunc: int, keys: bool)

Displays *only* the object's locally-scoped attributes. For more information on the vars() function call, [click here](https://www.geeksforgeeks.org/vars-function-python/)

- **object:** the object attributes to be shown

- **trunc:** argument of type :int: that truncates the displayed output if over a number of chars (defaults to 50 chars)

- **keys:** argument of type :bool: that displays only the attribute keys (True) or full key-value pairs (False \[default\])

Using the Python built-in vars() call...
- *difficult to parse*
- *full response can include non-relevant information*
```
>>> vars(r)
{'_content': b'\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n  <link rel="dns-prefetch" href="https://github.githubassets.com">\n  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">\n  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">\n  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">\n  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">\n  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">\n  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">

<<<20 lines removed for readability here, only for this example>>>

', '_content_consumed': True, '_next': None, 'status_code': 200, 'headers': {'date': 'Thu, 09 Jul 2020 08:30:23 GMT', 'content-type': 'text/html; charset=utf-8', 'server': 'GitHub.com', 'status': '200 OK', 'vary': 'X-Requested-With, Accept-Encoding, Accept, X-Requested-With, Accept-Encoding', 'etag': 'W/"4cb794e9c5cb47d1844b6ae53f226c78"', 'cache-control': 'max-age=0, private, must-revalidate', 'strict-transport-security': 'max-age=31536000; includeSubdomains; preload', 'x-frame-options': 'deny', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'referrer-policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'expect-ct': 'max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"', 'content-security-policy': "default-src 'none'; base-uri 'self'; block-all-mixed-content; connect-src 'self' uploads.github.com www.githubstatus.com collector.githubapp.com api.github.com www.google-analytics.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com cdn.optimizely.com logx.optimizely.com/v1/events wss://live.github.com wss://alive.github.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com; frame-ancestors 'none'; frame-src render.githubusercontent.com; img-src 'self' data: github.githubassets.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com *.githubusercontent.com; manifest-src 'self'; media-src 'none'; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; worker-src github.com/socket-worker.js gist.github.com/socket-worker.js", 'Content-Encoding': 'gzip', 'Set-Cookie': '_gh_sess=5nmk4kZpPurzgoey6Bsly9F4o0XnbNiiXe4nr95JeZij9RljPF4bMXi1dv8NcJbI%2BSKLTogXIjrTqxa9utrvPEKsgDqBR%2FgAG8%2FyDnx1Sp0DSGtKYWfzjVh12RV5GXTpBRfcAS7SHusZYIUjV20wfyVXv95S39u1fZgoNbEvS0ELRj7QnNA5nauf2t3MFU2U9%2BHEp58mFOnxlm5rOfSo5llgF1KIC25OeYjdxSZ18Z9w9OelxpiM57Y%2Fb5Arb4yYn1Fliq14QB7wAXqkrveUNw%3D%3D--EVZtRV00B4WQ99sE--0rMgj86hLP%2BpiElJvDtDWA%3D%3D; Path=/; HttpOnly; Secure; SameSite=Lax, _octo=GH1.1.1678721293.1594283423; Path=/; Domain=github.com; Expires=Fri, 09 Jul 2021 08:30:23 GMT; Secure; SameSite=Lax, logged_in=no; Path=/; Domain=github.com; Expires=Fri, 09 Jul 2021 08:30:23 GMT; HttpOnly; Secure; SameSite=Lax', 'Accept-Ranges': 'bytes', 'Transfer-Encoding': 'chunked', 'X-GitHub-Request-Id': '3FDF:0CCF:1BDB827:27F8C90:5F06D59F'}, 'raw': <urllib3.response.HTTPResponse object at 0x7f37e4903a90>, 'url': 'https://github.com/rbed23', 'encoding': 'utf-8', 'history': [<Response [301]>], 'reason': 'OK', 'cookies': <RequestsCookieJar[Cookie(version=0, name='_octo', value='GH1.1.1678721293.1594283423', port=None, port_specified=False, domain='.github.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=True, expires=1625819423, discard=False, comment=None, comment_url=None, rest={'SameSite': 'Lax'}, rfc2109=False), Cookie(version=0, name='logged_in', value='no', port=None, port_specified=False, domain='.github.com', domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=True, expires=1625819423, discard=False, comment=None, comment_url=None, rest={'HttpOnly': None, 'SameSite': 'Lax'}, rfc2109=False), Cookie(version=0, name='_gh_sess', value='5nmk4kZpPurzgoey6Bsly9F4o0XnbNiiXe4nr95JeZij9RljPF4bMXi1dv8NcJbI%2BSKLTogXIjrTqxa9utrvPEKsgDqBR%2FgAG8%2FyDnx1Sp0DSGtKYWfzjVh12RV5GXTpBRfcAS7SHusZYIUjV20wfyVXv95S39u1fZgoNbEvS0ELRj7QnNA5nauf2t3MFU2U9%2BHEp58mFOnxlm5rOfSo5llgF1KIC25OeYjdxSZ18Z9w9OelxpiM57Y%2Fb5Arb4yYn1Fliq14QB7wAXqkrveUNw%3D%3D--EVZtRV00B4WQ99sE--0rMgj86hLP%2BpiElJvDtDWA%3D%3D', port=None, port_specified=False, domain='github.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=True, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None, 'SameSite': 'Lax'}, rfc2109=False)]>, 'elapsed': datetime.timedelta(microseconds=934239), 'request': <PreparedRequest [GET]>, 'connection': <requests.adapters.HTTPAdapter object at 0x7f37e3e85710>}
```

Versus using this module's dump_vars() call...
- *more readable output*
- *value items truncated for clarity*
- *variable length for truncation*
```
>>> dump_vars(r)
{
    "_next": "None",
    "_content_consumed": "True",
    "_content": "b'\\n<!DOCTYPE html>\\n<html lang=\"en\">\\n  <head>\\n  (<<<---truncated)",
    "connection": "<requests.adapters.HTTPAdapter object at 0x7f37e3e (<<<---truncated)",
    "cookies": "<RequestsCookieJar[<Cookie _octo=GH1.1.1678721293. (<<<---truncated)",
    "elapsed": "0:00:00.934239",
    "encoding": "utf-8",
    "headers": "{'date': 'Thu, 09 Jul 2020 08:30:23 GMT', 'content (<<<---truncated)",
    "history": "[<Response [200]>]",
    "raw": "<urllib3.response.HTTPResponse object at 0x7f37e49 (<<<---truncated)",
    "reason": "OK",
    "request": "<PreparedRequest [GET]>",
    "status_code": "200",
    "url": "https://github.com/rbed23"
}
```

Additional examples, using 'trunc' and 'keys' arguments...

```
>>> dump_vars(r, keys=True)
[
  "_content",
  "_content_consumed",
  "_next",
  "connection",
  "cookies",
  "elapsed",
  "encoding",
  "headers",
  "history",
  "raw",
  "reason",
  "request",
  "status_code",
  "url"
]

>>> dump_vars(r, trunc=300)
{
    "_next": "None",
    "_content_consumed": "True",
    "_content": "b'\\n<!DOCTYPE html>\\n<html lang=\"en\">\\n  <head>\\n    <meta charset=\"utf-8\">\\n  <link rel=\"dns-prefetch\" href=\"https://github.githubassets.com\">\\n  <link rel=\"dns-prefetch\" href=\"https://avatars0.githubusercontent.com\">\\n  <link rel=\"dns-prefetch\" href=\"https://avatars1.githubusercontent.com\">\\n  <li (<<<---truncated)",
    "connection": "<requests.adapters.HTTPAdapter object at 0x7f37e3e85710>",
    "cookies": "<RequestsCookieJar[<Cookie _octo=GH1.1.1678721293.1594283423 for .github.com/>, <Cookie logged_in=no for .github.com/>, <Cookie _gh_sess=5nmk4kZpPurzgoey6Bsly9F4o0XnbNiiXe4nr95JeZij9RljPF4bMXi1dv8NcJbI%2BSKLTogXIjrTqxa9utrvPEKsgDqBR%2FgAG8%2FyDnx1Sp0DSGtKYWfzjVh12RV5GXTpBRfcAS7SHusZYIUjV20wfyVXv95S3 (<<<---truncated)",
    "elapsed": "0:00:00.934239",
    "encoding": "utf-8",
    "headers": "{'date': 'Thu, 09 Jul 2020 08:30:23 GMT', 'content-type': 'text/html; charset=utf-8', 'server': 'GitHub.com', 'status': '200 OK', 'vary': 'X-Requested-With, Accept-Encoding, Accept, X-Requested-With, Accept-Encoding', 'etag': 'W/\"4cb794e9c5cb47d1844b6ae53f226c78\"', 'cache-control': 'max-age=0, priva (<<<---truncated)",
    "history": "[<Response [301]>]",
    "raw": "<urllib3.response.HTTPResponse object at 0x7f37e4903a90>",
    "reason": "OK",
    "request": "<PreparedRequest [GET]>",
    "status_code": "200",
    "url": "https://github.com/rbed23"
}
```
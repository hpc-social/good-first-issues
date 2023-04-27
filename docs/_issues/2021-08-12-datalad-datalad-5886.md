---
tags: DX,tests
title: "Should sleep/retry a few times upon 'Network is unreachable'"
html_url: "https://github.com/datalad/datalad/issues/5886"
user: yarikoptic
repo: datalad/datalad
---

During local tests got following test failure

```
======================================================================
ERROR: datalad.downloaders.tests.test_s3.test_restricted_bucket_on_NDA('s3://NDAR_Central_4/submission_23075/README', 'error', 'BIDS')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.9/urllib/request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "/usr/lib/python3.9/http/client.py", line 1255, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/lib/python3.9/http/client.py", line 1301, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/lib/python3.9/http/client.py", line 1250, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/lib/python3.9/http/client.py", line 1010, in _send_output
    self.send(msg)
  File "/usr/lib/python3.9/http/client.py", line 950, in send
    self.connect()
  File "/usr/lib/python3.9/http/client.py", line 1417, in connect
    super().connect()
  File "/usr/lib/python3.9/http/client.py", line 921, in connect
    self.sock = self._create_connection(
  File "/usr/lib/python3.9/socket.py", line 843, in create_connection
    raise err
  File "/usr/lib/python3.9/socket.py", line 831, in create_connection
    sock.connect(sa)
OSError: [Errno 101] Network is unreachable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/nose/case.py", line 197, in runTest
    self.test(*self.arg)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/tests/utils.py", line 764, in _wrap_with_tempfile
    return t(*(arg + (filename,)), **kw)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/tests/test_http.py", line 279, in check_download_external_url
    downloaded_path = downloader.download(url, path=d)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/base.py", line 520, in download
    return self.access(self._download, url, path=path, **kwargs)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/base.py", line 165, in access
    used_old_session = self._establish_session(url, allow_old=allow_old_session)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/s3.py", line 228, in _establish_session
    self._bucket = try_multiple_dec_s3(self.authenticator.authenticate)(
  File "/home/yoh/proj/datalad/datalad-maint/datalad/utils.py", line 2032, in _wrap_try_multiple_dec
    return f(*args, **kwargs)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/s3.py", line 106, in authenticate
    credentials = credential()
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/credentials.py", line 310, in __call__
    next_fields = adapter(self, **fields)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/downloaders/credentials.py", line 324, in _nda_adapter
    token = gen.generate_token(user, password)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/support/third/nda_aws_token_generator.py", line 34, in generate_token
    return self.__make_request(request_xml)
  File "/home/yoh/proj/datalad/datalad-maint/datalad/support/third/nda_aws_token_generator.py", line 81, in __make_request
    response = urllib_request.urlopen(request)
  File "/usr/lib/python3.9/urllib/request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.9/urllib/request.py", line 517, in open
    response = self._open(req, data)
  File "/usr/lib/python3.9/urllib/request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "/usr/lib/python3.9/urllib/request.py", line 494, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.9/urllib/request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "/usr/lib/python3.9/urllib/request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 101] Network is unreachable>

```

and in that `try_multiple_dec_s3` we only retry on:

```
                exceptions=S3ResponseError,
                exceptions_filter=_check_S3ResponseError,
```

where adding `urllib.error.URLError` to `exceptions` might do the trick, but `_check_S3ResponseError` might need tune up to ensure that it returns True (should be retried) on that one.

Test should mock `urllib_request.urlopen` so it first fails with that unreachable error and then proceeds on subsequent run.  URL to try on could be any of the ones we already use, e.g. `s3://datalad-test0-versioned/2versions-nonversioned1.txt` although this one would not trigger auth code path like here, so we should try on multiple , e.g. also on `3://NDAR_Central_4/submission_23075/README` used here (but requires NDA authorization for this one)
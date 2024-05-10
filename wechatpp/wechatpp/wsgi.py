"""
WSGI config for wechatpp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wechatpp.settings')

application = get_wsgi_application()


#{'type': 'websocket', 'path': '/ws/chat_2/', 'raw_path': b'/ws/chat_2/', 'root_path': '', 'headers': [(b'host', b'127.0.0.1:8000'), (b'connection', b'Upgrade'), (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), 
#(b'user-agent', b'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0'), (b'upgrade', b'websocket'), (b'origin', b'http://127.0.0.1:8000'), (b'sec-websocket-version', b'13'), (b'accept-encoding', b'gzip, deflate, br'), (b'accept-language', b'en-US,en;q=0.9'), (b'cookie', b'exampleCookie1=value1; exampleCookie2=value2; cookieConsent=1; csrftoken=pLRJ8HsUOxDKFkIeuxyX0WjNzAjNs4Ev; sessionid=i5vpcabujbbifeiod73rctyeof2384ie'), (b'sec-websocket-key', b'VPJsRx2iZ2O5JXO00kcQBQ=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')], 'query_string': b'', 'client': ['127.0.0.1', 50782], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 'cookies': {'exampleCookie1': 'value1', 'exampleCookie2': 'value2', 'cookieConsent': '1', 'csrftoken': 'pLRJ8HsUOxDKFkIeuxyX0WjNzAjNs4Ev', 'sessionid': 'i5vpcabujbbifeiod73rctyeof2384ie'}, 'session': <django.utils.functional.LazyObject object at 0x000002B5ACD29F60>, 'user': <channels.auth.UserLazyObject object at 0x000002B5ACD2B280>, 'path_remaining': '', 'url_route': {'args': (), 'kwargs': {'room_slug': 'chat_2'}}}
# feature_extractor.py
import re
from urllib.parse import urlparse

# A list of common URL shortening services. Phishers often use them to hide the real destination.
SHORTENING_SERVICES = [
    'bit.ly', 'goo.gl', 'shorte.st', 'go2l.ink', 'x.co', 't.co', 'tinyurl', 'tr.im', 'is.gd',
    'cli.gs', 'yfrog.com', 'migre.me', 'ff.im', 'url4.eu', 'twit.ac', 'su.pr', 'twurl.nl',
    'snipurl.com', 'short.to', 'BudURL.com', 'ping.fm', 'post.ly', 'Just.as', 'bkite.com',
    'snipr.com', 'fic.kr', 'loopt.us', 'doiop.com', 'short.ie', 'kl.am', 'wp.me', 'rubyurl.com',
    'om.ly', 'to.ly', 'bit.do', 't.mp', 'lnkd.in', 'db.tt', 'qr.ae', 'adf.ly', 'goo.by',
    'cur.lv', 'tiny.cc', 'alturl.com', 'ow.ly', 'bitly.com', 'youtu.be'
]

def extract_features(url):
    """
    Extracts a wide range of lexical and host-based features from a URL.

    Args:
        url (str): The URL to analyze.

    Returns:
        dict: A dictionary of extracted features.
    """
    features = {}
    
    # Ensure the URL has a scheme for proper parsing
    if not url.startswith('http'):
        url = 'http://' + url

    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname if parsed_url.hostname else ''
        path = parsed_url.path

        # 1. Address Bar Based Features
        features['hostname_length'] = len(hostname)
        features['path_length'] = len(path)
        features['url_length'] = len(url)
        features['fd_length'] = len(path.split('/')[1]) if len(path.split('/')) > 1 else 0
        features['count_subdomains'] = hostname.count('.')

        # 2. Domain Based Features
        features['having_ip_address'] = 1 if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", hostname) else 0
        features['has_shortening_service'] = 1 if any(service in hostname for service in SHORTENING_SERVICES) else 0

        # 3. Symbol Based Features
        features['count_dash'] = url.count('-')
        features['count_at'] = url.count('@')
        features['count_question'] = url.count('?')
        features['count_percent'] = url.count('%')
        features['count_dot'] = url.count('.')
        features['count_equal'] = url.count('=')
        features['count_http'] = url.count('http')
        features['count_https'] = url.count('https')
        features['count_www'] = url.count('www')

        # 4. Lexical Features
        features['count_digits'] = sum(c.isdigit() for c in url)
        features['count_letters'] = sum(c.isalpha() for c in url)
        
        hostname_letters = sum(c.isalpha() for c in hostname)
        hostname_digits = sum(c.isdigit() for c in hostname)
        features['hostname_digit_letter_ratio'] = hostname_digits / (hostname_letters + 1)

        sensitive_words = ['secure', 'login', 'signin', 'bank', 'account', 'verify', 'password', 'update']
        features['has_sensitive_words'] = 1 if any(word in url.lower() for word in sensitive_words) else 0

    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
        feature_keys = [
            'hostname_length', 'path_length', 'url_length', 'fd_length', 'count_subdomains',
            'having_ip_address', 'has_shortening_service', 'count_dash', 'count_at',
            'count_question', 'count_percent', 'count_dot', 'count_equal', 'count_http',
            'count_https', 'count_www', 'count_digits', 'count_letters',
            'hostname_digit_letter_ratio', 'has_sensitive_words'
        ]
        features = {key: 0 for key in feature_keys}

    return features


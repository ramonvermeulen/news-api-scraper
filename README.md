### News API scraper


Powered by [**NewsAPI.org**](https://newsapi.org/)

Example `config.cfg`
```
[MAIN]
API_URL=https://newsapi.org/v2/
API_KEY=some_api_key
API_KEY_QUERY_PARAM_KEYWORD=apiKey
API_ROUTE=everything
SEARCH_QUERY_PARAM_KEYWORD=query
SEARCH_KEYWORD=alfen

[MAIL]
MAIL_RECEIVERS=['email@list.com', 'anothermail@email.com']
MAIL_AUTH_EMAIL=some@email.com
MAIL_AUTH_PASSWORD=some_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
INTERVAL=5
```
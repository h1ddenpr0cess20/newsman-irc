# newsman-irc
An AI newsroom for IRC which reports news by category in the style of a tv news report, including general, business, sports, entertainment, science, technology, health, and weather.  Powered by NewsAPI, WeatherAPI and OpenAI gpt-3.5-turbo.

## Setup
```
pip3 install openai irc
```
Fill in your [OpenAI API](https://platform.openai.com/signup) key, [NewsAPI](https://newsapi.org/account) key, [WeatherAPI](https://www.weatherapi.com/my/) key, IRC server, username, and channel

## Use
```
python3 newsman.py
```

### Avaiable commands

!news

!business

!entertainment

!general

!health

!science

!sports

!technology

!politics

!weather _location_

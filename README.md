# newsman-irc
An AI newsroom with news, sports, entertainment, science, technology, health, and weather for IRC powered by NewsAPI, WeatherAPI and OpenAI gpt-3.5-turbo which reports news by category in the style of a tv news report.

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

!news _news report with no category_

!business

!entertainment

!general

!health

!science

!sports

!technology

!weather _location_

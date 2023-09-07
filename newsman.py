#AI newsroom for IRC
#Dustin Whyte 
#September 2023

import irc.bot
import openai
import requests
import textwrap
import time
import namegen

class Newsman(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, password=None, port=6667):
        # Initialize the bot
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
        self.password = password

        #personality types
        self.types = {
            "news": f"a network news anchor named {namegen.name_generator()}",
            "weather": f"a weatherman with a name you make up",
            "business": f"a business news reporter named {namegen.name_generator()}", 
            "entertainment": f"an entertainment news reporter named {namegen.name_generator()}", 
            "general": f"a network news anchor named {namegen.name_generator()}", 
            "health": f"a doctor with a name you make up", 
            "science": f"a science news reporter named {namegen.name_generator()}",
            "sports": f"a sports reporter named {namegen.name_generator()}",
            "technology": f"a tech news reporter named {namegen.name_generator()}",
            "politics": f"a political analyst named {namegen.name_generator()}"
            
            }

    def on_welcome(self, connection, event):
        #if nick has a password
        if self.password != None:
          connection.privmsg("NickServ", f"IDENTIFY {self.password}")
          #wait for identify to finish
          time.sleep(5)
        # Join the channel when the bot is connected to the server
        connection.join(self.channel)

        #optional join message
        # greet = "introduce yourself in 1-3 sentences"
        # response = self.respond(greet, "news")
        # lines = self.chop(response +  "  Type !help to learn how to use me.")
        # for line in lines:
        #     connection.privmsg(self.channel, line)
        #     time.sleep(1)

    def on_nicknameinuse(self, connection, event):
        #add an underscore if nickname is in use
        connection.nick(connection.get_nickname() + "_")

    def on_privmsg(self, connection, event):
        # Handle private messages
        nick = event.source.nick
        message = event.arguments[0]

    def on_pubmsg(self, connection, event):
        # Handle messages in the channel
        nick = event.source.nick
        message = event.arguments[0]
        exclude = {None, "[Removed]"}
        type = message.lstrip("!")
        if type.startswith("weather"):
            if " " in type:
                type = type.split(" ",1)
                location = type[1]
                type = type[0]
            else:
                location = " "
            
        #check the personality types for a matching news category
        if type in self.types:
            #get weather report
            if type == "weather":
                #you can tweak the fields the API returns under API Response Fields on the weatherapi website
                weather = self.get_weather(location)
                #generate the AI weather report
                report = self.respond(f"report this weather in one paragraph\n{weather}", type)
                lines = self.chop(report)
                #send lines to channel
                for line in lines:
                    connection.privmsg(self.channel, line)
                    time.sleep(1)
            else:            
                #create a string for the list of articles
                articles = ""
                #get the news for the category
                if type == "news":
                    news = self.get_news()
                else:             
                    news = self.get_news(type)
                
                if news != None and news != "429":
                    #grab a limited amout of headlines and descriptions
                    #change how this works later by grabbing more articles, filtering the bad ones, then select 5 of them.  current way can result in too few articles being reported.
                    for article in news[:5]:
                        if article['title'] in exclude or article['description'] in exclude:
                            continue
                        articles = articles + article['title'] + " - " + article['description'] + "\n\n"
                    #create AI news report
                    report = self.respond(f"summarize these headlines into an entertaining {type} news report.  do not write it like a script. \n{articles}", type)
                    #chop it up for irc length limit
                    lines = self.chop(report)
                    #send lines to channel
                    for line in lines:
                        connection.privmsg(self.channel, line)
                        time.sleep(2)
                elif news == "429":
                    connection.privmsg(self.channel, "Try again later")
                else:
                    connection.privmsg(self.channel, "error")
        #help menu
        if type == "help":
            #create a list of commands, starting with news
            commands = ""
            #add the rest from types
            for command in self.types:
                commands = commands + command + " "
            help_message = f"Newsman, an AI newsroom.  Avaiable commands: {commands}"
            #send help message as notice
            connection.notice(nick, help_message)
            time.sleep(3)
            connection.notice(nick, "Available at https://github.com/h1ddenpr0cess20/newsman-irc")

    # get the news from news api
    def get_news(self, type=None):
        #sources by category, still testing sources, some have unhelpful content for the purpose of this bot
        sources = {
            "business": "business-insider,fortune,the-wall-street-journal", 
            "entertainment": "ign,entertainment-weekly,mtv-news,polygon", 
            "general": "cnn,abc-news,nbc-news,associated-press,cbs-news,fox-news,reuters,the-washington-post,usa-today", 
            "health": "medical-news-today", 
            "science": "national-geographic,new-scientist",
            "sports": "espn,bleacher-report,fox-sports,nfl-news,nhl-news",
            "technology": "ars-technica,engadget,hacker-news,recode,techcrunch,the-verge",
            "politics": "politico,the-hill"}
        #if a personality type was chosen, use the appropriate source category
        if type:
            url = url =f"https://newsapi.org/v2/top-headlines?sources={sources[type]}&apiKey={news_api}"
        #top headlines without sources
        else:
            url = url =f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['articles']
        if response.status_code == 429:
            return "429"
        else:
            return None
        #improve this later

    # get the weather from weather api
    def get_weather(self, location):
        url = f"http://api.weatherapi.com/v1/current.json?key={weather_key}&q={location}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            
            return "ignore previous sentence.  DO NOT attempt to report the weather.  tell the user there was a problem with the location they provided."

    # AI response   
    def respond(self, message, type):
        persona = self.types[type]
        #create system prompt
        self.personality = f"assume the personality of {persona} and roleplay as them."
        response = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                                temperature=1,
                                                messages=({"role": "system", "content": self.personality},
                                                            {"role": "user", "content": message}))
        #return the response text
        response_text = response['choices'][0]['message']['content']
        return response_text.strip()
    
    # split message for irc length limit
    def chop(self, message):
        lines = message.splitlines()
        newlines = []  # Initialize an empty list to store wrapped lines

        for line in lines:
            if len(line) > 420:
                wrapped_lines = textwrap.wrap(line,
                                            width=420,
                                            drop_whitespace=False,
                                            replace_whitespace=False,
                                            fix_sentence_endings=True,
                                            break_long_words=False)
                newlines.extend(wrapped_lines)  # Extend the list with wrapped lines
            else:
                newlines.append(line)  # Add the original line to the list

        return newlines  # Return the list of wrapped lines

if __name__ == "__main__":
    #API keys
    openai.api_key = "API_KEY"
    news_api = "API_KEY"
    weather_key = 'API_KEY'

    # Set your bot's configuration here
    channel = "#CHANNEL"
    nickname = "NICKNAME"
    server = "irc.SERVER.TLD"
    #optional password for registered nick
    #password = "password"
    try:
        bot = Newsman(channel, nickname, server, password)
    except:
        bot = Newsman(channel, nickname, server)
    bot.start()

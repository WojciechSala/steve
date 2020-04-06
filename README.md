# What's Steve?

Steve is a voice OS manager. It simply manages your OS and other apps by commands like Cortana or Siri does.

###### May remake the project in the future but with own ML algorithm avoiding google speech recognition API as it's too slow to wait for the response.

---

## Challenges and conclusions

- Speech recognition form google in form of API is too slow to manage the OS fast and comfortable enough.
- The most interesting part lies behind the AI and using API just "black boxes" the whole project.
- Dialects and different microphone settings are a big variables that change everything and need to be very specific to make recognition accurate.

---

## Installation

To run the project you will need [Python 2.5 or lower](https://www.python.org/downloads/release/python-252/) since the dependencies used in the project were removed in next versions.

You will need to ``` pip install ``` all third party dependencies from main.py and your are ready to go.

###### Note that there is a delay caused by google API so you will need to wait few seconds for an action, you can make sure everything is ok console logging the input.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

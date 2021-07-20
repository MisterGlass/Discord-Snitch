# Discord Snitch, v1

## Dockerfile & VSCode devcontainer included

There are five settings:
- DISCORD_TOKEN: An API token for discord
- ALERT_CHANNEL: The channel you wish discord snitch to report to
- WORD_LIST: The name of a file in this directory containing the list of words you wish to watch
- IGNORED_CHANNELS: A comma-separated list of channel names to not report on
- IGNORED_ROLES: A comma-separated list of channel names to not report on

The word list file should be a text file with one word per line.

### Devcontainer usage:
   - Copy `.devcontainer/devcontainer.env.dist` to `.devcontainer/devcontainer.env`
   - In the file, set the five environment variables: DISCORD_TOKEN, WORD_LIST, ALERT_CHANNEL IGNORED_CHANNELS & IGNORED_ROLES
   - Run app.py (F5)


### Regular usage:
   - Install the dependencies with poetry
   - Add a wordlist of your choice
   - Set five environment variables: DISCORD_TOKEN, WORD_LIST, ALERT_CHANNEL IGNORED_CHANNELS & IGNORED_ROLES
   - Run app.py with Python3


### Docker usage:
   - Add a wordlist of your choice
   - Build the dockerfile with the following command `docker build . -f .devcontainer/Dockerfile -t your-tag`
   - Copy `.devcontainer/devcontainer.env.dist` to `.devcontainer/devcontainer.env`
   - In the file, set the five environment variables: DISCORD_TOKEN, WORD_LIST, ALERT_CHANNEL IGNORED_CHANNELS & IGNORED_ROLES
   - Run the dockerfile with the following command `docker run --env-file .devcontainer/devcontainer.env your-tag`

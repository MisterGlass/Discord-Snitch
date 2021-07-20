# Discord Snitch, v1

A simple python script to log & report use of certain words within a discord server to moderators.

## Dockerfile & VSCode devcontainer included

There are six settings:
- ALERT_CHANNEL: The channel you wish discord snitch to report to.
- DISCORD_TOKEN: An API token for discord.
- IGNORED_CHANNELS: A comma-separated list of channels to not report on.
- IGNORED_ROLES: A comma-separated list of roles to not report on.
- LOG_FILE (optional): Location to log events to. Leave blank for stdout.
- WORD_LIST: The file containing the list of words you wish to watch. Supports a relative filename or a full path.

The word list file should be a text file with one word per line.

### Devcontainer usage:
   - Copy `.devcontainer/devcontainer.env.dist` to `.devcontainer/devcontainer.env`
   - In the file, set the six environment variables
   - Run app.py (F5)


### Regular usage:
   - Install the dependencies with poetry
   - Add a wordlist of your choice
   - Set six environment variables
   - Run app.py with Python3


### Suggested Docker usage:
   - Add a wordlist of your choice
   - Build the dockerfile with the following command `docker build . -f .devcontainer/Dockerfile -t your-tag`
   - Copy `.devcontainer/devcontainer.env.dist` to `.devcontainer/devcontainer.env`
   - In the file, set the six environment variables
   - Run the dockerfile with the following command `docker run --env-file .devcontainer/devcontainer.env your-tag`

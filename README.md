Discord Snitch, v1

Dockerfile & VSCode devcontainer included

Devcontainer usage:
   Copy `.devcontainer/devcontainer.env.dist` to `.devcontainer/devcontainer.env.dist`
   Fill in the approiate settings in the env file
   Run app.py (F5)

Regular usage:
   Install the dependencies with poetry
   Add a wordlist of your choice
   Set three environment variables: DISCORD_TOKEN, WORD_LIST & ALERT_CHANNEL
   Output is all printed to stdout

# MineDiscBot

## Table of contents
- [MineDiscBot](#minediscbot)
  - [Table of contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
- [Discord](#discord)
- [Discord bot](#discord-bot)
- [Minecraft server](#minecraft-server)
- [MineAPI Minecraft API](#mineapi-minecraft-api)
- [Docker](#docker)
- [Ansible](#ansible)
  - [SSH key](#ssh-key)
- [Github Actions](#github-actions)
  - [Secrets](#secrets)
  - [Environment variables](#environment-variables)

## Description
This is a Discord bot to get information about Minecraft servers how the status of the server or the number of players. If you haven't a Minecraft server, you can use the following repository to deploy a **[Minecraft server](https://github.com/francisjgarcia/minecraft)**.

## Requirements
Before to deploy the infrastructure and provision the server, you must need the following resources:

- [Discord](https://discord.com)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Minecraft server](https://github.com/francisjgarcia/minecraft)
- [MineAPI Minecraft API](https://github.com/francisjgarcia/mineapi)
- [Docker](https://www.docker.com)
- [Ansible](https://www.ansible.com)
- [GitHub Actions](https://github.com/features/actions)


# Discord
In the Discord server, you must create a channel where the bot will send the information about the Minecraft server. The channels must be named of the following way:

- Estado: Offline
- Jugadores: 0/0

# Discord bot

To create a Discord bot, you must create an application in the **[Discord Developer Portal](https://discord.com/developers/applications)**. Then, you must create a bot and copy the token.

To allow the bot to connect to the Discord server, you must create an OAuth2 URL with the following scopes:

- bot

Next, you must copy the URL and paste it in your browser and select the server where you want to add the bot.

# Minecraft server
You must have a Minecraft server deployed. If you haven't a Minecraft server, you can use the following repository to deploy a **[Minecraft server](https://github.com/francisjgarcia/minecraft)**.

# MineAPI Minecraft API
You must have a MineAPI Minecraft API deployed. If you haven't a MineAPI Minecraft API, you can use the following repository to deploy a **[Minecraft API](https://github.com/francisjgarcia/mineapi)**.

# Docker
To deploy the bot in local, you must have Docker installed in your computer. Then, you must clone the repository and copy the file **.env.example** to **.env** in the path .app and edit the file with the following information:

```bash
STATUS_API_URL=<STATUS-API-URL> # URL of the status API
DISCORD_BOT_TOKEN=<DISCORD-BOT-TOKEN> # Discord bot token
DISCORD_PLAY_GAME=<DISCORD-PLAY-GAME> # Name of the game the bot will play
DISCORD_STATUS_CHANNEL_ID=<DISCORD-STATUS-CHANNEL-ID> # ID of the channel where the bot will post the status of the server
DISCORD_PLAYERS_CHANNEL_ID=<DISCORD-PLAYERS-CHANNEL-ID> # ID of the channel where the bot will post the players online
```

Finally, you must run the following command to deploy the bot:

```bash
cd infra/docker
docker-compose up -d
```

# Ansible
If you have a server where you want to deploy the bot, you must have Ansible installed in your computer. Then, you must export the following environment variables:

```bash
export GHCR_PAT="<GITHUB-PERSONAL-ACCESS-TOKEN>" # Personal access token of GitHub
export REPOSITORY_USERNAME="<GITHUB-USERNAME>" # Username of GitHub
export IMAGE_NAME="<IMAGE-NAME>" # Name of the image
export IMAGE_TAG="<IMAGE-TAG>" # Tag of the image
export STATUS_API_URL="<STATUS-API-URL>" # URL of the status API
export DISCORD_BOT_TOKEN="<DISCORD-BOT-TOKEN>" # Discord bot token
export DISCORD_PLAY_GAME="<DISCORD-PLAY-GAME>" # Name of the game the bot will play
export DISCORD_STATUS_CHANNEL_ID="<DISCORD-STATUS-CHANNEL-ID>" # ID of the channel where the bot will post the status of the server
export DISCORD_PLAYERS_CHANNEL_ID="<DISCORD-PLAYERS-CHANNEL-ID>" # ID of the channel where the bot will post the players online
```

## SSH key
To deploy the bot in the server, you must have a SSH key. If you don't have a SSH key, you must create it with the following commands:

```bash
ssh-keygen -t rsa -b 4096 -C "MineDiscBot"
```

And next, you need evaluate the ssh-agent and add the private key:

```bash
eval $(ssh-agent)
ssh-add /path/to/private/key
```

If you not automate the deployment, you must copy manually the public key in the server.

Finally, you must run the following command to deploy the bot in the server:

```bash
ansible-playbook -u root -i '<SERVER-IP or DNS>,' infra/ansible/playbooks/main.yml
```

# Github Actions
To automate the deployment, you can use **Github Actions**. You must *fork* this repository or using the repository template and create the following secrets and environment variables:

## Secrets

```bash
GHCR_PAT="<GITHUB-PERSONAL-ACCESS-TOKEN>" # Personal access token of GitHub
DISCORD_BOT_TOKEN="<DISCORD-BOT-TOKEN>" # Discord bot token
SSH_PRIVATE_KEY="<SSH-PRIVATE-KEY>" # Private key of SSH
```

## Environment variables

```bash
STATUS_API_URL="<STATUS-API-URL>" # URL of the status API
DISCORD_PLAY_GAME="<DISCORD-PLAY-GAME>" # Name of the game the bot will play
DISCORD_STATUS_CHANNEL_ID="<DISCORD-STATUS-CHANNEL-ID>" # ID of the channel where the bot will post the status of the server
DISCORD_PLAYERS_CHANNEL_ID="<DISCORD-PLAYERS-CHANNEL-ID>" # ID of the channel where the bot will post the players online
SERVER_HOST="<SERVER-IP or DNS>" # IP or DNS of the server
```

The Github Actions will deploy the infrastructure and provision the server with Ansible. This process execute only when you push a commit in the repository to the **development** branch or when you create a **version tag** in the repository.

# Rocket Lab Coding Challenge

## System Requirements


## Getting Started
How do you run the app
  - include windows instructions
  - include mac/linux instructions

1. Copy `.env.example` to `.env`
```bash
cp .env.example .env
```
2. (optional) Customize values in `.env` file # TODO consider a Make target that prompts for inputs to build this for the user.
```bash
```
3. 


## Technology Selection
Why was each technology selected
 - `Python`: 
 - `git`: 
 - `GNU Make`:
 - `MongoDB`: A NoSQL database allows for simpler queries and app logic when it comes to adding child nodes of infinite size. To my knowledge there is no limit to the # of subdocs as long as the overall document size is < 16MB.
 - `Docker`: Ensures a consistent runtime environment for application.
 - `Docker Compose`: Simple orchestration for Database and API server that is portable to every machine.
 - `Motor`: Official async MongoDB driver for python.


## Challenges
What were the key challenges faced when implementing this solution

## Caveats and Downfalls
What are the engineering trade offs for this approach?

## Production Changes
What changes would be made for a production environment
 - packages are pinned to a specific version. In prod I would allow for some automatic upgrades of packages.
 - I would not name the folder for the backend code `be`. Something like `rocket-nodes` would be better.
 - I would not be using the root user credentials as the user/password for the application
 - 

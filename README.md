# Rocket Lab Coding Challenge

## Table of Contents

  - [Getting Started](#getting-started)
    - [Setup Instructions](#setup-instructions)
    - [Installing GNU Make](#installing-gnu-make)
  - [Technology Selection](#technology-selection)
  - [Challenges](#challenges)
  - [Caveats](#caveats)
  - [Production Changes](#production-changes)


## Getting Started

To make the setup process simpler most of the commands for building and running the application exist as `GNU Make` targets. If the `make` command isn't installed on your system
see the [Instaling GNU Make](#installing-gnu-make) section below which contains instructions for installing on Mac, Linux, and Windows.

Since the API also requires a MongoDB server running a `docker-compose.yml` has been provided that will setup a MongoDB Server and API server on the same network. If you already
have MongoDB running on your system there is a `make` target for running the API outside of the Docker container.

### Setup Instructions

1. Copy `.env.example` to `.env` The .env file is used to specify a consistent set of environment variables for the API and Docker setup
```bash
cp .env.example .env
```
2. (optional) Customize values in `.env` file
3. Run the application
```bash
docker-compose up
# OR
make run # Note this assumes you have MongoDB running locally already
```

### Tests

What Tests?... just kidding of course there are tests. You can run tests with the following commands
```bash
make tests
# OR
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest tests -s
```

### Instaling GNU Make

 - [Mac](https://formulae.brew.sh/formula/make)
 - [Linux](https://www.incredibuild.com/integrations/gnu-make#:~:text=If%20you're%20on%20Linux,Fedora%2FRHEL%20%E2%80%93%20yum%20install%20make)
 - [Windows](https://gnuwin32.sourceforge.net/packages/make.htm)


## Technology Selection
Why was each technology selected
 - `Python`: Required to use FastAPI
 - `FastAPI`: Framework requested by interview team 
 - `git`: 
 - `GNU Make`: Allows for complex build/test commands to be hidden behind a simple make target. 
 - `MongoDB`: A NoSQL database allows for simpler queries and app logic when it comes to adding child nodes of infinite size. To my knowledge there is no limit to the # of subdocs as long as the overall document size is < 16MB. MongoDB's storage engine made it really simple to run the insert command that could build out an entire subtree rather than just a single node at a time.
 - `Docker`: Ensures a consistent runtime environment for application.
 - `Docker Compose`: Simple orchestration for Database and API server that is portable to every machine.
 - `Motor`: Official async MongoDB driver for python.


## Challenges

The most difficult part of the challenge was figuring out how to model and store the tree like data strucure. At first I went down the path
of traversing a standard dictionary object which lead to complex functions for searching and inserting sub-nodes and properties. Inserting a
sub-node in this approach was especially difficult because as I traversed down the tree I was loosing reference to the parent node which meant
the newly attached subnode didn't actually appear in the main tree structure.

I then went down the path of building a Node SubNode and NodeProperty class. This led to complex logic parsing a path into these classes and
parsing the dictionary returned from the DB into these classes. It also led to problems trying to serialize them into JSON when returning
them as the body of a JSONResponse.

Ultimately I landed on the simpler solution of leveraging MongoDB's search syntax which is very similar to the path's received in the Requests
to write the filter and update querys.


## Caveats and Downfalls

 - Given the data structure there could never be 2 Nodes with the same rot i.e. "Rocket"
 - MongoDB is limited at 16MB per doc so an incredibly large and complex node structure could exceed that limit.


## Production Changes

 - Currently all the packages are pinned to a specific version. In prod I would allow for some automatic upgrades of packages. i.e. >= 1.*.*
 - I would not name the folder for the backend code `be`. Something like `rocket-nodes` would be better.
 - I would not be using the databases root user credentials as the user/password for the application.
 - I would include logging lib instead of print statements.

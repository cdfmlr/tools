# My Tools

Personal tools: simple and useful.

Notice: some programs here were hard-coded for my own convenience. However, you can easily  tailor constants to fit your jobs.

## Setup

Just add the `active.sh` into your `~/.zshrc`:

```sh
source /path/to/tools/active.sh
```

Then all tools wil be ready.

## proxy

Proxy takes the http proxy on/off in current env by export/unset the `http_proxy`, `https_proxy`, `git config --global http.proxy`.

Usage:

```sh
$ proxy {on,off,do CMD}
    on      takes proxy on
    off     takes proxy off
    do CMD  run a command CMD with proxy on, then take the proxy off 
```

## minidocker

This script helps to start a docker demon by running `minikube start -p no-k8s-docker` and setting up docker env: `eval $(minikube -p no-k8s-docker docker-env)`.

Usage:

```sh
$ minidocker {start,stop}
```

## makegitignore

A command to fill `./.gitignore` with templates from [github.com/github/gitignore](https://github.com/github/gitignore).

Usage:

```sh
$ makegitignore [-h] [--default-envs] [--favorite] [--macos]
                         [--jetbrains] [--visualstudiocode] [--virtualenv]
                         [--c] [--go] [--python] [--node] [--lang LANG]
                         [--env ENV]
```

Run `makegitignore --help` for more details.


E.g.

```sh
$ makegitignore -d --go --lang Swift --lang TeX --env Windows
```

## f2utf8

Any text file to UTF-8.

```sh
f2utf8.py [-h] [-o OUTFILE] file

convert file to utf-8 encoded

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
```

## ignore_folders_in_spotlight

[SUDO] Make spotlight ignoring folders:

```sh
ignore_folders_in_spotlight [-h] [-n NAME] [-s SPOTLIGHT_PLIST_PATH] path

Ignore a path in Spotlight

positional arguments:
  path                  Path to ignore

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the path to ignore
  -s SPOTLIGHT_PLIST_PATH, --spotlight-plist-path SPOTLIGHT_PLIST_PATH
                        Path to the Spotlight plist
```

e.g. ignore all node_modules:

```sh
ignore_folders_in_spotlight -n node_modules /
```

## httpserve

A simple static http server with CORS allowed:

```sh
httpserve [-h] [--cgi] [--bind ADDRESS] [--directory DIRECTORY] [port]

positional arguments:
  port                  specify alternate port (default: 8000)

optional arguments:
  -h, --help            show this help message and exit
  --cgi                 run as CGI server
  --bind ADDRESS, -b ADDRESS
                        specify alternate bind address (default: all interfaces)
  --directory DIRECTORY, -d DIRECTORY
                        specify alternate directory (default: current directory)
```

e.g.

```sh
httpserve -d ./myweb 8000
```

## others

All kinds of clutter. Read the source code before using.

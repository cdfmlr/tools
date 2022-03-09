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

## others

All kinds of clutter. Read the source code before using.

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

## httpstatic

A golang alternative to `httpserve`, with better performance (maybe) and more features (e.g. 206).


```sh
httpstatic -d . -l :8080
```

Serving static files from a directory (`.`) over HTTP (`:8080`) with CORS allowed.
Notice the arguments are different from `httpserve`.

⚠️ Build before use (TODO: make a global Makefile for any required tools later):

```sh
cd ./httpstatic && make
```

## emsend

Send emails.

```sh
emsend [-f SENDER] [-p PASSWORD] [-m SMTP_HOST] [-t RECEIVERS]
       [-s SUBJECT] [-c CONTENT] [-a ATTACHMENTS] [-S SIGNATURE]

Send email.

optional arguments:
  -h, --help            show this help message and exit
  -f SENDER, --from SENDER
                        Sender email address. Default: None (set by MYEMAIL_SENDER)
  -p PASSWORD, --password PASSWORD
                        Sender email password. Default: None (set by MYEMAIL_PASSWORD)
  -m SMTP_HOST, --smtp SMTP_HOST
                        SMTP host. Default: None (set by MYEMAIL_SMTP_HOST)
  -t RECEIVERS, --to RECEIVERS
                        Receiver email address. Multiple receivers can be specified by
                        multiple -t options: -t receiver1 -t receiver2
  -s SUBJECT, --subject SUBJECT
                        subject, default: "No subject"
  -c CONTENT, --content CONTENT
                        content in plain text. Default: read from stdin
  -a ATTACHMENTS, --attachment ATTACHMENTS
                        attachment file path. Multiple attachments can be specified by
                        multiple -a options: -a attachment1 -a attachment2
  -S SIGNATURE, --signature SIGNATURE
                        signature, default: "<sender> <current time>"
```

example:

```sh
emsend -f foo@bar.com -p greetPassW0rd -m smtp.bar.com -t fuzz@buzz.com -s 'A test email'
<content from stdin>
```

```sh
export MYEMAIL_SENDER=foo@bar.com
export MYEMAIL_PASSWORD=greetPassW0rd
export MYEMAIL_SMTP_HOST=smtp.bar.com
emsend -t fuzz@buzz.com -a hello.jpg -c hello.txt
emsend --help | emsend -t fuzz@buzz.com -s 'emsend help'
```

## others

All kinds of clutter. Read the source code before using.

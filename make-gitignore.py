#!python3

"""make-gitignore.py:
A command to fill .gitignore file with templates from github.com/github/gitignore
"""

from typing import List
import requests
import argparse


HUB_URL = 'https://github.com/github/gitignore/blob/main'  # For human
RAW_URL = 'https://raw.githubusercontent.com/github/gitignore/main'  # For content


OUT_FILE = '.gitignore'

# For Debug

DEBUG = False


if DEBUG:
    debug = print
    OUT_FILE = 'out.gitignore'
else:
    def debug(*args, **kwargs):
        pass

# End Debug


class Gitignore(object):
    """https://github.com/github/gitignore/blob/main/{lang}.gitignore
    """

    def __init__(self, lang):
        self.lang = lang

    def _url(self, base_url):
        return f'{base_url}/{self.lang}.gitignore'

    def hub_url(self):
        return self._url(HUB_URL)

    def raw_url(self):
        return self._url(RAW_URL)

    def fetch_content(self):
        resp = requests.get(self.raw_url())
        if resp.status_code != 200:
            # common error: not such {lang}.gitignore
            if resp.status_code == 404:
                raise ValueError(
                    f'No gitignore template regarding "{self.lang}": {self.hub_url()} responses 404 not found')
            raise ValueError(f"{resp.status_code=}")
        return resp.content.decode('utf-8')


class GlobalGitignore(Gitignore):
    """https://github.com/github/gitignore/blob/main/Global/{lang}.gitignore
    """

    def __init__(self, env):
        super().__init__(f"Global/{env}")


# Common langs (for me).

# https://github.com/github/gitignore/blob/main/Global/{xxx}.gitignore
GLOBS_LIST = ['macOS', 'JetBrains', 'VisualStudioCode', 'VirtualEnv']
globs = {x.lower(): GlobalGitignore(x) for x in GLOBS_LIST}

# https://github.com/github/gitignore/blob/main/{xxx}.gitignore
LANGS_LIST = ['C', 'Go', 'Python', 'Node']
langs = {x.lower(): Gitignore(x) for x in LANGS_LIST}


# CLI
# There are 3 groups of flags:
# - Default (useful collections for me);
# - Common (select globs or langs defined above);
# - Custom (get HUB_URL/{file_name}.gitignore from user)

def cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=f'Append current git ignore config ({OUT_FILE}) with specific languages or environments templates.')

    # Default
    group_default = parser.add_argument_group('Recommended environments')
    group_default.add_argument(f'--default-envs', '-d',
                               action='store_true',
                               help=f'Default OS & editors: {GLOBS_LIST}')
    group_default.add_argument(f'--favorite', '-f',
                               action='store_true',
                               help=f'ALL MY FAVORITES: {GLOBS_LIST + LANGS_LIST}')

    # Common
    group_common_envs = parser.add_argument_group(
        'Common OS-specific or editor specific environments')
    for g in globs:
        group_common_envs.add_argument(f'--{g}',
                                       action='store_true',
                                       help=f'{globs[g].hub_url()}')

    group_common_langs = parser.add_argument_group(
        'Common Languages and technologies')
    for l in langs:
        group_common_langs.add_argument(f'--{l}',
                                        action='store_true',
                                        help=f'{langs[l].hub_url()}')

    # Custom
    group_custom = parser.add_argument_group(
        "Custom (these flags can be appended multi-times: e.g. --lang Swift --lang TeX)")
    group_custom.add_argument(f'--lang',
                              action='append',
                              type=str,
                              help=f'Custom language: {HUB_URL}/<LANG>.gitignore')
    group_custom.add_argument(f'--env',
                              action='append',
                              type=str,
                              help=f'Custom os/editor: {HUB_URL}/Global/<ENV>.gitignore')

    return parser


def tasks_manager(args: argparse.Namespace) -> List[Gitignore]:
    tasks: List[Gitignore] = []

    # default
    if args.favorite:
        tasks.extend(globs.values())
        tasks.extend(langs.values())
    if args.default_envs:
        tasks.extend(globs.values())

    # common
    commons = {**globs, **langs}
    for k in commons:
        if args.__dict__[k]:
            tasks.append(commons[k])

    # custom
    if args.env:
        tasks.extend([GlobalGitignore(e) for e in args.env])
    if args.lang:
        tasks.extend([Gitignore(l) for l in args.lang])

    return tasks


if __name__ == '__main__':
    # parse argv
    parser = cli_parser()
    args = parser.parse_args()
    debug(args)

    # tasks
    tasks = tasks_manager(args)
    debug([t.lang for t in tasks])

    if not tasks or len(tasks) == 0:
        print('Nothing to do!')
        parser.print_help()
        exit(1)

    # write .gitignore
    with open(OUT_FILE, 'a') as f:
        for gitignore in tasks:
            print(f'Add {gitignore.lang}...')
            content = gitignore.fetch_content()
            f.write(f'### {gitignore.hub_url()}\n{content}\n')

    print(f'Done: ignores appended to {OUT_FILE}')

#!/usr/bin/env python3

from subprocess import check_output

DOCUMENT_FOLDER = 'doc'
API_DOCUMENT_FOLDER = '{}/{}'.format(DOCUMENT_FOLDER, 'api')
SOURCE = 'everywhere'
MASTER_BRANCH = 'master'
HTML_DIR = 'html'


def run_cmd(cmd):
    print('running command: {}'.format(cmd))
    result = check_output(cmd.split())
    print(result.decode(), end='')
    return result


def build_docstring_rst():
    run_cmd('sphinx-apidoc -o {} {}'.format(API_DOCUMENT_FOLDER, SOURCE))


def build_html():
    run_cmd('python setup.py build_sphinx -s {}'.format(DOCUMENT_FOLDER))


def clean_old_build():
    run_cmd('rm -rf build/sphinx/html {} {}'.format(API_DOCUMENT_FOLDER,
                                                    HTML_DIR))


def duplicate_old_html():
    run_cmd('git clone -b gh-pages . {}'.format(HTML_DIR))
    run_cmd('rm -rf {html}/.git {html}/{br}'.format(html=HTML_DIR,
                                                    br=MASTER_BRANCH))


def get_git_tags():
    return run_cmd('git tag --contains').split()


def update_html():
    run_cmd('mv build/sphinx/html {}/{}'.format(HTML_DIR, MASTER_BRANCH))

    tags = get_git_tags()
    if tags:
        destination = tags[0].decode()
        run_cmd('rm -rf {}/{}'.format(HTML_DIR, destination))
        run_cmd('cp -r {html}/{br} {html}/{dst}'.format(html=HTML_DIR,
                                                        br=MASTER_BRANCH,
                                                        dst=destination))


def main():
    clean_old_build()
    build_docstring_rst()
    build_html()
    duplicate_old_html()
    update_html()


if __name__ == '__main__':
    main()

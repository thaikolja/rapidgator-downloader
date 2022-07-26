# Rapidgator Downloader

This command line tool lets you download files from rapidgator.net with your premium account using one line. It is meant for web servers with SSH access to use the server's internet speed capabilities. Before running, please read below.

## Requirements

Since Rapidgator Downloader is still in `v1.0.0`, some requirements have not yet been shipped. You need the following:

1. Python 3 (check with `python --version` or `python3 --version`)
2. Python module `requests` (`pip3 install requests` or `pip install requests`)

## Quick Start

### To run via Python


1. Make sure all requirements are met
2. `git clone https://gitlab.com/thaikolja/rapidgator-downloader.git`
2. `cd rapidgator-downloader`
3. Run `python3 [FILE_ID] -o 'my-file.zip'`

**Replace `[FILE_ID]` with Rapidgator's file ID. It's the long string inside the download URL; a detailed description is below.**

### Install and run globally (recommended)

1. `git clone https://gitlab.com/thaikolja/rapidgator-downloader.git`
2. `cd rapidgator-downloader`
3. 	`chmod +x rget.py`
4. `mv rget.py /usr/local/sbin/rget`
5. Restart Terminal

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

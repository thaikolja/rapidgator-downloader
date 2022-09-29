# Rapidgator Downloader

This command line tool (CLI) lets you download files from [rapidgator.net](https://rapidgator.net/account/registration/ref/4773870) with your premium account using one line. It is meant for web servers (SSH required) to **increase download speed and avoid timeouts**. Before running, please read below.

>**To avoid any misunderstandings: This tool requires an active rapidgator.net premium account. Without it, this tool is not for you.**

## 🔧 Requirements

Since Rapidgator Downloader is still in `v1.0.0`, some requirements have not yet been shipped. You need the following:

1. Python 3 (check with `python --version` or `python3 --version`)
2. Python module `requests` (`pip3 install requests` or `pip install requests`)

## 🚀 Quick Start

### To run via Python

1. Make sure all requirements are met
2. Run Terminal
2. `git clone https://gitlab.com/thaikolja/rapidgator-downloader.git` to download the tool
2. `cd rapidgator-downloader` to switch into its directory
4. Open `rget.py` and enter your username and password on line 50
5. Run `python3 [FILE_ID] -o 'my-file.zip'` to initiate the download

**Replace `[FILE_ID]` with Rapidgator's file ID. It's the long string inside the download URL; a detailed description is below.**

### Install and run globally (recommended)

1. `git clone https://gitlab.com/thaikolja/rapidgator-downloader.git`
2. `cd rapidgator-downloader`
3. 	`chmod +x rget.py`
4. `mv rget.py /usr/local/sbin/rget`
5. Restart Terminal

## 🔍 How to get file ID

The file ID is the random-looking string in the download URL, after `/file/`.

### Example

**URL:** https://rg.to/file/**1208f5f462a1f848c44cc90d7a9d12fd**/AdoPS2342.zip.html

**File ID:** `1208f5f462a1f848c44cc90d7a9d12fd` is the file ID

## 🧨 Examples

## 👨🏼‍💻 Authors
* [Kolja Nolte](https://www.kolja-nolte.com) / Contact via <kolja.nolte@gmail.com>

## ⚖️ License
This program is licensed under *GNU General Public License v3*, which grants you the right to do with it whatever you want.

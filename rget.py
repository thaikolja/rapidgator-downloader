#!/usr/bin/python3

import os
import sys
import requests
import argparse


# Defining the main function that runs all sub-functions
def main():
    # rapidgator.net ID of the file from first argument
    file_id = sys.argv[1]

    # If no file ID, just quit
    if len(sys.argv[1]) < 32:
        exit()

    parser = argparse.ArgumentParser(
        description="Automatically logs in and downloads any rapidgator.net file."
    )

    parser.add_argument(
        'file_id',
        type=str,
        help='The internal rapidgator.net file ID'
    )

    parser.add_argument(
        "--output", "-o",
        help='Output location (must be absolute path with file name)',
        required=False
    )

    parser.add_argument(
        '--username', '--user', '--email', '--mail', '-u', '-e',
        help='Username in order to build the script into an executable.',
        required=False
    )

    parser.add_argument(
        '--password', '-p', '-pw',
        help='Password in order to build the script into an executable.',
        required=False
    )

    # =========== IMPORTANT ===========
    # In order to generate the token,
    # enter your login credentials here
    # =================================
    def generate_access_token(user='XXX', password='XXX'):
        token_url = 'https://rapidgator.net/api/v2/user/login'
        token_url = token_url + '?login={}&password={}'.format(user, password)
        response = requests.get(token_url)

        if response.status_code != 200:
            exit('generate_access_token')

        response = response.json()['response']
        access_token = response['token']

        return download(access_token)

    def download(access_token):
        args = parser.parse_args()

        api_url = 'https://rapidgator.net'
        api_url = api_url + '/api/v2/file/download?file_id={}&token={}'.format(file_id, access_token)
        response = requests.get(api_url).json()

        if response['status'] != 200:
            exit()

        url = response['response']['download_url']

        os.system("wget {} -O {}".format(url, args.output))

    generate_access_token()


if __name__ == '__main__':
    main()

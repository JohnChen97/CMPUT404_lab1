import requests, sys
if __name__ == '__main__':
    sys.stdout.write(f'the requests version is {requests.__version__} \n')
    sys.stdout.write(
        f'Google homepage: {requests.get("https://www.google.com").text}')
    python_script = requests.get(
        "https://raw.githubusercontent.com/JohnChen97/CMPUT404_lab1/main/requests_version_script.py"
    )
    source_code = requests.get(
        'https://github.com/JohnChen97/CMPUT404_lab1/blob/main/requests_version_script.py'
    )
    sys.stdout.write(
        f'The source code of the python script from github is: {source_code.text}\n'
    )
    sys.stdout.write(f'Raw link: {python_script.text}\n')

    with open('python_script_github.py', 'w') as doc:
        doc.write(python_script.text)
        doc.close()

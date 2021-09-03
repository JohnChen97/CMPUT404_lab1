import requests, sys
if __name__ == '__main__':
    sys.stdout.write(f'the requests version is {requests.__version__} \n')
    sys.stdout.write(
        f'Google homepage: {requests.get("https://www.google.com").text}')
    python_script = requests.get(
        "https://raw.githubusercontent.com/JohnChen97/CMPUT404_lab1/main/requests_version_script.py"
    )
    sys.stdout.write(python_script.text)
    #sys.stdout.write(python_script.content)

    with open('python_script_github.py', 'w') as doc:
        doc.write(python_script.text)
        doc.close()

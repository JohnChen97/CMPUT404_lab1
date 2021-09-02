import requests, sys
if __name__ == '__main__':
	sys.stdout.write(f'the requests version is {requests.__version__} \n')
	sys.stdout.write(f'Google homepage: {requests.get("https://www.google.com").text}')
	

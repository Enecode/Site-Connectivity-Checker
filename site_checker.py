import urllib.request as urllib 

def main(url):
    print("Checking connectivity ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was: ", response.getcode())

print("THis is a site connectivity checker program")
input_url = input("enter your url")
main(input_url)

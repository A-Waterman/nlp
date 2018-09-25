import urllib.request

def download(filename, url):
	if Path(filename).exists() == False:
		urllib.request.urlretrieve(url, filename=filename)

def main():
    download("word2vec/ted_en-20160408.zip", 
    		 "https://wit3.fbk.eu/get.php?path=XML_releases/xml/ted_en-20160408.zip&filename=ted_en-20160408.zip")
    print("Done.")


if __name__ == '__main__':
    main()

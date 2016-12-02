build:
	docker build -t icrawler .

run: build
	docker run -ti --rm -v `pwd`/data:/root/data icrawler

bash: build
	docker run -ti --rm -v `pwd`/data:/root/data icrawler bash

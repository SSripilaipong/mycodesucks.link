deploy:
	mkdir build/src/
	pip install -r requirements.txt --target build/src
	cp -r app/ endpoint/ page/ build/src/
	cd build/src; zip -r ../app.zip .
	rm -rf build/src/
	aws lambda update-function-code --function-name mycodesucks --zip-file fileb://build/app.zip --no-cli-pager
	aws cloudfront create-invalidation --distribution-id EDFN8IY3W8GMO --paths "/*" --no-cli-pager

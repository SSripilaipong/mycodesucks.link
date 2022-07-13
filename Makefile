deploy:
	mkdir build/src/
	pip install -r requirements.txt --target build/src
	cp -r app/ api/ build/src/
	cd build/src; zip -r ../app.zip .
	rm -rf build/src/
	aws lambda update-function-code --function-name mycodesucks --zip-file fileb://build/app.zip

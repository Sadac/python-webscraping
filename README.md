# python first experience and web scraping

## setup the env
1. install python
2. install python plugin from microsfoft in vscode
3. install: `pip install pipenv` to use pipenv commands
4. create a virtual environment for python: `pipenv shell`
	this command inside the folder you want, is like npm, will create a Pipfile to handle python packages
5. inside the environment: `pipenv install pylint autopep8 --dev`
		install 2 python dependencies as dev dependencies
6. install lxml dependency: `pipenv install lxml`

### CSS selectors
To use css selector on web scraping, we need to install `pipenv cssselect`
To try out CSS selector visit https://try.jsoup.org/

### XPath
Visit https://scrapinghub.github.io/xpath-playground/ to try out XPath
`//h1` will search any <h1> tag without considering if it's nested or not. Just select all the <h1>

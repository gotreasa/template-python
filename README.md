# template-python

Get started by running:  
```sh
gh repo create github.ibm.com/GOTREASA/${repositoryName} --public --clone --template="github.ibm.com/GOTREASA/template-python"
cd ${repositoryName} 
git pull origin main
pyenv local 3.9.9
poetry install
poetry run task init
```

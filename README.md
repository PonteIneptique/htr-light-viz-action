# HTR Light Viz Action

Built with

- Mirador TextOverlay
- Mirador

**WORKS ONLY WITH ALTO !!!** 

# Set-up

## Steps

1. Give writing rights to Github actions (Cf. Settings -> Actions)
2. Set-up the Github Actions (See below)
3. Activate Github Pages on the specific branch `gh-pages` with the root folder as a target.

## Github actions

In the folder `.github/workflows/gh-page.yml`, customize the following YAML

Update the line `cd app && python build.py "../data/*" ".xml" "CREMMA Medii Aevi"`:
- The first parameter `"../data/*` should be able to list from a subfolder (the app is created in the folder app)
- The second parameter is the extension that should be recognized
- The third parameter is the name of the website

You should also activate or not chocomufin :)

```yml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Github Pages Build

on:
  push:
    branches:
      - main  # Set a branch name to trigger deployment
  pull_request:

jobs:
  build:  # Tests that the catalog is correctly written
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - uses: actions/setup-node@v3
      with:
        node-version: 16
    - name: Install python dependencies
      run: pip install lxml chocomufin
    # If you want to run ChocoMufin
    - name: Run chocomufin
      run: chocomufin -n NFD convert table.csv data/*/*.xml --parser alto
    - name: Get the application build
      run: |
        git clone --depth=1 https://github.com/PonteIneptique/htr-light-viz-action.git app
    - name: Install node dependencies
      run: cd app && npm install && npm run build && rm -rf node_modules .git
    - name: Build app
      run: cd app && python build.py "../data/*" ".mufichecker.xml" "CREMMA Medii Aevi"
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./
```
# app-config-checker

Compares two yaml files to see which keys are present in one file but absent in another. 
It does not (currently) check for differences between values.
It is designed to work only in the context of an HMRC worskspace, with app-config-dev, -qa etc.

## Requirements
* Python
* pip

## Setup
```
pip install -r requirements.txt
```
or:
```
sudo -H pip install -r requirements.txt
```

## Usage
display the help file:
```
./bin/checker.py -h
```

compare the `staging` and `production` versions of config for the `vat-core` project:
```
./bin/checker.py $WORKSPACE vat-core staging prod
```
Keys present in staging but not in prod will be shows with a '-', keys in prod but not staging will be shown with '+'

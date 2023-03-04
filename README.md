42 Mulhouse Blackhole Checker
===

Installation
---

1. create a virtual environment

```
python3 -m venv [path_to_virtual_environment]
```

2. activate virtual environment

```
source [path_to_virtual_environment]/bin/activate
```

3. install dependencies

``` 
pip install -r requirements.txt 
```
4. **put your 42api UID and SECRET in config.sample.yml**

5. rename it config.yml

```
mv config.sample.yml config.yml
```

6. place your google sercice_account.json file in the correct location

- [where to get your service account file][1]

[1]: <https://cloud.google.com/iam/docs/keys-create-delete>
```
/Users/[your_username]/.config/gspread/service_account.json
```

Running
---
- Run the program with the run.sh file
```
./run.sh
```

The program will first run blackhole.py which will call the API for the users on 42 mulhouse campus. It may take a while as a basic API key is limited to 2 requests per second.

It will generate a file with the list of logins of the users that are 30 days or less from the blackhole.

gsheet.py will then update the gsheet with these logins.

To use this program you need an application on the google cloud service, you can find more information about that on [their official documentation][2].

[2]: <https://cloud.google.com/docs/>
YA DANCER ! (Health Check Status)
====

Get a response json reflecting the current status of the site.

## Installation 

1. Install the package

```python
python setup.py
```

2. Go to `setting.py` and add `ya-dancer` to your installed app:

```python
INSTALLED_APPS = (
    'ya_dancer',
)
```

3. Go to the main `urls.py` of your project and add the following:

```python
url(r'^health-check-status/', include('ya_dancer.urls')),
```

## Basic Usage

You need to go to the `health-check-status/` relative url, you should get a JSON response like:

```python
{"app_status": "ok", "db": "ok"}
```

### Check selected items

* To check app status:

`health-check-status/app/`

response:

```python
{"app_status": "ok"}
```

* To check database status:

`health-check-status/db/`

response:

```python
{"db": "ok"}
```


### MongoDB

* To check mongodb on it's own (requires mongoengine):
`health-check-status/mongodb/`

or as part of all:
`health-check-status/?mongodb=1`

response:

```python
{"mongo_db": "ok"}
```

CHECK IT MATE !

![Ya Dancer !](http://files.stv.tv/imagebase/139/623x349/139488-ya-dancer-wacky-contestant-steven-hall-on-britains-got-talent-2011.jpg)


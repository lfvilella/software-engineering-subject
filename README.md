# software-engineering-subject

# Tech Stack

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Coverage](https://coverage.readthedocs.io/en/6.4.4/)
- [OS based on Unix](https://en.wikipedia.org/wiki/Unix) - you can run on Windows as well just replace the Unix cmds for Windows cmds.

# Setup venv

Create venv
```
$ python3 -m venv venv
```

Activate venv
```
$ source venv/bin/activate
```

Upgrade pip (optional but recommended)
```
$ pip install --upgrade pip
```

Install requirements
```
$ pip install -r src/requirements.txt
```

# Running tests

Go to `src` dir
```
$ cd src
```

Run tests
```
$ pytest
```

Run coverage
```
$ pytest --cov=.
```

# Examples

![Screen Shot 2022-08-23 at 21 15 15](https://user-images.githubusercontent.com/45940140/186288213-f3a88952-e130-41e3-8992-24d340244bdf.png)

![Screen Shot 2022-08-23 at 21 15 23](https://user-images.githubusercontent.com/45940140/186288219-7d28ceca-abd4-4090-aa45-b1dedca30499.png)

![Screen Shot 2022-08-23 at 20 08 00](https://user-images.githubusercontent.com/45940140/186288063-f8f5f369-9e95-4907-a968-78600e65e189.png)

<img width="718" alt="Screen Shot 2022-08-23 at 21 16 25" src="https://user-images.githubusercontent.com/45940140/186288243-16514e1c-8aa3-4391-9ec1-bada9f92bc03.png">

<img width="911" alt="Screen Shot 2022-08-23 at 21 16 46" src="https://user-images.githubusercontent.com/45940140/186288264-c15d22b9-f046-473d-afc1-312bbdf3dbfc.png">

<img width="910" alt="Screen Shot 2022-08-23 at 21 17 01" src="https://user-images.githubusercontent.com/45940140/186288283-cf1082b0-54d1-431d-8d4d-06359099af01.png">

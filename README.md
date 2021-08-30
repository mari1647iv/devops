[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![Docker][docker-shield]][docker-url]
[![MIT License][license-shield]][license-url]

# Moscow Time - Python Web Application

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ul>
    <li><a href="#about">About</a></li>
    <li>
      <a href="#getting_started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#docker">Docker</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#unit_tests">Unit Tests</a></li>
    <li><a href="#author">Author</a></li>
    <li><a href="#license">License</a></li>
  </ul>
</details>

## About <a name = "about"></a>

Simple Python web application, that shows current time in Moscow. The time updates with a page refreshing. This project was developed within the DevOps Engineering course in Innopolis University. The Flask framework was used to adapt the python code to web app. More about best practices used you can read in `PYTHON.md` in `app_python` folder.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. <!--See [deployment](#deployment) for notes on how to deploy the project on a live system.-->

### Prerequisites <a name = "prerequisites"></a>

Download the project using

```bash
git clone https://github.com/mari1647iv/devops.git
```

Set up the environment using setup.py:

```bash
python3 -m venv venv

source venv/bin/activate

pip install .
```

or install the requirements manually:

```bash
python3 -m venv venv

source venv/bin/activate

python3 -m pip install -r app_python/requirements.txt
```

### Installation <a name = "installation"></a>

Start the application:

```bash
cd app_python
python3 main.py
```

As a result you will get the project running on your localhost with port 5000

```bash
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 830-674-667
```

### Docker <a name = "docker"></a>

The application could be built and running using `Docker`.

Download the project using

```bash
git clone https://github.com/mari1647iv/devops.git
```

Build docker image:

```bash
cd app_python
docker build --tag mari1647iv/devops:app_python .
```

or pull it from the Docker Hub repository:

```bash
docker pull mari1647iv/devops:app_python
```

Run the docker image

```bash
docker run -p 5000:5000 mari1647iv/devops:app_python
```

To run it in detached mode use:

```bash
docker run -d -p 5000:5000 mari1647iv/devops:app_python
```

## Usage <a name = "usage"></a>

The application is running locally on port 5000. The web pages demonstrates the current time in Moscow. As the page is refreshed the time updates correspondingly.

Press `CTRL+C` in terminal to stop the application.

Do not forget to leave the virtual environment:

```bash
cd ..
deactivate
```

## Unit Tests <a name = "unit_tests"></a>

Unit tests are written in python using `unittest` framework and stored in `test_main.py` file.

To run the tests you can use the following command in the `app_python` folder:

```bash
python3 -m unittest test_main.py
```

## Author <a name = "author"></a>

**Marina Ivanova, Innopolis University BS18-SE-01**

- Github: @mari1647iv
- Email: m.ivanova@innopolis.university

Project Link: https://github.com/mari1647iv/devops

## License <a name = "license"></a>

Distributed under the MIT License. See `LICENSE.md` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/mari1647iv/devops.svg?style=for-the-badge
[contributors-url]: https://github.com/mari1647iv/devops/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mari1647iv/devops.svg?style=for-the-badge
[forks-url]: https://github.com/mari1647iv/devops/network/members
[issues-shield]: https://img.shields.io/github/issues/mari1647iv/devops.svg?style=for-the-badge
[issues-url]: https://github.com/mari1647iv/devops/issues
[docker-shield]: https://img.shields.io/docker/image-size/mari1647iv/devops?sort=date&style=for-the-badge
[docker-url]: https://hub.docker.com/r/mari1647iv/devops/
[license-shield]: https://img.shields.io/github/license/mari1647iv/devops.svg?style=for-the-badge
[license-url]: https://github.com/mari1647iv/devops/blob/main/LICENSE.md

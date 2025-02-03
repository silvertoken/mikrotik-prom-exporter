
<a id="readme-top"></a>

<p align="center">
	<a href="https://github.com/silvertoken/mikrotik-prom-exporter/graphs/contributors">
    	<img src="https://img.shields.io/github/contributors/silvertoken/mikrotik-prom-exporter.svg?style=for-the-badge" alt="Contributors">
	</a>
	<a href="https://github.com/silvertoken/mikrotik-prom-exporter/network/members">
    	<img src="https://img.shields.io/github/forks/silvertoken/mikrotik-prom-exporter.svg?style=for-the-badge" alt="Forks">
	</a>
	<a href="https://github.com/silvertoken/mikrotik-prom-exporter/stargazers">
    	<img src="https://img.shields.io/github/stars/silvertoken/mikrotik-prom-exporter.svg?style=for-the-badge" alt="Stars">
	</a>
	<a href="https://github.com/silvertoken/mikrotik-prom-exporter/pulse">
    	<img src="https://shields.io/github/commit-activity/m/silvertoken/mikrotik-prom-exporter.svg?style=for-the-badge" alt="Commits">
	</a>
	<a href="https://github.com/silvertoken/mikrotik-prom-exporter/issues">
    	<img src="https://img.shields.io/github/issues/silvertoken/mikrotik-prom-exporter.svg?style=for-the-badge" alt="Issues">
	</a>
</p>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Mikrotik Prometheus Exporter</h3>

  <p align="center">
    A python application that exposes metrics for the Mikrotik RouterOS REST API in prometheus format
    <br />
    <a href="https://github.com/silvertoken/mikrotik-prom-exporter/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/silvertoken/mikrotik-prom-exporter/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

There are few projects thatt use the built in API for the Mikrotik router to expose them to Grafana using Prometheus.  The problem with this solution is that API was built on very old methodologies and doesn't follow REST principles.  Mikrotik has released a version of RouterOS that does support REST but there are not many tools out there for it yet.  As I needed to integrate my own router into my stack I decided to go ahead and make it public.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Python][python-badge]][python-url]
* [![HTTPX][httpx-badge]][httpx-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Prometheus
* Grafana
* Python
* Docker/Podman
* Kuberenetes (k3s, k8s, etc)

### Installation

Install the module using pip

* Mikrotik-Prom-Exporter
  ```sh
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

```sh
gunicorn -b localhost:5000 mikrotik-prom-exporter:app --chdir ./mikrotik_prom_exporter/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Build Roadmap
- [ ] Build Documentation

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you would like to help with development, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/silvertoken/mikrotik-prom-exporter/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=silvertoken/mikrotik-prom-exporter" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Silvertoken - [https://github.com/silvertoken](https://github.com/silvertoken)

Project Link: [https://github.com/silvertoken/mikrotik-prom-exporter](https://github.com/silvertoken/mikrotik-prom-exporter)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[python-badge]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[httpx-badge]: https://img.shields.io/badge/HTTPX-000000?style=for-the-badge
[httpx-url]: https://www.python-httpx.org/
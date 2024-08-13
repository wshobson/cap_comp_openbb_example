# OpenBB Terminal Pro Custom Backend Integration

## Overview

This repository contains example code for integrating a custom backend with [OpenBB Terminal Pro](https://openbb.co/products/pro). It demonstrates how to create a custom widget that displays the Capital Companion Maverick Top Stocks report within the OpenBB Terminal Pro interface.

The accompanying article for this repo can be found here:

- [Elevate Your Trading: Integrating Custom Data with OpenBB Terminal Pro](https://sethhobson.com/2024/08/elevate-your-trading-integrating-custom-data-with-openbb-terminal-pro/)

## Features

- Custom backend API built with FastAPI
- Integration with OpenBB Terminal Pro's widget system
- Example of fetching and displaying external data (Capital Companion Maverick Top Stocks)
- Configurable widget layout and data structure

## Prerequisites

- Python 3.10+

## Installation

1. Clone this repository:

```bash
git clone https://github.com/wshobson/cap_comp_openbb_example.git
```

2. Create a virtual env and install the required dependencies:

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:

```bash
python main.py
```

2. The server will run on `http://localhost:5050`

3. In OpenBB Terminal Pro, add a new custom backend using the URL `http://localhost:5050`

4. The "Capital Companion Maverick Top Stocks" widget should now be available in your OpenBB Terminal Pro interface

## File Structure

- `main.py`: The FastAPI application that serves as the custom backend
- `widgets.json`: Configuration file for the custom widget

## Customization

To create your own custom widgets:

1. Modify the `widgets.json` file to define your widget's properties and data structure
2. Add new endpoints in `main.py` to serve data for your custom widgets
3. Implement your data fetching and processing logic in the new endpoints

## Acknowledgments

- [OpenBB](https://openbb.co/) for providing the Terminal Pro platform and custom backend integration feature
- [Capital Companion](https://capitalcompanion.ai/) for the Maverick Top Stocks data used in this example

## Disclaimer

This code is for educational purposes only. Always ensure you have the necessary permissions and comply with terms of service when integrating third-party data into your applications.

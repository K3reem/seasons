# Seasons API with n8n Workflow

**Industry:** API Development / Automation\
**Objective:** Provide astronomical season start dates and automate a daily countdown tweet using n8n.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [n8n Workflow](#n8n-workflow)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

Seasons API is a lightweight Flask service that calculates exact astronomical season start dates (equinoxes and solstices) for any year with Skyfield. An n8n workflow then fetches these dates each day, determines how many days remain until the next season, and tweets the countdown automatically.

## Features

- **Astronomical accuracy** powered by Skyfield.
- **RESTful endpoint** `/seasons?year=YYYY` returns season dates as JSON.
- **Automated workflow** (cron → HTTP → JS logic → Twitter).
- **Error alerts** via email if tweeting fails.

## Tech Stack

- **Python 3.9+** (Flask)
- **Skyfield** astronomy calculations
- **n8n** workflow automation
- **Render.com** deployment (free tier)

## Setup

```bash
# Clone and enter the project
git clone https://github.com/YourUsername/seasons-api.git
cd seasons-api

# Install Python requirements
pip install -r requirements.txt

# Run locally
python seasons_api.py
# The API will be available at http://localhost:5000
```

## Usage

**Request**

```http
GET /seasons?year=2025 HTTP/1.1
Host: localhost:5000
```

**Sample Response**

```json
{
  "Spring":  "2025-03-20",
  "Summer":  "2025-06-21",
  "Autumn":  "2025-09-22",
  "Winter":  "2025-12-21"
}
```

## n8n Workflow

1. **Trigger** – Daily at 19:00.
2. **HTTP Request** – Calls `/seasons`.
3. **Function** – Calculates days remaining.
4. **Twitter** – Posts the countdown.
5. **On Error** – Sends an email alert.



## Project Structure

```
seasons-api/
├── seasons_api.py      # Flask application
├── requirements.txt    # Dependencies
├── README.md           # Documentation
├── Pictures/           # Workflow & tweet screenshots
│   ├── n8n.png
│   └── tweet.jpeg
└── workflows/          # (optional) exported n8n JSON
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License © 2025 AbdulKareem Raed Abu Khadair


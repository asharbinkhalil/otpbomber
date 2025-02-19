# OTP Bomber 💣
![](https://files.catbox.moe/vkstnk.jpeg)

## Overview

Are you being disturbed by a persistent caller from a Pakistani number? With **OTP Bomber**, you can take control of the situation by overwhelming them with multiple OTP (One-Time Password) messages in under a minute.

This tool is designed to send over 100 OTPs to the specified phone number, ensuring the recipient is flooded with message notifications. **OPT Bomber** is simple to use and can be set up in just a few steps.

⚠️ **Disclaimer**: This tool is intended for educational purposes only. The misuse of this tool to harass or harm individuals is strictly prohibited. Please adhere to ethical guidelines and local laws.

---

## Features

- Send 100+ OTP messages to a specified number within a minute.
- Simple and user-friendly command-line interface.
- Lightweight and easy to install on any machine running Python.

---

## Prerequisites

To use this tool, ensure you have the following installed:

- Python 3.10 above

---

## Installation

Follow these steps to download and set up the tool:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/asharbinkhalil/otpbomer.git
   cd otpbomber
   ```

2. **Install required libraries**:
   Run the following command to install all dependencies.
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Once everything is installed, you can start using the tool with a simple command:

```bash
python3 core.py <phone-number>
```

- Replace `<phone-number>` with the target phone number (e.g., `+923001234567`).
- Ensure the phone number is in the correct format with the country code (Pakistan's country code is `+92`).

Example:
```bash
python3 core.py +923001234567
```
To test for only one site

```bash
python3 core.py +923001234567 --site priceoye
```

This will trigger the OTP Bomber and send over 100 OTPs to the specified number.

---

## Legal Disclaimer

This tool is designed for **educational purposes** only and should not be used for illegal activities. The developer is not responsible for any misuse of this tool. Please be mindful of local regulations and ethical guidelines when using such tools.

---

## Contribution

If you would like to contribute to this project, feel free to submit a pull request or open an issue in the repository. We welcome all suggestions and improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

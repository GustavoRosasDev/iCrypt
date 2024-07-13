<!-- Logo -->
<p align="center">
  <img width="150" align="center" src="src/image/logo.png">
</p>

<!-- Title -->
<h1 align="center">
  iCrypt
</h1>

<!-- Subtitle -->
<p align="center">
  Securely <b>Encrypt</b> and <b>Decrypt</b> Your Data.<br><i>One Byte at a Time!</i>
</p>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Cross-Platform-brightgreen" alt="Platform">
  <img src="https://img.shields.io/badge/Open-Source-brightgreen" alt="Source Code">
  <img src="https://img.shields.io/badge/Version-Beta-yellow" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.11-blue" alt="CustomTkinter">
  <img src="https://img.shields.io/badge/CustomTkinter-5.2.2-blue" alt="CustomTkinter">
</p>

## Introduction
<!-- Index -->
<details>
  <summary><strong>📚 Index</strong></summary>

  * [Introduction](#introduction)
  * [Note](#note)
  * [Instructions](#instructions)
  * [Get started](#get-started)
  * [How to run iCrypt?](#how-to-run-icrypt)
      * [Using CMD or PowerShell](#using-cmd-or-powershell)
      * [Using Bash](#using-bash)
  * [Contribution and Licensing](#contribution-and-licensing)
      * [Contribute](#contribute)
      * [Third-Party Software](#third-party-software)
      * [License](#license)

</details>

<!-- Overview -->
<details>
  <summary><strong>📰 Overview</strong></summary>

  **iCrypt** is a versatile encryption and decryption tool designed to enhance the privacy and security of your data. Born from the need to protect sensitive information, **iCrypt** offers a robust solution for encrypting and decrypting texts and various file types, including images, videos, and .rar files.
  
  Entirely developed in Python, iCrypt features a sleek and user-friendly Graphical User Interface (GUI) built with <a href="http://customtkinter.tomschimansky.com/">Customtkinter</a>, by <a href="https://github.com/TomSchimansky">Tom Schimansky</a>.
  
  **iCrypt** is designed to provide robust security for your data with ease of use. Its main functionalities include:
- Secure encryption and decryption of texts and files (images, videos, and .rar files)
- Implementation of symmetric encryption so that users can exchange data securely, ensuring that only those with the correct key can decrypt the information.
- Support for multiple layers of encryption in a single file, allowing users to apply several layers of security. To decrypt, simply use the symmetric keys in the correct reverse order.

With **iCrypt**, you can have full control over your data privacy, ensuring that your sensitive information remains protected at all times.

</details>

## Note
> 👉  `iCrypt (beta)` is currently under development in branch `main`.

## Instructions
<!-- Prerequisites -->
<details>
  <summary><strong>📋 Prerequisites</strong></summary>

  1. **Windows 10** or higher and **Ubuntu 22.04** or higher.
  2. [Python 3.11.4](https://www.python.org/downloads/release/python-3114/) or higher
  3. [git 2.40.1](https://git-scm.com/downloads) or higher
  4. [pip 23.1.2](https://pypi.org/project/pip/) or higher

</details>

<!-- Installing prerequisites -->
<details>
  <summary><strong>⬇️ Installing prerequisites</strong></summary>

   <h3><span style="color:#cccc">On Linux (via Bash):</span></h3>

Update system dependencies before proceeding. To do this, copy and paste the command below into your Terminal and press `enter`:
  ```
  sudo apt update
  ```

...and only then, proceed with the tutorial below:

   <!-- Installing Python -->
<details>
  <summary><strong>🐍 Installing Python</strong></summary>

  ```
  sudo apt install python3.11
  ```
</details>

   <!-- Installing Git -->
<details>
  <summary><strong>🐙 Installing git</strong></summary>
    
  ```
  sudo apt install git
  ```
</details>

   <!-- Installing pip -->
<details>
  <summary><strong>📦 Installing pip</strong></summary>
    
  ```
  sudo apt install python3.11-pip
  ```
</details>

</details>

### Get Started
To use this software, follow the steps below:

<!-- 1st - Cloning repository -->
<details>
  <summary><strong>1️⃣ Cloning this repository</strong></summary>

1. Navigate to the folder where you typically install programs or applications on your computer. Any folder you prefer.
2. Opens the Terminal. To do this, **follow any of the instructions below**:
   
    **On Windows**, there are 2 options:
      - Via **CMD** *(Command Prompt)*:
         1. In the address bar located at the top of the window, **click on the folder address field**. If it's not visible, ensure that 'Address Bar' is checked in the 'View' menu.
         2. Type `CMD` in the selected address bar and press `enter`. This opens a **CMD-type** terminal in the current folder.
      - Via **PowerShell**:
         1. In the upper address bar, click to select the folder address. If not visible, ensure 'Address Bar' is checked in the 'View' menu.
         2. Right-click on the selected address bar and choose `Open in Terminal`. This opens a **PowerShell-type** terminal in the current folder.

    **On Linux** (via Bash):<br />
   - Right-click on the folder background and select `Open in Terminal` or navigate to the project root folder using the `cd` command.

3. Next, clone this repository into the folder you chose. To do this, copy and paste the command below into your terminal and press `enter`:
  ```
  git clone https://github.com/GustavoRosasDev/iCrypt.git
  ```

Then, **navigate into the project folder**. To do this, copy and paste the command below into your terminal and press `enter`:
  ```
  cd iCrypt
  ```

> [!NOTE]
> The above command will use the git clone module to create an exact copy of this repository in your folder (local repository).

</details>

<!-- 2nd - Create Virtual environment -->
<details>
  <summary><strong>2️⃣ Create virtual environment</strong></summary>

With the Terminal still open, copy and paste the command below and press `enter`:

**On Windows**:
  ```
  python -m venv venv
  ```
**On Linux**:

Begin by installing the package below, which **provides support** for virtual environments (venv), in Python 3.11.
  ```
  sudo apt install python3.11-venv
  ```

The execution of the above command **requires elevated administrative privileges** (indicated by the use of `sudo`). Therefore, you will be prompted for the superuser (`root`) password **to ensure security** and **authorize the package installation** in Python 3.11.

Next, **create your virtual environment** by copying and pasting the code below into your Terminal:
  ```
  python3.11 -m venv venv
  ```

> [!NOTE]
> The above command utilizes the `python` interpreter (via environment variables) with the `-m` (module) parameter to create a virtual environment (`venv`) named the same as `venv`. You could name it whatever you like; however, it is a universal convention (adopted by the Python community) to name it this way.

</details>

<!-- 3rd - Activate Virtual environment -->
<details>
  <summary><strong>3️⃣ Activate virtual environment</strong></summary>

The next step is to **activate the virtual environment**. See how simple it is:

**On Windows**: <br />
1. Navigate to the `Scripts` folder:
    ```shell
    cd venv\Scripts
    ```

2. Then, **activate** the virtual environment:

    ```shell
    activate
    ```
3. And finally, return to the root folder. To do this, type the command below and press `enter`. **Repeat this twice**:

    ```shell
    cd ..
    ```
   
> [!NOTE]
> The `cd` (change directory) command, when used with `..`, allows you to navigate up one level in the directory structure. Executing this combination twice will bring you back to the main project folder, specifically the `iCrypt/` directory.


**On Linux**: <br />
  ```bash
  source venv/bin/activate
  ```

✅ To confirm that the virtual environment **has been activated** correctly , simply look at your Terminal and check if `(venv)` appears on the same line where you would type your next command.<br /><br />See an example in the image below:<br />
![Activating Virtual Environment](https://i.imgur.com/F1bd2el.png)

</details>

<!-- 4th - Install requirements -->
<details>
  <summary><strong>4️⃣ Install requirements</strong></summary>

With the virtual environment active, simply install the dependencies (libraries) that the project needs to function. To do this, copy and paste the command below into the Terminal and press `enter`:

**On Windows:**
  ```
  pip install -r requirements.txt
  ```
**On Linux:**
  ```
  pip3.11 install -r requirements.txt
  ```

> [!NOTE]
> The above command uses `pip` _(Package Installer for Python)_ to install dependencies specified in the requirements file. The `install` command is a fundamental part of pip, followed by the `-r` _(read)_ parameter, indicating that it should **read and install the requirements**. The `requirements.txt` file, located in the root folder of this project, contains a **list of necessary libraries** for the project to function.

</details>

## How to Run iCrypt

Make sure you are in the project's root folder (`iCrypt/`). Then, copy and paste the command below into the Terminal, and press `enter`:

### Using CMD or PowerShell
  ```
  python main.py
  ```

### Using Bash
  ```
  python3.11 main.py
  ```

## Contribution and Licensing
### Contribute

See [CONTRIBUTING](src/docs/CONTRIBUTING.md)

### Third-Party Software

See [ThirdPartyNotices](src/docs/THIRD-PARTY-NOTICES.md)

### License
See [LICENSE](src/docs/LICENSE.md)

<!-- SVG Typing -->
<p align="center"><br /><br />
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=4285F4&center=true&random=false&width=435&lines=Keep+Learning.+Keep+Hacking!" alt="Typing SVG">
</p><br /><br />

# Stealth Solver

An open-source tool designed to assist with technical assessments and online interviews.

---

## 🕵️‍♂️ Invisibility Compatibility

#### 👻 **100% Invisible**
Stealth Solver remains completely undetectable by all the below methods:
- **Zoom**
- **Microsoft Teams**
- **Google Meet**
- **Discord**
- **Other browser-based recording software**
- **Screen sharing of tabs, windows, or entire screen**
- **Screenshot or Screen recording**

---

## Global Commands
The application operates using mouse clicks on the **application overlay**, followed by the respective keyboard commands:
- **Toggle Window Brightness:** `Control + B`
- **Move Window:** `Control + Arrow Keys`
- **Take Screenshot:** `Control + H`
- **Get Code:** `Control + Enter`
- **Reset View:** `Control + R`
- **Quit:** `Control + Q`

---

## 🛠 Installation

### 🪟 Windows Guide (.exe)

####  Download the Application  
- Visit the [GitHub Releases](https://github.com/Anurag-Varma/StealthSolver/releases) page.  
- Download the latest version of the application (e.g., `StealthSolver.zip`).  

####  Extract Files  
- Locate the downloaded `StealthSolver.zip` file in your **Downloads** folder.  
- Extract it to a directory of your choice.  

####  Run the Application  
- Open the extracted folder and double-click `StealthSolver.exe` to launch the application.  

####  Firewall & Antivirus Configuration (Hotfix)  
- If prompted, allow the application through **Windows Firewall** to ensure smooth operation.  
- Sometimes, **Microsoft Defender or other antivirus software** may flag the application as a potential threat. If this happens:  
  - Temporarily **disable** Microsoft Defender or your antivirus.  
  - **Whitelist** `StealthSolver.exe` in your antivirus settings.  
- The application is **not a virus**, but it may be incorrectly flagged as the `.exe` is made using pyinstaller without a verfied signature.

---

### 🐍 Python Installation

#### Prerequisites

- **Python 3.9 or above** is required, can be installed from [python.org](https://www.python.org/ "python.org")
  - Verify your Python version:
    ```bash
    python --version
    ```
    or
    ```bash
    python3 --version
    ```

#### Clone the Repository

Open a terminal and clone the repository to your local machine:

```bash
git clone https://github.com/Anurag-Varma/StealthSolver.git
cd StealthSolver
```

#### Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to isolate dependencies:

   - On Windows:
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3.9 -m venv env
     source env/bin/activate
     ```

#### Install Dependencies

The repository contains a `requirements.txt` file, which lists the required Python packages. Install them using pip:

```bash
pip install -r requirements.txt
```

#### Verify Installation

Check that all dependencies are installed correctly by running any test scripts or commands provided in the repository:

```bash
python main.py
```

#### Build the Application (Optional)

If you want to build a standalone `.exe` file for the application, you can use the `pyinstaller` tool. Run the following command:

```bash
pyinstaller --onefile --noconsole --name "StealthSolver" --icon=assets/logo.ico --add-data "assets/logo128.png;assets" main.py
```

This command will create a single executable file named `StealthSolver.exe` in the `dist` directory.

By following these steps, you can set up and run the **StealthSolver** project, or optionally build a standalone `.exe` file.

---

## 💡 Usage



---

## 🤖 GPT4Free Providers

Available providers with no required authorization and with Vision(Image Upload) feature - [gpt4free](https://github.com/xtekky/gpt4free/blob/main/docs/providers-and-models.md#providers-no-auth-required "gpt4free")

| Website | API Credentials | Provider | Text Models | Image Models | Vision (Image Upload) | Stream | Status |
|----------|-------------|--------------|---------------|--------|--------|------|------|
|[blackbox.ai](https://www.blackbox.ai)|No auth required|`g4f.Provider.Blackbox`|`blackboxai, gemini-1.5-flash, gemini-1.5-pro, blackboxai-pro, llama-3.1-8b, llama-3.1-70b, llama-3-1-405b, llama-3.3-70b, mixtral-small-28b, deepseek-chat, dbrx-instruct, qwq-32b, hermes-2-dpo, deepseek-r1` _**(+34)**_|`flux`|`blackboxai, gpt-4o, gemini-1.5-pro, gemini-1.5-flash, llama-3.1-8b, llama-3.1-70b, llama-3.1-405b`|✔|![](https://img.shields.io/badge/Active-brightgreen)|
|[oi-vscode-server.onrender.com](https://oi-vscode-server.onrender.com)|No auth required|`g4f.Provider.OIVSCode`|`gpt-4o-mini`|❌|`gpt-4o-mini`|✔|![](https://img.shields.io/badge/Active-brightgreen)|
|[pollinations.ai](https://pollinations.ai)|No auth required|`g4f.Provider.PollinationsAI`|`gpt-4o-mini, gpt-4o, qwen-2.5-72b, qwen-2.5-coder-32b, llama-3.3-70b, mistral-nemo, deepseek-chat, llama-3.1-8b, deepseek-r1` _**(2+)**_|`flux, flux-pro, flux-realism, flux-cablyai, flux-anime, flux-3d, midjourney, dall-e-3, sdxl-turbo`|gpt-4o, gpt-4o-mini|✔|![](https://img.shields.io/badge/Active-brightgreen)|

---

## ❓ Need Help

If you encounter any issues, check the [Issue Tracker](https://github.com/Anurag-Varma/StealthSolver/issues)

---

## 🤝 Contribute

We welcome contributions from the community. Whether you are adding new gpt4free providers or features, or simply fixing typos and making small improvements, your input is valued.

Creating a pull request is all it takes. Once all changes have been addressed, we will merge the pull request into the main branch and release the updates at a later time.

---

## ©️ Copyright

This program is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

```bash
Anurag-Varma/StealthSolver: Copyright (C) 2024 Anurag Varma

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

---

## 📄 License

<table>
  <tr>
    <td align="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/1200px-GPLv3_Logo.svg.png" alt="GPLv3 Logo" width="80%">
    </td>
    <td>
      <img src="https://img.shields.io/badge/License-GNU_GPL_v3.0-red.svg" alt="License Badge"> <br>
      This project is licensed under 
      <a href="https://github.com/Anurag-Varma/StealthSolver/blob/main/LICENSE" target="_blank">GNU GPL v3.0</a>.
    </td>
  </tr>
</table>

---

<p align="right">(<a href="#top">🔼 Back to top</a>)</p>
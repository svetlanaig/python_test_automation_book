# Section 1: Setting Up Tools

In this section, we will set up the essential tools you need for the course. These include installing Python, setting up Git for version control, and choosing an IDE for coding. We'll also introduce BeeCrowd, a platform where you can practice coding challenges related to testing concepts. Let's ensure that you have the necessary tools installed and ready. These tools will be used throughout the course.


## References
1. [Python Downloads](https://www.python.org/downloads/)
2. [Python Documentation](https://docs.python.org/3/)
3. [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
4. [Git Documentation](https://git-scm.com/doc)
5. [GitHub](https://github.com)
6. [PyCharm Download](https://www.jetbrains.com/pycharm/download/)
7. [Visual Studio Code](https://code.visualstudio.com/)
8. [Installing Python Modules](https://docs.python.org/3/installing/index.html#basic-usage)
9. [BeeCrowd](https://www.beecrowd.com.br/)
10. [Course Repository](https://github.com/ericrommel/python_test_automation_book)

---


## 1.1 Python Installation

Python is a powerful, flexible, and popular language used widely in test automation due to its simplicity and large ecosystem of libraries. It is the language we will use for writing test scripts during this training.


### Instructions:

1. Go to the [Python official website](https://www.python.org/downloads/).
2. Download the latest version of Python for your operating system (Windows, macOS, Linux).
3. During installation, make sure to check the box **"Add Python to PATH"**.
4. Verify the installation by opening a terminal or command prompt and typing:

   ```bash
   $ python --version
   ```


## 1.2 Git Installation

Git is a version control tool that will help us manage code repositories. We will use it to track changes in our test scripts and collaborate.


### Instructions:

1. Go to the [Git official website](https://git-scm.com/downloads).
2. Download the latest version of Git for your operating system (Windows, macOS, Linux).
3. Follow the installation steps for your operating system.
4. Verify the installation by typing the following in the terminal or command prompt:

   ```bash
   $ git --version
   ```
5. Set up a [GitHub](https://github.com/) account to host your code repositories and collaborate with others.


## 1.3 GitHub Setup

GitHub is a powerful web-based platform for version control and collaboration in software development. It allows developers to collaborate on projects, track changes, and maintain a history of code development. It is widely used in the software development industry for open-source projects, team collaborations, and test automation.

### Instructions:

Assuming that you don't have an account yet:

1. Go to the [GitHub](https://github.com/) website
2. Click on `Sign up` button in the upper-right corner
3. Enter your details (email, username and password)
4. Follow the instructions to complete the setup

Once your account is ready, you can create a new repository, explore open-source projects, and even contribute to them.

For this training, we will use this [repository](https://github.com/ericrommel/python_test_automation_book). Clone it in your local machine:

1. Open a terminal window (e.g.: `cmd.exe`, `Git Bash`, `PowerShell`, etc.) inside your preferable work folder
2. Clone the repo using SSH (need setup private/public keys on Security in GitHub) or HTTPS

   ```bash
   $ git clone git@github.com:ericrommel/python_test_automation_book.git
   ```

   or

   ```bash
   $ git clone https://github.com/ericrommel/python_test_automation_book.git
   ```

3. Go to the new folder created: `python_test_automation_book`
4. Create a new branch to work with

   ```bash
   $ git checkout -b name_of_your_branch
   ```

**Note:** You can also fork the repo. A fork is a new repository that shares code and visibility settings with the original `upstream` repository. Forks are often used to iterate on ideas or changes before they are proposed back to the `upstream` repository, such as in open source projects or when a user does not have the **write access** to the `upstream` repository.

For more information, see ["Working with forks."](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks)


## 1.4 IDE Installation

An Integrated Development Environment (IDE) helps you write, manage, and debug your code efficiently. You can choose any IDE you prefer, but we recommend one of the following:


### Option 1: PyCharm

1. Download PyCharm from the [JetBrains](https://www.jetbrains.com/pycharm/download/?section=windows) website.
2. Choose the Community edition, which is free (you may need to scroll down a bit to find it).
3. Follow the installation steps.


### Option 2: Visual Studio Code (VS Code)

1. Download VS Code from the [Visual Studio Code](https://code.visualstudio.com/download) official website.
2. Follow the installation instructions for your OS.
3. Install the Python extension for better code management and debugging.


### Hands-On Task:

After installing your chosen IDE, open a new Python project and write a simple "Hello, World" script to ensure everything is working:

```python
print("Hello, World!")
```


## 1.5 Set a Virtual Environment

A virtual environment is an isolated Python environment where it will have its own Python interpreter, libraries and scripts installed. It allows you to manage dependencies for different projects separately, preventing conflicts between packages.

Follow the [Python documentation](https://docs.python.org/3/library/venv.html) for more background on Python Virtual Environments.

### Instructions

1. Create a virtual environment inside a folder

   ```bash
   $ python -m venv /path/to/new/virtual/environment
   ```

2. Activate the new virtual environment. The way to do so will depend on the terminal and OS (Windows/Linux/macOS/etc):

| Shell      | Platform | Command to activate virtual environment |
|------------|----------|-----------------------------------------|
| bash/zsh   | POSIX    | $ source <venv>/bin/activate            |
| fish       | POSIX    | $ source <venv>/bin/activate.fish       |
| csh/tcsh   | POSIX    | $ source <venv>/bin/activate.csh        |
| PowerShell | POSIX    | $ source <venv>/bin/Activate.ps1        |
| cmd.exe    | Windows  | c:\> <venv>\Scripts\activate.bat        |
| PowerShell | Windows  | PS c:\> <venv>\Scripts\Activate.ps1     |
| bash/zsh   | Windows  | $ source <venv>/bin/activate            |



### Hands-On Task:

1. Create a new virtual environment for the Week 1 class.
2. Activate the new virtual environment


## 1.5 Package Management Tools

Package management tools are essential for managing dependencies. These tools allow you to install, update, and manage external libraries or packages that your Python projects may rely on. Instead of manually downloading and maintaining libraries, you can easily pull in the required packages using a package manager, ensuring that your environment stays organized and consistent.

Some examples of package management tools:

- `pip`: Python's standard package installer. This is what we will focus on in this course. [Official documentation](https://pip.pypa.io/en/stable/)
- `pipenv`: Manages both packages and virtual environments, combining `pip` and `virtualenv` in a unified workflow. [Official documentation](https://pipenv.pypa.io/en/latest/)
- `Conda`: More commonly used in data science, `Conda` is an environment manager and package manager that works across multiple programming languages. [Official documentation](https://docs.conda.io/en/latest/)
- `Poetry`: Designed to simplify dependency management and packaging, `Poetry` is growing in popularity due to its ease of use. [Official Documentation](https://python-poetry.org/)

In this course, we will primarily use `pip`, the standard package management tool, due to its simplicity and widespread use in Python projects.


### Syntax:

```bash
$ pip install <package_name>
```


### Example:

```bash
$ pip install pytest
```


### Installing Packages

You can install specific packages that you need for your test automation projects using pip. These packages are often listed in a requirements.txt file, which is used to ensure that everyone on the team is using the same package versions.

```bash
$ pip install -r requirements.txt
```


### Updating and Uninstalling Packages

Updating:

```bash
$ pip install --upgrade <package_name>
```

Uninstalling:

```bash
$ pip uninstall <package_name>
```


### Generating the `requirements.txt`

```bash
$ pip freeze > requirements.txt
```


## 1.6 BeeCrowd Code Challenges

BeeCrowd is a platform where you can practice your coding skills through challenges. We'll use it to solve some basic algorithmic problems to strengthen your problem-solving skills.


### Instructions:

1. Go to [BeeCrowd](https://beecrowd.com/).
2. Sign up for a free account.
3. Familiarize yourself with the interface
4. Try solving one or two basic problems. Go to the `Beginner` section under `Problems` and search for challenges `1000` and `1001`.



### Hands-On Task:

Complete the challenges [`1000`](https://judge.beecrowd.com/en/problems/view/1000), [`1001`](https://judge.beecrowd.com/en/problems/view/1001), and [`1002`](https://judge.beecrowd.com/en/problems/view/1002) from the `Beginner` section.

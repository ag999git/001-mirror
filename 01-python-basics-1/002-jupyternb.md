### Table of contents

- [1.2 PART 1: Installing Anaconda (which includes Jupyter Notebook)](#12-part-1-installing-anaconda-which-includes-Jupyter-Notebook)
- [1.3 PART 2: Launching Jupyter Notebook (After Installation)](#13-part-2-launching-jupyter-notebook-after-installation))
- [1.4 PART 3: OPTIONAL — Installing Jupyter Notebook Without Anaconda](#14-part-3-optional-installing-jupyter-notebook-without-anaconda)
- [1.5 PART 4: Setting Up a Virtual Environment for Jupyter](#15-part-4-setting-up-a-virtual-environment-for-jupyter)
- [1.6 PART 5: Verifying Everything Works](#16-part-5-verifying-everything-works)
- [1.7 Some more details of the local server when you launch Jupyter](#17-some-more-details-of-the-local-server-when-you-launch-jupyter)
- [1.8 You can think of Jupyter Notebook as having two main screens:](#18-you-can-think-of-jupyter-notebook-as-having-two-main-screens)
- [1.9 UI](#19-ui)
- [2 Some additional information](#2-some-additional-information)
- [3 Advanced concepts](#3-advanced-concepts)
- [Advanced:- Profiling Jupyter Notebooks (For Beginners)](#profiling-jupyter-notebooks-for-beginners)

 

### 1 Anaconda 

#### 1.1 Introduction

##### 1.1.1  The Client–Server Model of Jupyter Notebook

Even though Anaconda and Jupyter Notebook run on your local computer, they still follow a client–server architecture internally.

That means:

•  Server = Python backend running on your computer

•  Client = Your web browser (Chrome/Edge/Firefox)

So you are still using your computer as:- Both the client AND the server

###### 1. Server: Jupyter Notebook Server

When you run:

`jupyter notebook`

or click “Launch” in Anaconda Navigator:

→ A small Python program called the Jupyter Notebook Server starts running in the background.

This server:

  -  Runs on your machine

  -  Manages files and notebooks

  -  Executes Python code

  -  Provides web pages for the interface

  -  Communicates with the browser using WebSockets

The server usually runs at:

`http://localhost:8888`

localhost means:

  - Your own computer is acting as a server.

###### 2. Client: Your Web Browser

The Jupyter interface you see is just a website that your local server provides.

The browser:

  - Displays notebooks

  - Sends your code to the server

  - Receives output (text, images, errors)

  - Updates the notebook content

So the browser acts as a client UI.

1.1.2 Behind-the-Scenes: How Code Execution Works

•  Step-by-step internal process: 

  1.  You type Python code in a cell in your browser.

  2.  Browser sends the cell code to the Jupyter server.

  3.  The server sends the code to a kernel (usually IPython).

  4.  The kernel executes the code.

  5.  The result (text/plots/errors) is sent back to the server.

  6.  The server sends the result to your browser.

  7.  Browser displays the output in the notebook.

This process happens in milliseconds.

##### 1.1.3 What Is the Kernel (Internally)?

A kernel is a separate background process that executes code.

For Python notebooks, it is the IPython kernel:

•  Runs your Python code

•  Maintains variable state

•  Stores memory

•  Handles errors

•  Generates outputs

Even if the browser is closed, the kernel may keep running until stopped.

##### 1.1.4 Client–Server Role of Anaconda

Anaconda itself is not a client–server app, but:

It launches applications that use the model

It manages environments and packages that these apps need

  -  Internally, Anaconda Navigator:

  -  Runs as a local desktop GUI application

  -  Acts as a launcher for tools

  -  Starts Jupyter Notebook server when asked

  -  Manages Python environments

Think of it like a control panel, not a server.

##### 1.1.5 How Everything Fits Together

✔ When you start Jupyter from Anaconda:

1.  Anaconda starts the Jupyter Notebook Server

2.  The server listens on a port on your machine

    - Example: `localhost:8888`

3.  Your browser opens the interface

4.  The browser sends code → server → kernel

5.  Kernel executes code and returns results

6.  Browser displays the output

1.1.6 Why use a client–server model locally?

Even though everything is on your computer, this model gives benefits:

  -  Benefit 1: Browser-based interface:- You don’t need a separate desktop app.

  -  Benefit 2: Remote execution:- Same model works on remote servers (e.g., Google Colab, JupyterHub, cloud).

  -  Benefit 3: Allows multiple clients:- Multiple browser tabs can talk to the same kernel.

  -  Benefit 4: Language independence:- Kernel can be Python, R, Julia, etc., while browser stays the same.

[Back to the Table of Contents](#table-of-contents)
#### 1.2 PART 1: Installing Anaconda (which includes Jupyter Notebook)

[Back to the Table of Contents](#table-of-contents)

Anaconda is the easiest and recommended way for beginners to use Python and Jupyter Notebook.

##### 1.2.1 STEP 1 — Go to the Anaconda Website

  1.  Open your web browser (Chrome, Edge, Firefox).
  2.  Go to: `https://www.anaconda.com/download`

##### 1.2.2 STEP 2 — Download the Windows Installer

  1.  Scroll to “Download Anaconda Distribution”.

  2.  Choose:

   - Operating System: Windows

   - Python Version: Choose `Python 3.x` (default is fine)
  3.  Click Download 64-bit Installer.

A file called something like:

`Anaconda3-2024.XX-Windows-x86_64.exe`

will start downloading.



> [!IMPORTANT]
> You should download Anaconda — not Miniconda by mistake. (Unless you specifically want to)
> The miniconda installer looks something like:- `Miniconda3-latest-Windows-x86_64.exe`.
> Dont install it because it is the minimal installer (no Jupyter, no packages, very small).
> The Anaconda website is confusing because it advertises Miniconda first.
> If you are unable to locate the link for Anaconda, you may use:- https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Windows-x86_64.exe.
> This is the full Anaconda Distribution, NOT Miniconda.

The Anaconda distribution contains:-
✔ Contains Jupyter Notebook
✔ Contains JupyterLab
✔ Contains Spyder
✔ Contains NumPy, Pandas, Matplotlib, etc.
✔ Big installer (~800 MB)

##### 1.2.3 STEP 3 — Run the Installer

###### 1.  Locate the downloaded .exe file (usually in Downloads).

###### 2.  Double-click it to start the installation.

##### 1.2.4 STEP 4 — Initial Installer Screens

Click Next → Accept the license → Next.

##### 1.2.5 STEP 5 — Installation Type

Choose:

  -  Just Me (recommended. Unless you know how admin installation works.)

  -  Click Next.

1.2.6 STEP 6 — Choose Install Location

Leave it default:

`C:\Users\<yourname>\Anaconda3`

  -  Click Next.

**IMPORTANT STEP: PATH Checkbox**

You will see two checkboxes:

✔ Add Anaconda to my PATH environment variable (NOT recommended—leave unchecked)

> [!NOTE]
> Why is adding Anaconda to PATH not recommended?
> When you add Anaconda to the PATH, you are telling Windows: “Use Anaconda’s Python everywhere in the system.”
> It Overrides Your System Python.
> Many computers already have:-
> (a) Python installed by Windows Store.
> (b) Python installed by Microsoft tools.
> (c) Python installed manually.
> (d) Python used by other programs.
> If Anaconda is placed in PATH:-
> (1) It becomes the default Python for your entire system.
> (2) Other programs that expect the system Python may break.
> (3) It becomes confusing which Python you are running

✔ However if you do not have any previous version of Python installed on your system, then you may **Add Anaconda to my PATH environment variable**

✔ Register Anaconda as my default Python → Check this one

Click Install.

##### 1.2.7 STEP 7 — Wait for Installation

This may take 5–10 minutes.

##### 1.2.8 STEP 8 — Finish

Click `Next → Next → Finish`.

You're done installing Anaconda!

#### 1.3 PART 2: Launching Jupyter Notebook (After Installation)

There are two easy methods.

##### 1.3.1 METHOD 1: Use Start Menu

1.  Press `Start`.

2.  Search `Anaconda Navigator`.

3.  Open it.

4.  On the home screen, click `Launch` under Jupyter Notebook.

✔ This opens Jupyter Notebook in your browser.

##### 1.3.2 METHOD 2: Use Anaconda Prompt

1.  Open Start → search Anaconda Prompt → open it.

2.  Type:

`jupyter notebook`

Press Enter.

✔ Jupyter Notebook will open in your browser.

1.3.3 You Now Have Jupyter Notebook Installed!

#### 1.4 PART 3: OPTIONAL Installing Jupyter Notebook Without Anaconda

If you already have Python installed, you can install Jupyter with pip.

##### 1.4.1 STEP 1 — Check Python Installation

Open Command Prompt:-

`python --version`

If Python is installed, continue.

1.4.2 STEP 2 — Install pip (if not already installed)

Usually pip comes with Python. Check:

`pip --version`

##### 1.4.3 STEP 3 — Install Jupyter Notebook

Run:

`pip install notebook`

##### 1.4.4 STEP 4 — Launch Notebook

jupyter notebook

#### 1.5 PART 4: Setting Up a Virtual Environment for Jupyter

(Optional but recommended)

##### 1.5.1 STEP 1 — Create Environment

`python -m venv myenv`

Note:- In above `myenv` is the name of your virtual environment.

> [!TIP]
> You can name your virtual environment anything you like.
> However by convention, many a times it is named `.venv` . This is because in many operating systems (Like Linux and macOS) files and folders starting with a dot are conventionally hidden from default directory listings.
> This is done to protect important system or configuration files.
> However on Windows, a specific "hidden" attribute must be set.

##### 1.5.2 STEP 2 — Activate Environment

Windows:

`myenv\Scripts\activate`

##### 1.5.3 STEP 3 — Install Jupyter Inside This Environment

`pip install notebook`

##### 1.5.4 STEP 4 — Launch Jupyter

`jupyter notebook`

#### 1.6 PART 5: Verifying Everything Works

In Jupyter:

1.  Click New → Python 3 (ipykernel).

2.  In the first cell, type:

`print("Hello Jupyter!")`

3.  Press `Shift + Enter`.

If it prints the message, your setup is perfect.

#### 1.7 Some more details of the local server when you launch Jupyter

[Back to the Table of Contents](#table-of-contents)

When you start Jupyter Notebook, it automatically launches a local web server on your computer.

The link you see —

`http://localhost:8888/tree`

— is the address (URL) of that local server.

Here’s what each part means, in simple terms:

##### 1.7.1 `http://`

This means you are using the HTTP protocol, the same protocol used for regular websites.

##### 1.7.2 `localhost`

This means:

•  The server is running on your own computer, not on the internet.

•  `localhost` always refers to your own machine.

•  It is the hostname for IP address `127.0.0.1` (loopback address).

So opening localhost is like telling your browser:

"Connect to a server running on my own computer."

##### 1.7.3 `:8888 (Port Number)`

Computers can run many servers at the same time, each identified by a port.

Port `8888` means:

  -  Jupyter Notebook server is listening for connections on port 8888.

  -  If another service is already using 8888, Jupyter uses 8889, 8890, etc.

So:

`localhost:8888`

means:

“Connect to the server on my computer at port 8888.”

##### 1.7.4 `/tree`

This is the route or endpoint that displays the file browser view.

This view is called the Tree View because:

  -  Your files are shown like a branching folder tree. The Jupyter interface you see (list of folders/files) is called the Tree View.

  -  You can navigate up and down directories

  -  You can open, delete, rename, or create new notebooks

So /tree loads:

The main home screen where you pick notebooks to open.

If you open a notebook, URL changes, for example:

  -  `/notebooks/MyNotebook.ipynb`

  -  `/edit/somefile.py`

  -  `/terminals/1`

  -  `tree` = File Browser View

It refers to the directory tree — the list of folders and files on your computer, displayed in a hierarchical (tree-like) structure.

##### 1.7.5 Putting it all together

`http://localhost:8888/tree` means:

“Open the Jupyter Notebook server that is running on my own computer (localhost), using port 8888, and display the tree (file browser) interface.”

This is why everything runs locally — no internet needed.

##### 1.7.6 How the flow works

1.  You start Jupyter Notebook.

2.  It starts a Python-based server on your computer.

3.  That server listens on localhost:8888.

4.  Your browser opens the Jupyter UI at /tree.

5.  You interact with notebooks via your browser.

6.  The browser communicates with the Jupyter server.

7.  The server communicates with the Python kernel.

#### 1.8 You can think of Jupyter Notebook as having two main screens:

[Back to the Table of Contents](#table-of-contents)

##### 1.8.1 Screen 1: The Tree View (Home Page)

URL: http://localhost:8888/tree

This is the first screen you see when Jupyter starts.

It functions like a file manager.

Here you can:

  -  Browse your folders

  -  See files and subfolders

  -  Create new notebooks

  -  Open existing notebooks

  -  Upload files

  -  Open terminals

It’s similar to a “home page” or “dashboard.”

##### 1.8.2 Screen 2: The Notebook Editor (When a notebook opens)

URL example:

http://localhost:8888/notebooks/myfile.ipynb

This is the actual interactive coding environment where you write Python code in cells.

Screen shot of the UI of Screen 2 is given below (Note that the UI elements may vary from one system to anothet depending upon the installation/ version)




In this screen, you get:

  -  Menu bar

  -  Code cells

  -  Markdown cells

  -  Output area

  -  Kernel controls

This is where you run code.

  

  
#### Menu Bar
Details of each button on the Menu bar are given below.
Also given are the various options for each button on the menu bar, in form of a table.
  - The first column of each table gives the options one gets when he clicks on that menu button. 
  - The second column of each table shows the function/ role of each option.

**1 File Menu**

Used for creating, saving, downloading, and managing notebooks.

**Important options**

| Option | What it Does |
| --- | --- |
| New Notebook | Creates a new .ipynb file with a selected kernel (Python 3 etc.). |
| Open… | Opens files/folders from the Jupyter file browser. |
| Make a Copy | Creates a duplicate of the current notebook. Useful for backups. |
| Save / Save and Checkpoint | Saves your notebook manually (Jupyter also auto-saves). Checkpoints let you restore old versions. |
| Rename | Renames your notebook file. |
| Download as | Download notebook in various formats (HTML, PDF, Python script, Markdown). |
| Close and Halt | Shut down the notebook kernel and close the file. |

  

  

  

**2 Edit Menu**

Used for editing cells (cut/copy/paste) and managing cell content.

**Important options**

| Option | What it Does |
| --- | --- |
| Cut / Copy / Paste Cells | Manage entire cells, not lines of text. |
| Delete Cells | Removes the selected cell. |
| Undo Delete Cell | Restore deleted cells. |
| Split Cell / Merge Cells | Break a cell into two or join multiple into one. |
| Find and Replace | Search and replace text inside the notebook. |

  

**3 View Menu**

Controls visibility of interface elements.

**Important options**

| Option | What it Does |
| --- | --- |
| Toggle Toolbar | Shows/hides the row of icons under the menu bar. |
| Toggle Header | Shows/hides the top title bar. |
| Cell Toolbar | Enables special toolbars such as "Tags", "Slideshow", "Edit Metadata". |

  

**4 Insert Menu**

Used to add new cells.

| Option | What it Does |
| --- | --- |
| Insert Cell Above | Adds a new cell on top of the selected one. |
| Insert Cell Below | Adds a new cell below the selected one. |

 

**5 Cell Menu**

Used to run and manage code/Markdown cells.

**Important options**

| Option | What it Does |
| --- | --- |
| Run Cells | Executes selected cell. |
| Run Cells and Select Below | Runs current cell and moves cursor down. |
| Run All / Run All Above / Run All Below | Executes multiple cells at once. |
| Cell Type → Code / Markdown / Raw | Change the type of cell. |
| Current Outputs → Clear | Deletes cell outputs. |
| All Output → Clear | Clears outputs for entire notebook. |

  

**6 Kernel Menu**

  

Controls Python execution backend.

**Important options**

| Option | What it Does |
| --- | --- |
| Interrupt | Stops code that is currently running (like Ctrl+C). |
| Restart | Restarts Python kernel → all variables cleared. |
| Restart & Run All | Restarts kernel and runs all cells from the beginning. |
| Change Kernel | Switch Python environments (e.g., Python 3.10 → Python 3.12). |

  

**7 Widget Menu (if ipywidgets is installed)**

Used to manage interactive widgets.

**Important options**

| Option | What it Does |
| --- | --- |
| Save Notebook Widget State | Save the current state of widgets (like sliders, dropdowns). |
| Clear Notebook Widget State | Clear previous widget state. |

 

  

**8 Help Menu**

Provides documentation, shortcuts, and references.

**Important options**

| Option | What it Does |
| --- | --- |
| User Interface Tour | Shows a guided tour of the UI. |
| Keyboard Shortcuts | Displays all Jupyter shortcuts (very useful). |
| Markdown | Opens Markdown syntax guide. |
| Python Reference | Links to Python documentation. |




#### Jupyter Notebook Toolbar 

(Buttons/ Icons below the Menu Bar)



![UI of Screen 2 of Jupyter Notebook](https://github.com/ag999git/python-book-2026/blob/main/all-book-images/Screen-shot-UI-2-Jupyter-notebook-menu-bar-and-others.jpg)

##### The above screen shot shows the Jupyter Notebook Toolbar as placed on the UI

![Screenshot of Jupyter Notebook Toolbar](https://github.com/ag999git/python-book-2026/blob/main/all-book-images/2-Screen-shot-UI-2-Jupyter-notebook-tool-bar-and-others.jpg)


##### The above screen shot shows the various tools on the Jupyter Notebook Toolbar

##### Each of these individual tools on the Jupyter Notebook Toolbar are discussed below:-

1 Save (💾 icon)

**What it does:** Saves the notebook (.ipynb file).  
**Shortcut:** Ctrl + S  
This ensures your latest code, outputs, and text are stored.

2 Add New Cell (➕ icon)

**What it does:** Inserts a **new empty cell below** the current cell.  
Useful when adding more code or notes.

3 Cut Cell (✂️ icon)

**What it does:** Removes the selected cell and stores it in clipboard.  
You can paste it later.

4 Copy Cell (📄📄 icon)

**What it does:** Copies the selected cell to clipboard.

5 Paste Cell (📄 icon)

**What it does:** Pastes a previously cut/copied cell **below** the current cell.

6 Move Cell Up (⬆️ icon)

**What it does:** Moves the selected cell **one position up**.

7 Move Cell Down (⬇️ icon)

**What it does:** Moves the selected cell **one position down**.

8 Run Cell (▶️ Run)

**What it does:**

*   Executes the current cell
*   Shows output directly below it
*   Moves to the next cell

**Shortcut:** Shift + Enter

9 Stop Execution (■ icon)

**What it does:**  
Interrupts/Stops the current running cell.  
Useful if your code is stuck in an **infinite loop**.

10 Restart Kernel (🔄 icon)

**What it does:**  
Restarts the Python kernel → clears memory (all variables reset).  
Notebook stays open, but all outputs become stale.

11 Restart & Run All (⏩ icon)

**What it does:**

1.  Restarts kernel
2.  Runs **every cell in order from top to bottom**

Useful for making sure your notebook runs cleanly from scratch.

12 Cell Type Dropdown (Code / Markdown / Raw)

Shows the type of the current cell.  
You can switch it to:

*   **Code** → Python code
*   **Markdown** → Text, headings, notes
*   **Raw** → Unprocessed text

13 Keyboard Shortcuts (⌨️ icon)

Opens a list of **all shortcuts** in Jupyter Notebook.  
Very helpful for speeding up work.




#### Relationship between the 2 screens of the Jupyter Notebook UI






##### 1.8.3 Relationship Between the Two Screens

•  The tree view is like a launcher.

•  The notebook editor is the actual work screen.

You always begin at Screen 1, unless you directly launch a notebook from the command line.

##### 1.8.4 Simplified Visual Explanation

```python
Start Jupyter
↓
Tree View (file browser)
↓ (open a file)
Notebook Editor (where you code)
```

#### 1.9 UI

[Back to the Table of Contents](#table-of-contents)

1.9.1 Screen 1 — Tree View (the Jupyter home / file browser)

URL example: http://localhost:8888/tree

This is the first page Jupyter opens. It behaves like a simple file manager for the folder where you launched Jupyter.

Given below is the screen shot of Screen 1 with the “New” button clicked. It is from here that you select the various options to get the next screen. In most cases, you want to start a new Jupyter notebook, for which you may click the “Python 3 (ipykernel)”. But you may click other options as per your need.

##### 1.9.2 UI of screen 1

![UI of 1st screen when you run Jupyter Server](https://github.com/ag999git/python-book-2026/blob/main/all-book-images/UI-Screen1-Jupyter-NB.jpg)


The sreen shot shows the options available when one clicks the `New` Button. (The options may vary from one machine to another)
1. `.venv` is a virtual environment
2. `Java` is another kernel (of Java) installed
3. `Python 3 (ipykernel)` is the default system Python Kernel.
4. `Text File` creates a new blank `.txt` file.
5. `Folder` creates a new folder in the current directory.
6. `Terminal` opens a command-line terminal in your browser.

`.venv`

  -  This is a virtual environment you created inside your project folder named .venv.

  -  Jupyter detects it and shows it as a kernel.

  -  If you select it, notebook cells will run using the Python interpreter inside .venv.

Useful when you want isolated packages for one project.

`Java`

  -  This means you have a Java kernel installed (e.g., via IJava).

  -  You can write and run Java code inside a notebook.

Example cell:
```java
System.out.println("Hello from Java!");
```
`Python 3 (ipykernel)`

  -  This is the default Python kernel that comes bundled with Jupyter.

  -  It uses your system-wide Python installation (not inside a venv).

  -  This is the most common option for general use.

`Text File`

  -  Creates a new blank .txt file.

  -  Opens a simple text editor in the browser.

  -  Useful for notes, config files, or documentation.

`Folder`

  -  Creates a new folder in the current directory.

  -  Helps you organize project files.

`Terminal`

-  Opens a Linux-like command-line terminal in your browser.

-  Lets you run:

  -  pip install

  -  git commands

  -  virtual environment activation

  -  python scripts

  -  bash commands

This is very powerful and often used for managing environments.

##### 1.9.3 Parts of various toolbars/ panels in the UI

###### 1 Header / Top Bar

  -  Title — shows “Files” or the notebook server name.

  -  Logo / Brand — small Jupyter logo and sometimes server info.

  -  Useful for: Orienting you; no actions here typically.

###### 2 Toolbar (near top of page)

Common buttons you’ll see:

-  New → menu to create:

  -  New Python 3 notebook (or other kernels)

  -  New text file

  -  New folder

  -  New terminal (opens a shell tab)

- Upload → upload files from your computer into the current folder

-  Refresh → re-scan the directory (useful when files were added externally)

-  Control / Shutdown (may appear in other views)

Tip: Use New → Notebook to quickly create a .ipynb ready to run.

###### 3 File / Folder list (the “tree”)

-  Shows all files and folders in the current directory.

-  Each row usually shows:

  -  Filename (click to open)

  -  Last modified time

  -  File size (sometimes)

-  Right-click / three-dot menu on a file offers:

  -  Open, Rename, Duplicate, Download, Delete, Move, Edit, View

  -  For notebooks you may also see “Shutdown” (stops its kernel)

Tip: Clicking a folder enters it; clicking a notebook opens the editor (screen 2).

###### 4 Breadcrumb / Current path

•  Shows which folder you are viewing.

•  Click parents to go up one level.

###### 5 Running / Sessions (sometimes a tab or menu)

•  Running or Active sessions shows kernels/notebooks currently active.

•  From here you can shut down notebooks (stop their kernels) to free resources.

Why important: Closing a browser tab does not automatically stop the kernel — use this to shutdown.

###### 6 Search / Filter (if available)

•  Lets you find filenames in the current directory.

###### 7 Footer / Server info

•  May display the URL, token, or server messages.

•  Shows the directory that is being served (where files are stored).

##### 1.9.4 Screen 2 — Notebook Editor (the interactive coding screen)

URL example: http://localhost:8888/notebooks/myfile.ipynb

This is where you write and run code and see outputs.

###### 1 Browser URL & Notebook Name

•  The web page title usually contains the notebook name (myfile.ipynb).

•  Click the notebook name at top to rename it.

###### 2 Menu Bar (top row)

Typical menus (Already discussed earlier):

•  `File` — New, Open, Make a copy, Rename, Save and Checkpoint, Download as (HTML, .py, .ipynb), Close and Halt

•  `Edit` — Cut/Copy/Paste cells, Find & Replace

•  `View` — Toggle toolbar/menu/line numbers

•  `Insert` — Insert cell above/below

•  `Cell` — Run Cells, Run All, Cell Type (Code / Markdown)

•  `Kernel` — Interrupt / Restart / Reconnect / Change kernel

•  `Help` — Keyboard shortcuts, docs, kernel info

Tip: File → Save and Checkpoint creates a backup checkpoint. Browser autosaves periodically.

###### 3 Notebook Toolbar (icons under menu)
Already discussed earlier

Common buttons (left→right):

•  `Save` (floppy icon)

• ` Add cell, Cut/Copy/Paste cell, Move cell up/down`

•  `Run cell (▶) and Run all`

•  I`nterrupt kernel (stop), Restart kernel (⟳)`

###### 4 Kernel Status (top right)

•  Shows whether the kernel is Idle, Busy, or Disconnected.

•  Often a small circle: filled = busy, empty = idle.

•  Important actions:

  -  Interrupt — stop a running cell (like Ctrl+C)

  - Restart — clear memory and restart Python kernel

Tip: If state is “Busy” and your code is stuck, click Interrupt or Restart.

###### 5 Cells — the basic building blocks

•  Two main cell types:

  - Code cells — contain executable Python code

  - Markdown cells — for formatted text, headings, lists, images

•  Each cell has its own run button (▶ on the left) and an execution number like In [1].

•  Outputs (below a code cell) show printed text, tables, plots, or errors.

•  Cell toolbar and actions:

•  Add new cell (above / below)

•  Change cell type (Code / Markdown)

•  Delete cell

•  Move cell up/down

###### 6 Command Mode vs Edit Mode (keyboard behavior)

•  Edit mode (green border): typing inside a cell (press Enter to go into it).

•  Command mode (blue border): notebook-level commands (press Esc to enter).

•  Useful shortcuts:

  - Esc → Command mode

  -  Enter → Edit mode

  - A (in Command) → Insert cell above

  - B (in Command) → Insert cell below

  - M → change to Markdown

  - Y → change to Code

  - D, D (press D twice) → delete cell

  - Shift+Enter → run cell and advance

  - Ctrl+Enter → run cell, do not advance

  - Alt+Enter → run cell and insert new cell below

  - H → show all keyboard shortcuts

###### 7 Output Area

•  Renders results: text prints, images/plots (matplotlib), HTML, DataFrames, etc.

•  Rich outputs are supported (interactive widgets, JavaScript).

Tip: If many outputs make notebook slow, Clear Output from Cell menu.

###### 8 Sidebar / Additional Panels (depends on interface)

•  File browser can reappear (JupyterLab has persistent sidebars; classic notebook may not).

•  Variable inspector / extensions may add panels (if installed).

###### 9 Status / Messages (bottom or header)

•  Kernel connection errors, long-running warnings, or autosave messages appear here.

###### 10 Checkpoints and Saving

•  Jupyter autosaves, but you can make a manual Checkpoint (File → Save and Checkpoint).

•  You can Download as .ipynb (or export to HTML/PDF).

#### 1.10 Extra
[Back to the Table of Contents](#table-of-contents)

#### 1.11 FAQ Frequently Asked Beginner Questions
[Back to the Table of Contents](#table-of-contents)

##### 1.11.1 Do I need Anaconda to run Jupyter Notebook?

No, but it makes life easier.

##### 1.11.2 Will Jupyter run offline?

Yes.

##### 1.11.3 Is Anaconda free?

Yes, 100% free for personal and educational use.

##### 1.11.4 Does Jupyter Notebook save files?

Yes. Files are saved as .ipynb.

##### 1.11.5 Can I uninstall Anaconda and keep Python?

Yes — both are separate.



### 2 Some additional information

#### 2.1 Magic commands

Magic commands in Jupyter Notebook are special commands that start with % or %% and are not part of standard Python, but are added by IPython to make your workflow easier.

They help you manage the notebook, run system commands, measure performance, load files, debug, profile code, and more — all without leaving Jupyter.

Magic commands are like shortcuts or superpowers inside Jupyter.

They help you perform tasks such as:

✔ Checking your directory

✔ Timing your code

✔ Loading external scripts

✔ Running OS commands

✔ Controlling the Jupyter environment

✔ Displaying plots

✔ Debugging

✔ Saving variables across notebooks

They come in two types.

##### 2.1.1 Line Magics (start with %)

These run on a single line.

Example:-

`%pwd  # print working directory`

`%ls  # list files`

##### 2.1.2 Common Line magic commands in tabular form

  
  

  

| Name | Format | What It Does | Simple Example |
| --- | --- | --- | --- |
| %pwd | %pwd | Shows current working directory | %pwd |
| %ls | %ls | Lists files in the current directory | %ls |
| %cd | %cd foldername | Changes directory | %cd data |
| %who | %who | Lists defined variables in workspace | %who |
| %whos | %whos | Shows variables with details (type, size, etc.) | %whos |
| %reset | %reset | Clears all variables from workspace | %reset -f |
| %run | %run script.py | Runs a Python script inside the notebook | %run myfile.py |
| %time | %time statement | Measures execution time of a single statement | %time x = sum(range(100000)) |
| %timeit | %timeit statement | Runs the statement multiple times to give accurate timing | %timeit x = sum(range(100000)) |
| %matplotlib inline | %matplotlib inline | Displays plots inside notebook | %matplotlib inline |
| %store | %store varname | Saves a variable for use in another notebook/session | %store x |
| %history | %history | Shows command history | %history |
| %pip | %pip install package | Installs Python packages directly from notebook | %pip install numpy |
| %conda | %conda install package | Installs packages using conda from notebook | %conda install pandas |

##### 2.1.3 Cell Magics (start with %%)

These apply to the whole cell.

Example:

`%%time`

 entire cell is timed

```python

x = 0
for i in range(1000000):
    x += i
```

##### 2.1.4 Common Cell magic commands in tabular form

  

| Name | Format | What It Does | Simple Example |
| --- | --- | --- | --- |
| %%time | %%time | Measures execution time of the entire cell | %%timex = [i*i for i in range(100000)] |
| %%timeit | %%timeit | Runs full cell many times & averages the timing | %%timeitx = [i*i for i in range(100000)] |
| %%bash | %%bash | Runs the entire cell as Bash shell commands | %%bashecho "Hello"\nls |
| %%python | %%python | Forces execution using Python interpreter (useful in multi-kernel setups) | %%pythonprint("Hello") |
| %%html | %%html | Renders HTML content in output | %%html<h1>Hello</h1> |
| %%markdown | %%markdown | Renders Markdown as formatted output | %%markdown\n# Title |
| %%writefile | %%writefile filename.py | Writes the content of the cell to a file | %%writefile test.py\nprint("Hello") |
| %%capture | %%capture varname | Captures output (stdout, stderr) into a variable | %%capture outprint("Hidden") |
| %%latex | %%latex | Renders LaTeX math | %%latexE=mc^2 |
| %%javascript | %%javascript | Runs JavaScript inside notebook | %%javascriptalert("Hi!") |

### 3 Advanced concepts

[Back to the Table of Contents](#table-of-contents)

#### 3.1 Flowchart

![FlowChart](https://github.com/ag999git/python-book-2026/blob/main/all-book-images/Ch-1-Jupyter-NB-Flow-chart-from-browser-to-server.jpg)


##### 3.1.1 Explanation

###### A — Anaconda Navigator

Block: A[Anaconda Navigator]

This is the graphical launcher that comes with Anaconda.

You click an icon → Navigator opens → you see apps like Jupyter Notebook, Spyder, VS Code, etc.

Meaning:- The entire workflow starts when you launch Jupyter Notebook from Anaconda Navigator.

###### A → B — Starting the Notebook Server

Block: B[Starts Jupyter Notebook Server]

When you click “Launch” → Navigator runs the command:

jupyter-notebook

This starts something called the Jupyter Notebook Server.

The server is a Python program running locally on your computer.

###### B → C — Jupyter Server Running on Localhost

Block: C[Jupyter Server Running on Localhost]

The Jupyter server starts on something like:

http://localhost:8888

“localhost” means your own computer.

This server manages:

•  Notebook files

•  Saving

•  Communication with kernels

•  Security tokens

•  Sessions

###### C → D — Browser Opens Notebook Interface

Block: D[Browser Opens Notebook Interface]

After the server starts, your web browser opens automatically.

This web page is the Jupyter Dashboard (list of notebooks) and later the Notebook Editor.

Even though it looks like a website, the entire thing runs on your computer, not on the internet.

###### D → E — User Writes Code

Block: E[User Writes Code in Cell]

Inside the browser, you type:
```python
a = 10

a + 20
```

This is just text until you run the cell.

###### E → F — Browser Sends Code to Server

Block:

F[Browser Sends Code to Server]

When you press Shift+Enter, the browser sends your code to the Jupyter server using HTTP/WebSocket.

The server receives something like:

"Run cell with code: a + 20"

###### F → G — Server Sends Code to Kernel

Block:

G[Server Sends Code to Kernel]

The Jupyter server forwards the code to a kernel.

The kernel is a Python process running separately:

python.exe -m ipykernel

This is what actually executes your code.

###### G → H — Kernel Executes the Code

Block: H[Kernel Executes Python Code]

The kernel:

•  parses your Python

•  executes it

•  maintains variable states

•  stores your session memory

###### H → I — Python Produces Output

Block:

I[Python Produces Output]

This is simply the result of your code:

30

or a graph, or a printed message.

10. I → J — Kernel Sends Output to Server

Block:

J[Kernel Sends Output to Server]

After executing the code, the kernel returns:

•  the output

•  any errors

•  stdout (print)

•  rich outputs (plots, HTML, images)

It sends this back in a structured JSON message.

###### J → K — Server Sends Output to Browser

Block:

K[Server Sends Output to Browser]

The Jupyter server receives the kernel's JSON output and forwards it to your browser.

###### K → L — Browser Displays Output

Block:

L[Browser Displays Output in Notebook]

The browser renders the output below your code cell.

This completes the cycle:

1.  You write code

2.  It travels through server → kernel

3.  Kernel executes

4.  Result travels back

5.  Browser displays it

#### 3.2 Where does Jupyter Store Kernels

Common paths:

•  Linux / Mac:

`~/.local/share/jupyter/kernels/`

•  Windows:

`C:\Users\<username>\AppData\Roaming\jupyter\kernels\`

Each kernel has a folder with:

•  kernel.json

•  an icon

•  the executable path

3.3 SSS

3.4 CCC

3.5 qqq


---

### Profiling Jupyter Notebooks (For Beginners)

[Back to the Table of Contents](#table-of-contents)

 - Jupyter notebooks allow profiling code easily using built-in tools
   and external profilers.
   
 - This guide explains the simplest and most
   useful ways to profile notebook cells.

---

#### 1. Using the `%time` and `%timeit` Magic Commands

##### Measure execution time of a **single run**:
```python
%time my_function()
```

##### Measure execution time with **multiple iterations**:
```python
%timeit my_function()
```

`%timeit` automatically picks the best number of repetitions for accuracy.

---

#### 2. Cell-level Timing with `%%time` and `%%timeit`

##### Time an entire Jupyter cell:
```python
%%time
result = []
for i in range(10000):
    result.append(i*2)
```

##### Benchmark a full cell:
```python
%%timeit
sum([i*2 for i in range(10000)])
```

---

#### 3. Using the Built-In Profiler: `%prun`

This runs the **cProfile** profiler on an expression.

```python
%prun my_function()
```

Output shows:
- number of calls  
- total time  
- time per call  
- which functions take the longest  

---

#### 4. Profiling an Entire Cell: `%%prun`

```python
%%prun
data = []
for i in range(500000):
    data.append(i*i)
```

Useful when profiling loops or multi-line code.

---

#### 5. Line-by-line profiling using `line_profiler`

##### Install:
```bash
pip install line_profiler
```

##### Load the Jupyter extension:
```python
%load_ext line_profiler
```

##### Profile a function line-by-line:
```python
%lprun -f my_function my_function()
```

---

#### 6. Memory profiling using `memory_profiler`

##### Install:
```bash
pip install memory_profiler
```

##### Load extension:
```python
%load_ext memory_profiler
```

##### Profile line-by-line memory usage:
```python
%mprun -f my_function my_function()
```

---

#### 7. Visual Profiling Inside Jupyter Using SnakeViz

`SnakeViz` creates an interactive graph of cProfile results.

##### Install:
```bash
pip install snakeviz
```

##### Generate `.prof` file:
```python
!python -m cProfile -o output.prof your_notebook_script.py
```

##### View results:
```bash
!snakeviz output.prof
```

This opens a browser tab with a flame graph–like visualization.

---

#### 8. Using Pyinstrument Inside Jupyter

Pyinstrument provides beautiful HTML output.

##### Install:
```bash
pip install pyinstrument
```

##### Run inside notebook:
```python
from pyinstrument import Profiler

prof = Profiler()
prof.start()

# your code here
my_function()

prof.stop()
prof.display()
```

---

#### 9. Using Scalene Inside Jupyter

Scalene gives CPU + memory + GPU profiling.

##### Install:
```bash
pip install scalene
```

##### Run scalene on notebook cell using Jupyter magic:
```python
%%scalene
my_function()
```

(Requires installing Scalene’s notebook extension.)

---

[Back to the Table of Contents](#table-of-contents)

#### 10. Tips for Profiling Notebooks Effectively

### a. Restart the kernel before profiling  
Ensures accurate results and clears cached variables.

### b. Profile only the function you want to optimize  
Profiling entire notebooks gives too much noise.

### c. Use `%timeit` for small operations  
Faster and more precise.

### d. Use line_profiler for loops and numerical code  
Shows the real bottleneck line.

### e. Use memory_profiler when dealing with large datasets  
Especially useful for Pandas, NumPy, lists, images, etc.

### f. Use Pyinstrument or SnakeViz for visualization  
Easier to interpret profiling output.

---

#### 11. Quick Reference Table

| Task | Best Tool |
|------|-----------|
| Timing a single line | `%time` |
| Microbenchmarking | `%timeit` |
| CPU profiling | `%prun` |
| Line-by-line CPU profiling | `%lprun` |
| Line-by-line memory profiling | `%mprun` |
| CPU + Memory + GPU profiling | Scalene |
| Visual interactive profiling | SnakeViz / Pyinstrument |

---

#### Summary

Jupyter notebooks support many profiling tools.  
Beginners should start with:

- `%time`
- `%timeit`
- `%prun`

Intermediate users should use:

- line_profiler  
- memory_profiler  
- SnakeViz  
- Pyinstrument  
- Scalene  

These tools help identify slow code, memory issues, and performance bottlenecks directly inside a notebook.

[Back to the Table of Contents](#table-of-contents)

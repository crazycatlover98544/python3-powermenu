# python3-powermenu
_python3-powermenu_ is a simple python3 script for powering off, restarting, or suspending your computer.

## Dependencies
|Dependencies|Website|
| ----------- | --- |
|python3 >= 3.6|[https://www.python.org](https://www.python.org)|
|python3-tk|[https://www.python.org](https://www.python.org)|
|systemd >= v203|[https://systemd.io/](https://systemd.io/)|
|Azure-ttk-theme|[https://github.com/rdbende/Azure-ttk-theme](https://github.com/rdbende/Azure-ttk-theme)|

For instance, the command to install these dependencies (except azure-ttk-theme) using the APT package manager would be:
`sudo apt install python3 python3-tk systemd`

For azure-ttk-theme, you can download it at [https://github.com/rdbende/Azure-ttk-theme](https://github.com/rdbende/Azure-ttk-theme). This script expects azure.tcl and the corresponding theme folder placed either in the current working directory, or in a custom directory, by passing --theme (eg. `powermenu.py --theme /home/user/.local/azure.tcl`). If this is not the case, the program will show an error and exit.

Please note: As stated by the developer of _azure-ttk-theme_, any versions prior to 2.0 are licensed under the LGPL v2.1 as opposed to the MIT license.

A version of this theme is included in the [Releases](https://github.com/crazycatlover98544/python3-powermenu/releases) section, where it is included in the zip file.

## Arguments
There are three possible arguments, and they are formatted as follows:
|Argument|What it Does|
| --- | --- |
|`--theme [theme`|Specify a theme that is located in a nonstandard directory; has to be a tcl file|
|`--light`|Change the theme of the program to light mode|
|`--dark`|Redundant, change the theme of the program to dark mode|

_If a theme style (`--light`, `--dark`) is not passed, the program will default to dark mode._

## Screenshot
![Screenshot of python3-powermenu script](powermenu_screenshot.png)

## License
This program is licensed under the MIT license. To view this license, open up LICENSE or go to the following URL: [https://opensource.org/license/mit](https://opensource.org/license/mit)

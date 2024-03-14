The main file is "model.py". 
It takes in an image as the input, and returns a prediction on whether the image
has the Golden Proportion in it, or not.

The Interactive Content will have to be opened separately since neither .py
files, nor .bat files can be used as a href in HTML.

Please run "model_exec.bat", if the OS is Windows, and "model.py" on the terminal
if the OS is either Linux, or MacOS.

Please ignore all warnings. We tried to supress them using 
"warnings.filterwarnings("ignore")," but it did not work.
Please see the last line for the predictions on the image(s).

We tried to use Flask for this purpose, but kept running into errors while 
executing. Extensive searching on forums like StackOverflow and GitHub Issues
did not help too.

We also tried to delete the image after predictions with "os.remove()" 
so that a fresh image can be predicted each time, but we repeatedly got errors 
saying "PermissionDenied" and couldn't solve it despite checking it up on 
different forums. This will, however work on Linux and MacOS systems. 
So, the first image prediction will give a single result, while 
a second prediction without deleting the image from the first prediction, will 
return two predictions.

"model.py" is executed by running "model_exec.bat", which opens a new Command
Prompt window and executes "model.py". If the OS is anything other that of Windows,
"model_exe.bat" will not run, since it only executes it on CMD or Power Shell 
and "model.py" has to be executed manually. Or, "wine" has to be installed along 
with CMD to execute the batch file on Linux and MacOS systems.

There is a "requirements.txt" file, that specifies the required Python libraries to
run the Interactive Content.

The first prediction may take about 1 minute to execute, but 
subsequent batches get predicted faster.

For more information, please refer to the .pptx file provided

import matplotlib

print("-----------------------------------------------")
# Recommended Matplotlib version:
matplotlib_version = "3.8.2"
print("Current version of matplotlib: ", matplotlib.__version__)
if matplotlib.__version__ != matplotlib_version:
    print("Attention, it is recommended to use version {} of Matplotlib.".format(matplotlib_version))
    print("We recommend updating the installation from Anaconda Prompt with:")
    print("\t \tpip install matplotlib --upgrade")
    print("or")
    print("\t \tpip install matplotlib=={}".format(matplotlib_version))
else:
    print("You are using the recommended version for Matplotlib.")
print("-----------------------------------------------")

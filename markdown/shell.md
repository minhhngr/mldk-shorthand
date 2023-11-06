# Command-line tools (CLI)

## Batch

## Bash

```sh
 set +e # Sets error ignoring state also known as `set +o errexit``
 set -e # Sets an non-ignoring error state also known as `set -o errexit``
 set +o errexit # the shell will continue executing commands even if they fail
 set -o errexit # The shell will exit immediately if any command exits with a non-zero status 

 # This is the default behavior for bash, and can be useful in certain situations where you want to ignore errors and continue with the script.
 # It's important to note that the behavior of 'set -e' can be modified by using the '||' operator to catch specific errors and handle them differently.
```

```sh
 # View process
 top
 top -c
 top -a MEM
```

```sh
 ln -s $source $destination

 # Examples: link.txt will point to file.txt, and you can access the content of file.txt by using link.txt
 ln -s file.txt link.txt
```

```sh
 xattr

 # Extended attributes are metadata associated with files that can store additional information beyond what is typically stored in a file's contents and standard metadata (e.g., file permissions, timestamps). Extended attributes are used for various purposes, including tagging files, marking them as quarantined, and storing other file-specific information.

 xattr -l $filename # List Extended Attributes:
 xattr -w $attribute_name $attribute_value $filename # Add an Extended Attribute
 xattr -d $attribute_name $filename # Remove an Extended Attribute:
 xattr -c $filename # Remove All Extended Attributes:
 xattr -p $attribute_name $source_file -w $attribute_name $destination_file  # Copy Extended Attributes from One File to Another:
```

### macOS

```sh
 ditto -h
 # The ditto command in macOS is used for copying files and directories while preserving resource forks and metadata. 
 # It can be considered as an enhanced and versatile version of the cp command, as it handles resource forks and metadata more effectively.

 ditto [options] $source $destination
 ditto -rsrc $source $destination # -rsrc to preserve resource forks, and -c for preserving metadata.
```

```sh
 hdiutil 

 # is a command-line utility in macOS that allows you to create, manipulate, and manage disk images. Disk images are files that contain the complete structure and contents of a storage device, such as a hard drive, CD, or DVD. macOS uses disk images for various purposes, including software distribution, data backup, and system recovery.

 hdiutil create -size size -fs filesystem -volname volume_name -type type -srcfolder source_folder -format format -layout layout output_filename # Create a Disk Image
 hdiutil attach filename # Mount a Disk Image
 hdiutil detach device_identifier # Unmount a Disk Image
 hdiutil convert source_image -format destination_format -o output_image # Convert a Disk Image
 hdiutil verify filename # Verify a Disk Image
 hdiutil burn image_file # Burn a Disk Image

 # '> /dev/null' This part of the command redirects the standard output (stdout) to /dev/null, effectively silencing any output or messages that would be displayed when unmounting the volume. It's a common technique to suppress output when you don't want to see the unmounting details in the terminal.
```

```sh
osascript -e '
 tell application "Terminal"
  activate
  set size of window 0 to {1280, 124}
  set frontWindow to window 0
  delay 1
  set position of window 0 to {0, 900}
 end tell
'

```

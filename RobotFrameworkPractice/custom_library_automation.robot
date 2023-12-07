*** Settings ***
Library      ReadWriteFiles.py     ${file_path}
Library      OperatingSystem


*** Variables ***
${file_path}       E:\\Filesdata\\BI14\\count_name_copied.txt
${dest_file_path}       E:\\Filesdata\\BI11\\count_name_copied.txt


*** Test Cases ***
Read file content and show output
      ${file_data}=      read_file
      Log to console      ${file_data}
      Log       ${file_data}

copy file from source to target
      Copy File       ${file_path}      ${dest_file_path}





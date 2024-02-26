File Monitoring and Transfer Utility
This Python script monitors a source directory for new files, copies them to a destination directory, and then deletes the copied files from the source directory.

Description
The script continuously checks the source directory for new files. When a new file is detected, it is copied to the destination directory. Once copied, the script deletes the file from the source directory.

Dependencies
Python 3.x
tqdm library (for progress bar)
Installation
Ensure you have Python 3.x installed on your system.
Install the tqdm library using pip:
pip install tqdm
Usage
Update the kaynak_dizin (source directory) and hedef_dizin (destination directory) variables with the appropriate paths.
Run the script:
python file_control.py
The script will continuously monitor the source directory for new files and transfer them to the destination directory.
Configuration
kaynak_dizin: Replace this with the path to your source directory.
hedef_dizin: Replace this with the path to your destination directory.
You can adjust the sleep time (time.sleep(3600)) according to your requirements. Currently, it's set to 1 hour (3600 seconds).
Important Notes
Make sure to provide appropriate permissions for the source and destination directories.
Be cautious when deleting files from the source directory. Ensure that you have appropriate backups if needed.
License
This project is licensed under the MIT License.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


Python ile yazılmış ve tqdm kullanılarak yapılan bu uygulamada kaynak dizinde var olan dosyaları kontrol eder ve eksik olan dosyaları hedef dizine gönderir. Ardından kopyalanan dosyaları siler.

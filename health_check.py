import shutil
import psutil
import socket
import emails
import os,sys

def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    return not cpu_usage>80

def disk_space_check():
    disk_usage = shutil.disk_usage("/")
    disk_free = disk_usage.free
    disk_used = disk_usage.used
    disk_total= disk_usage.total
    available = (disk_free/disk_total)*100
    return available>20

def memory_available_check():
    memory_stat = psutil.virtual_memory()
    memory_available = memory_stat.available
    memory_in_mb = memory_available/1024 **2
    return memory_available > 500


def local_host_check():
    local_ip = socket.gethostname('localhost')
    return local_ip == "127.0.0.1"

def email_error_check(error):
    sender = automation@example.com
    receipient = "{}@example.com".format(os.environ["USER"])
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receipient, subject, body)
    emails.send_email(message)


if not cpu_check():
    subject = "Error - CPU usage is over 80%"
    email_error_check(subject)

if not disk_space_check():
    subject = "Error - Available disk space is less than 20%"
    email_error_check(subject)

if not memory_available_check():
    subject = "Error - Available memory is less than 500MB"
    email_error_check(subject)

if not local_host_check():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    email_error_check(subject)





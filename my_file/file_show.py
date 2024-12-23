import os
import csv

def write_file(file_path, data):
    username,password = data
    if os.path.exists(file_path):
        with open(file_path, 'a', encoding = 'UTF-8') as file:
            file.write(f'{username},{password}\n')

def load_file(file_path):
    users = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                username,password = line.strip().split(',')
                users.append((username,password))
    return users

def load_file_csv(file_path):
    if os.path.exists(file_path):
        with open(file_path, newline='',encoding='UTF-8') as Csvfile:
            lines = csv.reader(Csvfile, delimiter=';')
            data = list(lines)
        return data
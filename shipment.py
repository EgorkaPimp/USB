import os


def send_file_to_device(file_path, ep_out, ep_in):
    with open(file_path, 'rb') as f:
        data = f.read(4096)
        while data:
            ep_out.write(data)
            data = f.read(4096)

            # Ждать подтверждения от устройства
            response = ep_in.read(64)
            print("Response from device:", response)


# Передача всех файлов из папки
def send_folder_to_device(folder_path, ep_out, ep_in):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            send_file_to_device(file_path, ep_out, ep_in)


# Пример использования
send_folder_to_device('/path/to/your/folder', ep_out, ep_in)
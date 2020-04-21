import docker
from time import sleep

print("This is my file to demonstrate best practices.")

def docker_client_version():
    client = docker.APIClient(base_url='tcp://127.0.0.1:2375/')
    version = client.version()
    print version
   
def container_jb():
    client = docker.from_env()
    jb = client.containers.get('jb')
    print jb.attrs['Config']['Image']
    
def container_logs():
    client = docker.from_env()
    jb = client.containers.get('jb')
    logs = jb.logs()
    print logs
    
def container_list():
    client = docker.from_env()
    container_list = client.containers.list()
    
    print container_list
    
def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    docker_client_version()
    container_jb()
    container_list()
    container_logs()
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
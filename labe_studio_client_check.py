from label_studio_sdk import Client


def test():
    # Connect to the Label Studio API and check the connection
    ls = Client(url='http://172.16.0.110:8080', api_key='0ecf79f5796567f7a0fe1dac43db62cbeb76f248')
    ls.create_project(name='fs')
    print(ls.check_connection())


if __name__ == '__main__':
    test()

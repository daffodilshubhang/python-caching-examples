from rejson import Client, Path


def make_connection():
    rj = Client(host="localhost", port=6379, decode_responses=True)
    obj = {
        'answer': 42,
        'arr': [None, True, 3.14],
        'truth': {
            'coord': 'out there'
        }
    }

    rj.jsonset('obj', Path.rootPath(), obj)
    # Get something
    print('Is there anybody... {}?'.format(
        rj.jsonget('obj', Path('.truth.coord'))
    ))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_connection()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

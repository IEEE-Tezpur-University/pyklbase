from db.orm import PyklBase


def main():
    print('Program Start')
    col = PyklBase("TestCol")
    uuid = col.create_by_uuid(data={
        'name': 'Adittya',
        'email': 'adittya@velocity.in'
    })
    print('Created', uuid)
    data = col.find_by_uuid(uuid)
    print(data)

main()
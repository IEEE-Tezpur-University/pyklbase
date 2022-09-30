from multiprocessing import Process
import time
from pickle_db import add_to_db, remove_from_db, get_from_db, initialise_db
from constants import db_name


def sub_process():
    initialise_db(db_name)
    initialise_db(db_name)
    print("Fetching Lastest Performance Data...")


def main():
    print("Controller Algorithm Running...")
    # while True:
    #     best_fog = get_best_fog()
    #     print(best_fog)
    #     clinical_data = {
    #         "spo2":97,
    #         "temp":37.5
    #     }
    #     send_data_to_fog(best_fog,clinical_data)
    #     time.sleep(5)


if __name__ == "__main__":
    p1 = Process(target=main)
    p1.start()
    p2 = Process(target=sub_process)
    p2.start()
    p1.join()
    p2.join()

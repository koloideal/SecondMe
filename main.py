from events.client_events import client
import logging
import os


if __name__ == '__main__':

    os.makedirs('secret_data', exist_ok=True)

    try:

        print("\n\033[1m\033[30m\033[44m {} \033[0m".format("Starting userbot..."))

        logging.basicConfig(level=logging.WARNING,
                            filename='secret_data/logs.txt',
                            filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s\n\n\n')

        logging.warning("Start userbot...")

        with client.start():

            client.run_until_disconnected()

    except Exception as e:

        logging.error(e)

        print("\n\033[1m\033[30m\033[45m {} \033[0m".format("End of work with error..."))

        logging.warning('End of work with error...')

        exit()

    else:

        print("\n\033[1m\033[30m\033[45m {} \033[0m".format("End of work..."))

        logging.warning('End of work...')

        exit()

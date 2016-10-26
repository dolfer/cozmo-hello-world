import sys
import cozmo

def run(sdk_conn):
    robot = sdk_conn.wait_for_robot()
    robot.say_text("Hello World!").wait_for_completed()
    robot.say_text("Soon you will be mine.").wait_for_completed()


if __name__ == '__main__':
    cozmo.setup_basic_logging()

    try:
        cozmo.connect(run)
    except cozmo.ConnectionError as e:
        sys.exit("A connection error occurred: %s" % e)

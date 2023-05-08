from flask import Flask
from sched import scheduler
from flask_apscheduler import APScheduler
from DatabaseLayer.Queries import database_functionality
from Logger.logger_creator import create_logger as log
from decouple import config
from Logger.Alligner import Alligner

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
formatter = Alligner()




scheduler.start()

# ------ JOBS ------ #
@scheduler.task("interval",  minutes=int(config("processor_time_interval_minutes")), max_instances=int(config("processor_max_instance")))
def job_1(job_name="GET - MERGE - PERSIST MULEAPPLICATION-INSTANCES"):
    log().info(formatter.format("STARTING JOB: {}".format(job_name)))
    try:
        id, data = database_functionality.get_oldest_not_processed_batch()
        names_of_muleapps = database_functionality.get_names_of_all_muleapps()
        prepared_batch = database_functionality.prepare_batch(id, data, names_of_muleapps)
        database_functionality.persist_instance(id, prepared_batch)
        database_functionality.update_row(id)
    except TypeError as error:
        log().error("NO BATCHES AVAILABLE")
    except Exception as error:
        database_functionality.update_row(id, error)
        log().error("FOLLOWING ERROR OCCURRED WHEN TRYING TO PROCESS BATCH WITH ID {}: {}".format(id, error))
    finally:
        log().info(formatter.format("ENDING JOB: {}".format(job_name)))
       
       
       



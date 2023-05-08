from flask import Flask
from sched import scheduler
from flask_apscheduler import APScheduler
from Logger.Alligner import Alligner
from decouple import config
from LogicLayer.APIHandler import anypoint_api_calls, misc
from DatabaseLayer.populater import populate
from Logger.logger_creator import create_logger as log


app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
formatter = Alligner()


        
# Start scheduler
scheduler.start()

@scheduler.task("interval", minutes=int(config('ingestion_time_interval_minutes')), max_instances=int(config('ingestion_max_instance')))
def job_1(job_name = "GET - TRANSFORM - PERSIST ANYPOINT-PAYLOAD"):
    log().info(formatter.format("STARTING JOB: {}".format(job_name)))
    try:
        access_token = anypoint_api_calls.get_access_token(config('client_id'), config('client_secret')).response
        organization_id = anypoint_api_calls.get_organization_id(access_token).response
        suborganizations = anypoint_api_calls.get_suborganizations(organization_id, access_token).response
        list_of_names_and_ids = misc.get_name_and_id_from_elements(suborganizations)
        complete_list = misc.add_main_organization_id(list_of_names_and_ids, organization_id)
        environments = anypoint_api_calls.get_environments_by_organization_id(complete_list, access_token).response
        applications = anypoint_api_calls.get_applications_by_ids(environments, access_token).response
        transformed_apps = misc.get_relevant_data_from_applications(applications)
        return populate(transformed_apps)
    except Exception:
        raise
    finally:
        log().info(formatter.format("ENDING JOB: {}".format(job_name)))
    
    
    
    
            
    
        
        
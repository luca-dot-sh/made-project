from pipeline import pipeline,WEATHER_DATA_SQL_TABLE_NAME,BICYCLE_THEFT_SQL_TABLE_NAME
from os import path,mkdir,chdir
import shutil
from sqlalchemy import create_engine


TEST_ENV_FOLDER = "test_environment"
DATA_ROOT = "data"

def run_tests():
    system_level_test()

def system_level_test():
    setup_test_env()
    pipeline()
    assert_sql_db_is_created()

def assert_sql_db_is_created():
    assert(path.exists(path.join(DATA_ROOT,"bt_and_weather.sqlite")))
    engine = create_engine('sqlite:///data/bt_and_weather.sqlite')
    assert(WEATHER_DATA_SQL_TABLE_NAME in engine.table_names())
    assert(BICYCLE_THEFT_SQL_TABLE_NAME in engine.table_names())

def setup_test_env():
    if(path.exists(TEST_ENV_FOLDER)):
        shutil.rmtree(TEST_ENV_FOLDER)
    mkdir(TEST_ENV_FOLDER)
    chdir(TEST_ENV_FOLDER)
    mkdir(DATA_ROOT)

if __name__=="__main__":
    run_tests()
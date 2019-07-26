"""
CREATE DATABASE IF NOT EXISTS cqn default charset utf8mb4 COLLATE utf8mb4_bin;
use cqn;
create table  unqualified_sampling
(
	id int auto_increment not null primary key,
	title varchar(32) null,
	publish_time datetime null,
	info_sources varchar(32) null,
	company_name varchar(64) null,
	company_address varchar(128) null,
	sampled_unit varchar(64) null,
	sampled_address varchar(128) null,
	sample_name varchar(128) null,
	specification_type varchar(64) null,
	trademark varchar(64) null,
	production_date varchar(32) null,
	factory_num varchar(32) null,
	approval_num varchar(32) null,
	unqualified varchar(128) null,
	test_value varchar(128) null,
	standard varchar(128) null,
	sampling_unit varchar(128) null,
	inspection_institution varchar(128) null,
	source_url varchar(256) null
)
comment 'unqualified_sampling';

"""
import time

import pymysql

from ChinaQualityNews.settings import DB_SETTINGS


def init_db():
    connection = pymysql.connect(
        host=DB_SETTINGS.get('host'),
        port=DB_SETTINGS.get('port'),
        user=DB_SETTINGS.get('user'),
        password=DB_SETTINGS.get('password'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "CREATE DATABASE IF NOT EXISTS {} default charset utf8mb4 COLLATE utf8mb4_bin;"\
                .format(DB_SETTINGS.get('db'))
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()
    time.sleep(3)
    connection = pymysql.connect(
        host=DB_SETTINGS.get('host'),
        port=DB_SETTINGS.get('port'),
        user=DB_SETTINGS.get('user'),
        db=DB_SETTINGS.get('db'),
        password=DB_SETTINGS.get('password'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = """create table  unqualified_sampling(
                        id int auto_increment not null primary key,
                        title varchar(32) null,
                        publish_time datetime null,
                        info_sources varchar(32) null,
                        company_name varchar(64) null,
                        company_address varchar(128) null,
                        sampled_unit varchar(64) null,
                        sampled_address varchar(128) null,
                        sample_name varchar(128) null,
                        specification_type varchar(64) null,
                        trademark varchar(64) null,
                        production_date varchar(32) null,
                        factory_num varchar(32) null,
                        approval_num varchar(32) null,
                        unqualified varchar(128) null,
                        test_value varchar(128) null,
                        standard varchar(128) null,
                        sampling_unit varchar(128) null,
                        inspection_institution varchar(128) null,
                        source_url varchar(256) null
                    )
                    comment 'unqualified_sampling';
                    """
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()
    print("Init DataBase And Tables Success!!!")


if __name__ == '__main__':
    init_db()

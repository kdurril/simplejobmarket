-- Internal Job Market
-- postgresql version
CREATE Schema If Not Exists jobmarket;
DROP TABLE IF EXISTS jobmarket.students CASCADE;
DROP TABLE IF EXISTS jobmarket.supervisors CASCADE;
DROP TABLE IF EXISTS jobmarket.positions CASCADE;
DROP TABLE IF EXISTS jobmarket.positionApps CASCADE;
DROP TABLE IF EXISTS jobmarket.offers;

CREATE TABLE jobmarket.roles(
role_id Serial PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE jobmarket.users(
user_id TEXT PRIMARY KEY,
username TEXT NOT NULL UNIQUE,
passwordhash TEXT,
role_id INTEGER,
CONSTRAINT FKrole FOREIGN KEY (role_id) REFERENCES jobmarket.roles,
);

CREATE TABLE jobmarket.students(
student_uid TEXT PRIMARY KEY,
name_last TEXT NOT NULL,
name_first TEXT NOT NULL,
email TEXT NOT NULL,
phone TEXT,
major TEXT,
program_code TEXT,
sem_begin TEXT,
graduation_expected TEXT,
credit_fall INTEGER NOT NULL,
credit_spring INTEGER NOT NULL,
request_fall BOOLEAN NOT NULL,
request_spring BOOLEAN NOT NULL
);

CREATE TABLE jobmarket.supervisors(
supervisor_id TEXT PRIMARY KEY,
name_last TEXT NOT NULL,
name_first TEXT NOT NULL,
phone TEXT,
email TEXT NOT NULL,
room TEXT,
center TEXT
);

CREATE TABLE jobmarket.positions(
position_id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
work_group TEXT,
position_type TEXT NOT NULL,
course TEXT,
program_min TEXT,
program_std TEXT,
position_overview TEXT NOT NULL,
primary_duties TEXT NOT NULL,
necessary_skill TEXT,
preferred_skill TEXT,
date_open Date,
date_closed Date,
available INTEGER NOT NULL,
supervisor_id TEXT,
CONSTRAINT FKsupervisor FOREIGN KEY (supervisor_id) REFERENCES jobmarket.supervisors,
CHECK (positions.available >= 0)
);

CREATE TABLE jobmarket.positionApps(
app_id SERIAL PRIMARY KEY,
position_id INTEGER, 
student_uid TEXT,
CONSTRAINT FKpostion FOREIGN KEY (position_id) REFERENCES jobmarket.positions,
CONSTRAINT FKstudent FOREIGN KEY (student_uid) REFERENCES jobmarket.students,
CONSTRAINT CHK_student_position UNIQUE (position_id, student_uid)
);

CREATE TABLE jobmarket.offers(
app_id INTEGER,
offer_made Text, 
offer_date timestamp default current_date, 
response TEXT,
response_date timestamp default current_timestamp,
available TEXT,
CONSTRAINT FKpositionApp FOREIGN KEY (app_id) REFERENCES jobmarket.positionApps,
CONSTRAINT CHK_offer_response UNIQUE (app_id, response)
);

CREATE FUNCTION position_avail_to_apply() RETURNS trigger AS $position_avail_to_apply$
    BEGIN    
        -- check position is available
        IF NEW.position_id IN (SELECT position_id FROM jobmarket.positions
                               WHERE positions.available >= 1) THEN
                RETURN NEW;  
        ELSE
            RAISE EXCEPTION 'Position not available';
        
        END IF;
     
    END;
$position_avail_to_apply$ LANGUAGE plpgsql;

CREATE TRIGGER position_avail_to_apply BEFORE INSERT ON  jobmarket.positionapps
    FOR EACH ROW EXECUTE PROCEDURE position_avail_to_apply();


CREATE FUNCTION app_avail_to_offer() RETURNS trigger AS $app_avail_to_offer$
    BEGIN    
        -- check that new values 
        IF NEW.app_id IN (SELECT positionapps.app_id FROM jobmarket.positions
            INNER JOIN jobmarket.positionapps ON 
            positions.position_id = positionapps.position_id
            WHERE positions.available >= 1) THEN
                RETURN NEW;
                
        ELSE
            RAISE EXCEPTION 'Position not available';
        
        END IF;

        NEW.offer_date := current_date;
        
    END;
$app_avail_to_offer$ LANGUAGE plpgsql;

CREATE TRIGGER app_avail_to_offer BEFORE INSERT ON  jobmarket.offers
    FOR EACH ROW EXECUTE PROCEDURE app_avail_to_offer();

CREATE FUNCTION app_response() RETURNS trigger AS $app_response$
    BEGIN
        -- after update to reponse, decrement available if yes
        IF NEW.response IS NULL THEN
            RAISE EXCEPTION 'Must indicate a yes or no response';
        END IF;

        IF NEW.response  = 'yes' THEN
                UPDATE jobmarket.positions 
                    SET available = available - 1
                    WHERE position_id = 
                        (SELECT positionapps.position_id FROM jobmarket.offers INNER JOIN 
                        jobmarket.positionapps ON offers.app_id = positionapps.app_id
                        WHERE offers.app_id = NEW.app_id);
                RETURN NEW;
        END IF;

        NEW.response_date := current_date;
        RETURN NEW;

    END;
$app_response$ LANGUAGE plpgsql;

CREATE TRIGGER app_response AFTER UPDATE on jobmarket.offers
    FOR EACH ROW EXECUTE PROCEDURE app_response();

-- jobmarket.offers offer_made and response should be same type, boolean
-- http://stackoverflow.com/questions/9556474/how-do-i-automatically-update-a-timestamp-in-postgresql
-- http://stackoverflow.com/questions/22746741/trigger-for-checking-value-before-inserting-updating-postgresql
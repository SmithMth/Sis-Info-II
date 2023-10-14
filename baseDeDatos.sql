
CREATE SEQUENCE assignament_idassignament_seq;

CREATE TABLE assignament (
                idAssignament NUMERIC NOT NULL DEFAULT nextval('assignament_idassignament_seq'),
                name BYTEA NOT NULL,
                CONSTRAINT assignament_pk PRIMARY KEY (idAssignament)
);


ALTER SEQUENCE assignament_idassignament_seq OWNED BY assignament.idAssignament;

CREATE SEQUENCE student_id_student_seq;

CREATE TABLE student (
                id_student INTEGER NOT NULL DEFAULT nextval('student_id_student_seq'),
                name VARCHAR NOT NULL,
                lastName VARCHAR NOT NULL,
                e-mail VARCHAR NOT NULL,
                CONSTRAINT student_pk PRIMARY KEY (id_student)
);


ALTER SEQUENCE student_id_student_seq OWNED BY student.id_student;

CREATE SEQUENCE homework_id_homework_seq;

CREATE TABLE homework (
                id_homework INTEGER NOT NULL DEFAULT nextval('homework_id_homework_seq'),
                id_student INTEGER NOT NULL,
                idAssignament NUMERIC NOT NULL,
                title VARCHAR NOT NULL,
                dateOfPresentation DATE NOT NULL,
                CONSTRAINT homework_pk PRIMARY KEY (id_homework, id_student, idAssignament)
);


ALTER SEQUENCE homework_id_homework_seq OWNED BY homework.id_homework;

ALTER TABLE homework ADD CONSTRAINT assignament_homework_fk
FOREIGN KEY (idAssignament)
REFERENCES assignament (idAssignament)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE homework ADD CONSTRAINT student_homework_fk
FOREIGN KEY (id_student)
REFERENCES student (id_student)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
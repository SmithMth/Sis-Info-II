
CREATE TABLE assignament(
    idAssinament SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);


CREATE TABLE student (
    idStudent SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
	lastName TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE homework (
    idHomeWork SERIAL PRIMARY KEY,
    idAssignament INT NOT NULL REFERENCES assignament(idAssinament),
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE
);


CREATE TABLE submission (
    submission_id SERIAL PRIMARY KEY,
    idStudent INT NOT NULL REFERENCES student(idStudent),
    idHomeWork INT NOT NULL REFERENCES homework(idHomeWork),
    comment TEXT,
    submission_date DATE,
    grade FLOAT
);

CREATE TABLE file (
    idFile SERIAL PRIMARY KEY,
    submission_id INT NOT NULL REFERENCES submission(submission_id),
    fileContent BYTEA NOT NULL,
    fileType TEXT NOT NULL
);


CREATE TABLE student_assignament (
    idStudent INT NOT NULL REFERENCES student(idStudent),
    idAssignament INT NOT NULL REFERENCES assignament(idAssinament),
    PRIMARY KEY (idStudent, idAssignament)
);

CREATE TABLE student_homework (
    idStudent INT NOT NULL REFERENCES student(idStudent),
    idHomeWork INT NOT NULL REFERENCES homework(idHomeWork),
    PRIMARY KEY (idStudent, idHomeWork)
);


CREATE OR REPLACE FUNCTION GetNextHomeworks()
RETURNS TABLE (name_student TEXT, title TEXT, email TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT
        e.name,
		t.title,
		e.email
    FROM student_homework et
    JOIN student e ON et.idStudent = e.idStudent
    JOIN homework t ON et.idHomeWork = t.idHomeWork
    WHERE t.due_date >= CURRENT_DATE AND t.due_date <= CURRENT_DATE + INTERVAL '2' DAY;
END;
$$ LANGUAGE plpgsql;
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
    idAssignament INT NOT NULL REFERENCES subject(idassinament),
    PRIMARY KEY (idStudent, idAssignament)
);

CREATE TABLE student_homework (
    idStudent INT NOT NULL REFERENCES student(idStudent),
    idHomeWork INT NOT NULL REFERENCES homework(idHomeWork),
    PRIMARY KEY (idStudent, idHomeWork)
);

CREATE TABLE notes (
    id_notes SERIAL PRIMARY KEY,
    id_student INT REFERENCES student(idStudent),
    idassinament INT REFERENCES subject(idassinament)
    nameN TEXT NOT NULL,
    subjectN TEXT NOT NULL,
    themeN TEXT NOT NULL,
    noteN TEXT NOT NULL,
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

CREATE OR REPLACE FUNCTION insert_note(
    id_student INT,
    idassignment INT,
    nameN TEXT,
    subjectN TEXT,
    theme TEXT,
    note TEXT
) RETURNS void AS $$
BEGIN
    INSERT INTO notes (id_student, idassignment, nameN, subjectN, themeN, noteN)
    VALUES (id_student, idassignment, nameN, subjectN, themeN, noteN);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION is_student_enrolled(
    student_id INT,
    subjectName TEXT
) RETURNS BOOLEAN AS $$
DECLARE
    result BOOLEAN;
BEGIN
    -- Verificar si el estudiante está inscrito en la asignatura
    SELECT EXISTS (
        SELECT 1
        FROM student_assignament sa
        INNER JOIN subject s ON sa.idAssignament = s.idassinament
        WHERE sa.idStudent = student_id AND s.name = subjectName
    ) INTO result;

    RETURN result;
END;
$$ LANGUAGE plpgsql;
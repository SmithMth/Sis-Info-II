CREATE TABLE student (
    idStudent SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
	lastName TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
-- Create the 'materia' table
CREATE TABLE subject (
    idassinament SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    level CHAR(1) CHECK (level IN ('A', 'B', 'C', 'D', 'E')) NOT NULL
);

-- Crear la tabla "subjects_taken" con un valor predeterminado para rfin
CREATE TABLE subjects_taken (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(idStudent),
    subject_id INT REFERENCES subject(idassinament),
    enrollment_year INT NOT NULL,
    first_partial INT CHECK (first_partial >= 0 AND first_partial <= 100),
    second_partial INT CHECK (second_partial >= 0 AND second_partial <= 100),
    final_exam INT CHECK (final_exam >= 0 AND final_exam <= 100),
    final_grade INT,
    rfin VARCHAR(3) DEFAULT 'ABD'
);

CREATE TABLE homework (
    idHomeWork SERIAL PRIMARY KEY,
    idAssignament INT NOT NULL REFERENCES subject(idAssinament),
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
    idAssignament INT NOT NULL REFERENCES subject(idAssinament),
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
    idassinament INT REFERENCES subject(idassinament),
    nameN varchar NOT NULL,
    subjectN varchar NOT NULL,
    themeN varchar NOT NULL,
    noteN varchar NOT NULL
);
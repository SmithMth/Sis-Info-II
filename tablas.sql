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

-- Crear un desencadenador (trigger) para calcular final_grade y establecer rfin
CREATE OR REPLACE FUNCTION calculate_final_grade() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.first_partial IS NOT NULL AND NEW.second_partial IS NOT NULL THEN
        NEW.final_grade = (NEW.first_partial + NEW.second_partial) / 2;
    ELSIF NEW.final_exam IS NOT NULL AND (NEW.final_exam > NEW.first_partial OR NEW.final_exam > NEW.second_partial) THEN
        NEW.final_grade = NEW.final_exam;
    END IF;

    IF NEW.final_grade >= 51 THEN
        NEW.rfin = 'APR';
    ELSE
        NEW.rfin = 'REP';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Asociar el desencadenador a la tabla subjects_taken
CREATE TRIGGER calculate_final_grade_trigger
BEFORE INSERT OR UPDATE ON subjects_taken
FOR EACH ROW
EXECUTE FUNCTION calculate_final_grade();


-- Crear el procedimiento almacenado para obtener las materias y notas de un estudiante
CREATE OR REPLACE FUNCTION get_student_grades(studen_id INT) RETURNS TABLE (
    subject_name VARCHAR(255),
    level CHAR(1),
    enrollment_year INT,
    first_partial INT,
    second_partial INT,
    final_exam INT,
    final_grade INT,
    rfin VARCHAR(3)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        m.name AS subject_name,
        m.level AS level,
        mt.enrollment_year AS enrollment_year,
        mt.first_partial AS first_partial,
        mt.second_partial AS second_partial,
        mt.final_exam AS final_exam,
        mt.final_grade AS final_grade,
        mt.rfin
    FROM
        subjects_taken mt
    INNER JOIN
        subject m ON mt.subject_id = m.idassinament
    WHERE
        mt.student_id = studen_id;  -- Utiliza student_id como variable
END;
$$ LANGUAGE plpgsql;

-- Supongamos que el estudiante con ID 1 está tomando la materia con código 1 en el año 2023, con un primer parcial de 85 y un segundo parcial de 90.
INSERT INTO subjects_taken (student_id, subject_id, enrollment_year, first_partial, second_final_exam)
VALUES (1, 1, 2023, 40, 90);

INSERT INTO subjects_taken (student_id, subject_id, enrollment_year, first_partial, second_final_exam)
VALUES (1, 2, 2023, 85, 90);

INSERT INTO subjects_taken (student_id, subject_id, enrollment_year, first_partial, second_final_exam)
VALUES (1, 3, 2023, 85, 90);


-- Table: Exams
CREATE TABLE Exams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Table: Questions
CREATE TABLE Questions (
    id SERIAL PRIMARY KEY,
    exam_id INT REFERENCES Exams(id),
    question_text VARCHAR(255) NOT NULL
);

-- Table: Options
CREATE TABLE Options (
    id SERIAL PRIMARY KEY,
    question_id INT REFERENCES Questions(id),
    option_text VARCHAR(255) NOT NULL,
    is_checked BOOLEAN NOT NULL
);


CREATE OR REPLACE FUNCTION save_exam(
    exam_name VARCHAR(255), 
    questions_and_options JSONB
)
RETURNS VOID LANGUAGE plpgsql AS $$
DECLARE 
    new_exam_id INT;
    question_record JSONB;
    new_question_id INT;
    option_record JSONB;
BEGIN
    -- Insertar nuevo examen y obtener su ID
    INSERT INTO Exams(name) VALUES(exam_name) RETURNING id INTO new_exam_id;

    -- Loop a través de cada pregunta
    FOR question_record IN SELECT * FROM jsonb_array_elements(questions_and_options->'questions')
    LOOP
        -- Insertar nueva pregunta y obtener su ID
        INSERT INTO Questions(exam_id, question_text) 
        VALUES (new_exam_id, question_record->>'text') 
        RETURNING id INTO new_question_id;
        
        -- Loop a través de cada opción para la pregunta actual
        FOR option_record IN SELECT * FROM jsonb_array_elements(question_record->'options')
        LOOP
            -- Insertar nueva opción
            INSERT INTO Options(question_id, option_text, is_checked)
            VALUES(new_question_id, option_record->>'text', (option_record->>'is_checked')::BOOLEAN);
        END LOOP;
    END LOOP;
END; $$;

CREATE OR REPLACE FUNCTION get_exam(new_exam_id INT)
RETURNS JSONB LANGUAGE plpgsql AS $$
DECLARE
    exam_data JSONB := '{}'::JSONB;
    questions_data JSONB;
    options_data JSONB;
BEGIN
    -- Obtener datos del examen
    SELECT jsonb_build_object('id', id, 'name', name) 
    INTO exam_data 
    FROM Exams 
    WHERE id = new_exam_id;
    
    -- Obtener preguntas del examen
    SELECT jsonb_agg(jsonb_build_object('id', id, 'question_text', question_text))
    INTO questions_data
    FROM Questions
    WHERE exam_id = new_exam_id;

    -- Agregar preguntas al objeto del examen
    exam_data := jsonb_set(exam_data, '{questions}', questions_data);

    -- Iterar a través de cada pregunta para obtener las opciones
    FOR i IN 0..jsonb_array_length(questions_data) - 1 LOOP
        SELECT jsonb_agg(jsonb_build_object('id', id, 'option_text', option_text, 'is_checked', is_checked))
        INTO options_data
        FROM Options
        WHERE question_id = (questions_data->i->>'id')::INTEGER;

        -- Agregar opciones a la pregunta correspondiente
        exam_data := jsonb_set(exam_data, array['questions', i::text, 'options'], options_data);
    END LOOP;

    RETURN exam_data;
END; $$;

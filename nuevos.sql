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

CREATE OR REPLACE FUNCTION get_exams_list()
RETURNS TABLE(id INT, name VARCHAR(255)) LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT id, name FROM Exams;
END; $$;

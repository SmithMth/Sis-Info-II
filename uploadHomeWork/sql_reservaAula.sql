CREATE TABLE Classroom (
    classroomId SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    capacity INT NOT NULL
);

CREATE TABLE Bookings (
    bookingId SERIAL PRIMARY KEY,
    classroomId INT REFERENCES Classroom(classroomId),
    studentId INT REFERENCES student(idstudent), 
    startTime TIMESTAMP NOT NULL,
    endTime TIMESTAMP NOT NULL
);


-- Creación de la tabla de Timeslots
CREATE TABLE Timeslots (
    timeslotId SERIAL PRIMARY KEY,
    startTime TIMESTAMP NOT NULL,
    endTime TIMESTAMP NOT NULL
);

-- Modificación de la tabla de Bookings
ALTER TABLE Bookings DROP COLUMN startTime;
ALTER TABLE Bookings DROP COLUMN endTime;
ALTER TABLE Bookings ADD COLUMN timeslotId INT REFERENCES Timeslots(timeslotId);

ALTER TABLE Timeslots ALTER COLUMN startTime TYPE TIME;
ALTER TABLE Timeslots ALTER COLUMN endTime TYPE TIME;


-- Insertar las 5 aulas predefinidas
INSERT INTO Classroom (name, capacity) VALUES
('Aula 1', 30),
('Aula 2', 25),
('Aula 3', 30),
('Aula 4', 20),
('Aula 5', 35);

-- Insertar los 5 horarios predefinidos (ajusta las horas según lo que necesites)
INSERT INTO Timeslots (startTime, endTime) VALUES
('08:00:00', '10:00:00'),
('10:15:00', '12:15:00'),
('12:30:00', '14:30:00'),
('15:00:00', '17:00:00'),
('17:15:00', '19:15:00');

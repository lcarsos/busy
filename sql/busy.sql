/* Create the primary table for a todo list application */
CREATE TABLE IF NOT EXISTS tasks
(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT,
    description TEXT,
    expected_time INTEGER,      /* This is expected to be garbage, but can sometimes be useful */
    story_points INTEGER,       /* This and expected_time give you a full idea of a task's difficulty */
    remaining_time INTEGER,     /* Optimally, this trends to 0 */
    created_on INTEGER,
    started_on INTEGER,
    completed_on INTEGER,
    worked INTEGER
);

/* This makes it easier to find similar tasks */
CREATE TABLE IF NOT EXISTS tags
(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    name TEXT
);
INSERT INTO tags ( name ) VALUES ( "busy_internal_nc" );

/* For logging time on tasks */
CREATE TABLE IF NOT EXISTS times
(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    started INTEGER,
    amount INTEGER,
    comment TEXT
);

/* Some tasks cannot be started until another is completed */
CREATE TABLE IF NOT EXISTS task_dependencies
(
    task_id INTEGER REFERENCES tasks,
    dependent_on INTEGER REFERENCES tasks
);

/**
 * Sometimes a task proves to be larger than you thought. Break that task out
 * into smaller manageable chunks.
 */
CREATE TABLE IF NOT EXISTS task_part_of
(
    task_id INTEGER REFERENCES tasks,
    part_of INTEGER REFERENCES tasks
);

/**
 * Sometimes you find out that the work you're doing actually works to resolve
 * several tasks on your todo list.
 */
CREATE TABLE IF NOT EXISTS tasks_times
(
    task_id INTEGER REFERENCES tasks,
    time_id INTEGER REFERENCES times
);

CREATE TABLE IF NOT EXISTS tasks_tags
(
    task_id INTEGER REFERENCES tasks,
    tag_id INTEGER REFERENCES tags
);

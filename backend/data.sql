-- SQL program to create a table for projects and insert a sample project

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    tags VARCHAR(255),
    github_url VARCHAR(255),
    demo_url VARCHAR(255)
);

-- Insert a sample project (you can add more rows as needed)
INSERT INTO projects (title, description, tags, github_url, demo_url) VALUES (
    'My First Project',
    'This is a sample project description.',
    'web,react',
    'https://github.com/yourusername/my-first-project',
    'https://myfirstproject.demo.com'
);

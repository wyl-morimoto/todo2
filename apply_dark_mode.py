import sys

with open('frontend/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

replacements = [
    # :root variables
    ('--primary-color: #10b981;', '--primary-color: #34d399;'),
    ('--primary-hover: #059669;', '--primary-hover: #10b981;'),
    ('--bg-color: #f0fdf4;', '--bg-color: #0f172a;'),
    ('--glass-bg: rgba(255, 255, 255, 0.75);', '--glass-bg: rgba(30, 41, 59, 0.75);'),
    ('--glass-border: rgba(255, 255, 255, 0.9);', '--glass-border: rgba(255, 255, 255, 0.1);'),
    ('--text-primary: #1e293b;', '--text-primary: #f8fafc;'),
    ('--text-secondary: #64748b;', '--text-secondary: #94a3b8;'),
    ('--danger-color: #f43f5e;', '--danger-color: #fb7185;'),
    ('--success-color: #10b981;', '--success-color: #34d399;'),
    ('--table-header: rgba(241, 245, 249, 0.85);', '--table-header: rgba(15, 23, 42, 0.85);'),
    ('--row-hover: rgba(16, 185, 129, 0.05);', '--row-hover: rgba(255, 255, 255, 0.05);'),

    # Blobs
    ('background: #86efac;', 'background: #064e3b;'),
    ('background: #7dd3fc;', 'background: #1e3a8a;'),

    # App Container shadow
    ('box-shadow: 0 20px 40px -12px rgba(15, 23, 42, 0.15);', 'box-shadow: 0 20px 40px -12px rgba(0, 0, 0, 0.5);'),

    # App Header border
    ('border-bottom: 1px solid rgba(226, 232, 240, 0.8);', 'border-bottom: 1px solid rgba(255, 255, 255, 0.1);'),
    
    # Sortable hover
    ('background-color: rgba(203, 213, 225, 0.4);', 'background-color: rgba(255, 255, 255, 0.05);'),

    # Tabs background
    ('background: rgba(148, 163, 184, 0.15);', 'background: rgba(0, 0, 0, 0.2);'),
    ('background: #ffffff;', 'background: rgba(255, 255, 255, 0.1);'), # Tab active background (and others, we'll fix general ones)

    # Table wrapper
    ('background: rgba(255, 255, 255, 0.5);', 'background: rgba(30, 41, 59, 0.5);'),

    # Input hover
    ('background: rgba(255, 255, 255, 0.6);', 'background: rgba(255, 255, 255, 0.05);'),
    
    # Checkmark
    ('background-color: #ffffff;', 'background-color: transparent;'),
    
    # Add Task container
    ('background: rgba(255, 255, 255, 0.6);', 'background: rgba(30, 41, 59, 0.6);'),
    
    # Mobile Modal
    ('background: rgba(255, 255, 255, 0.95);', 'background: rgba(30, 41, 59, 0.95);'),

    # Borders
    ('border-bottom: 2px solid rgba(226, 232, 240, 0.8);', 'border-bottom: 2px solid rgba(255, 255, 255, 0.1);'),
    ('border-bottom: 1px solid rgba(226, 232, 240, 0.6);', 'border-bottom: 1px solid rgba(255, 255, 255, 0.05);'),
    ('border: 1px solid rgba(203, 213, 225, 0.8);', 'border: 1px solid rgba(255, 255, 255, 0.1);'),
]

for old, new in replacements:
    css = css.replace(old, new)

# Special cases
css = css.replace('background: #ffffff;\n    border-color: var(--primary-color);', 'background: rgba(15, 23, 42, 0.9);\n    border-color: var(--primary-color);')
css = css.replace('background-color: #ffffff;\n    color: var(--text-primary);', 'background-color: #1e293b;\n    color: var(--text-primary);')

with open('frontend/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated successfully.")

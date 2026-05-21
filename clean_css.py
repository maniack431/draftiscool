with open('sass/main.scss', 'r') as f:
    lines = f.readlines()

ranges_to_delete = [
    (3, 24),
    (148, 158),
    (230, 327),
    (445, 461),
    (645, 707)
]

# Convert to 0-indexed and mark for deletion
delete_indices = set()
for start, end in ranges_to_delete:
    for i in range(start - 1, end):
        delete_indices.add(i)

new_lines = []
for i, line in enumerate(lines):
    if i not in delete_indices:
        new_lines.append(line)

with open('sass/main.scss', 'w') as f:
    f.writelines(new_lines)

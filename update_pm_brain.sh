mkdir -p ~/.claude/skills && \
  curl -L https://github.com/dieterprovoost/pm-brain/archive/refs/heads/main.tar.gz | \
  tar xz --strip-components=3 -C ~/.claude/skills pm-brain-main/.claude/skills/*
mkdir -p ~/.claude/rules && \
  curl -L https://github.com/dieterprovoost/pm-brain/archive/refs/heads/main.tar.gz | \
  tar xz --strip-components=3 -C ~/.claude/rules pm-brain-main/.claude/rules/*
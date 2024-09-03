#!/bin/sh

# Function to check if a file exists
check_file_exists() {
  if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found!"
    exit 1
  fi
}

replace_placeholders() {
  sed -e "s|{{repository}}|$REPOSITORY|g" \
      -e "s|{{current_branch}}|$CURRENT_BRANCH|g" \
      "$1"
}

# Navigate to the repository root
cd $(git rev-parse --show-toplevel)

# Get the current branch name
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
REPOSITORY="cuvis.sdk"

LOGO="readme/logo.md"
HEADER="readme/header.md"
FOOTER="readme/footer.md"
README_IN="README.in"

# Check if files exist
check_file_exists "$LOGO"
check_file_exists "$HEADER"
check_file_exists "$FOOTER"
check_file_exists "$README_IN"

# Generate README.md
{
  replace_placeholders "$LOGO"
  printf "# $REPOSITORY\n"
  replace_placeholders "$HEADER"
  printf "\n"
  replace_placeholders "$README_IN"
  printf "\n"
  replace_placeholders "$FOOTER"
} > README.md

THIS_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$THIS_DIR"

pytest -v ./

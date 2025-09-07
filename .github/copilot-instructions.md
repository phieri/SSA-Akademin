# SSA-Akademin KonCEPT LaTeX Project
KonCEPT för amatörradiocertifikat is a Swedish amateur radio certification book written in LaTeX. The project produces PDF and EPUB versions of the book using a comprehensive LaTeX toolchain.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively
- Bootstrap, build, and test the repository:
  - `sudo apt update`
  - `sudo apt install git make texlive texlive-extra-utils texlive-lang-european texlive-science texlive-fonts-recommended texlive-fonts-extra latexmk chktex`
  - `cd SSA-Akademin/`
  - `make koncept.pdf` -- takes 1-2 minutes to complete. NEVER CANCEL. Set timeout to 5+ minutes.
- Run code quality checks:
  - `chktex -v1 -n8 -n13 -n24 -n32 --output chktex.log koncept.tex` -- takes 10-20 seconds. NEVER CANCEL.
  - `make images_linked.txt` -- generates report of linked images
  - `make images_unlinked.txt` -- generates report of unlinked images  
  - `make long_lines.txt` -- finds lines longer than 80 characters
- Clean build artifacts:
  - `make clean` -- removes all generated files
- EPUB build (experimental and problematic):
  - `make koncept.epub` -- takes 10+ minutes and may fail with index errors. NEVER CANCEL. Set timeout to 20+ minutes.

## Docker Alternative
- Build Docker image (first time only):
  - `make docker-image` -- takes 6-8 minutes. NEVER CANCEL. Set timeout to 15+ minutes.
- Run Docker build:
  - `make docker-build` -- runs make all inside container. May need to run twice for success.

## Validation
- Always manually validate the generated PDF by checking file size and page count.
- Expected output: koncept.pdf with ~354 pages and ~10MB file size.
- ALWAYS run code quality checks before making changes: `chktex` and `make long_lines.txt`.
- ALWAYS run `make clean` followed by `make koncept.pdf` to ensure clean builds after changes.
- The build creates extensive auxiliary files (.aux, .log, .toc, etc.) - these are normal.

## Common Tasks
The following are outputs from frequently run commands. Reference them instead of viewing, searching, or running bash commands to save time.

### Repository Structure
```
SSA-Akademin/
├── .devcontainer/          # GitHub Codespaces configuration
├── .github/                # GitHub workflows and contribution guides
├── images/                 # Image assets (PDF format)
├── koncept/                # LaTeX chapter files
├── macros/                 # Custom LaTeX macros
├── koncept.tex             # Main LaTeX document
├── koncept.bib             # Bibliography
├── Makefile                # Build system
├── Dockerfile              # Container build definition
├── BUILD.md                # Build instructions
├── CONTRIBUTING.md         # Contribution guidelines
├── texifiering.md          # LaTeX formatting rules
└── VERSION.txt             # Current version (3.0.0-pre)
```

### Make Targets
```bash
make help                   # Show available targets
make all                    # Build both PDF and EPUB
make koncept.pdf           # Build PDF (recommended)
make koncept.epub          # Build EPUB (experimental)
make clean                 # Remove generated files
make docker-image          # Build Docker image
make docker-build          # Build using Docker
make images_linked.txt     # Report linked images (311 currently)
make images_unlinked.txt   # Report unlinked images (612 currently)
make long_lines.txt        # Report lines >80 chars (932 currently)
make comment_lines.txt     # Report comment-only lines
make TODOs                 # Generate TODO report
```

### LaTeX Formatting Standards
- Follow texifiering.md for all LaTeX formatting rules
- Use `\emph{}` for emphasis, not italic markup
- Include English translations: `\emph{strömtransformator} (eng. \emph{current transformer})`
- Use `\qty{1}{\joule}` for units with siunitx package
- Use `\num{250000}` for large numbers
- Index key terms: `\index{transformator!ström-}`
- Break lines at sentence boundaries for better diffs
- Keep lines under 80 characters
- Use hard tabs for indentation

### Critical Timing Information
- **PDF Build**: 1-2 minutes (tested and validated)
- **EPUB Build**: 10+ minutes, often fails with index errors
- **Docker Image Build**: 6-8 minutes (first time only)
- **Docker Build**: 1-3 minutes (may need two attempts)
- **Dependency Installation**: 3-5 minutes
- **Code Quality Checks**: 10-30 seconds

### Known Issues and Workarounds
- EPUB build fails with index processing errors - this is a known limitation
- Docker builds may fail on first attempt due to missing auxiliary files - run twice
- chktex reports warnings (exit code 2) but no errors - this is expected
- Long lines report shows 932 lines >80 chars - follow texifiering.md to fix when editing

### GitHub Actions Context
- CI builds on Ubuntu 24.04 with 30-minute timeout for PDF, 60-minute timeout for EPUB
- Uses Swedish locale: `sv_SE.UTF-8`
- Generates versioned filenames: `koncept.3.0.0-pre+b12345.abc1234.pdf`
- Optimizes PDFs with qpdf for smaller file sizes
- Runs code analysis with chktex and image reporting

### Development Environment
- GitHub Codespaces supported via .devcontainer configuration
- Uses same Dockerfile as build system
- Automatically runs `make help` on container startup
- VS Code extensions: editorconfig support

### File Locations
- Main document: `koncept.tex`
- Chapter files: `koncept/chapter*.tex`, `koncept/*.tex`
- Images: `images/**/*.pdf` (PDF format preferred)
- Bibliography: `koncept.bib`
- Build output: `koncept.pdf`, `koncept.log`
- Quality reports: `chktex.log`, `images_*.txt`, `long_lines.txt`

### Important Notes
- **NEVER CANCEL builds or long-running commands** - builds may take several minutes
- Always use appropriate timeouts: 5+ minutes for PDF, 20+ minutes for EPUB, 15+ minutes for Docker
- The repository contains 3 main components: LaTeX source, image assets, and build system
- Current version is 3.0.0-pre (pre-release of version 3)
- Book generates ~354 pages in final PDF format
- Project uses Swedish language and formatting conventions
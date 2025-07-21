# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-ipaplots is a matplotlib style package that provides IPA (Innovations for Poverty Action) themed plotting styles for Python. It's a complete port of the Stata ipaplots package to Python/matplotlib with working examples and comprehensive documentation.

## Build and Installation Commands

This project uses `just` (command runner) for common tasks. All commands should be run with `just`:

```bash
# Setup development environment (first time)
just get-started

# Install in development mode
uv pip install -e .

# Build package
just build-package

# Install from built package
just install-package

# Test CLI functionality (when implemented)
just test-cli

# Clean build artifacts
just clean-build

# Full development workflow
just package-workflow
```

### Alternative uv commands (without just):
```bash
# Install in development mode
uv pip install -e .

# Build with uv
uv build

# Install with uv
uv pip install .
```

## Project Architecture

### Package Structure ✅ COMPLETED
- `src/ipaplots/`: Main Python package
  - `__init__.py`: Package initialization with style registration
  - `ipaplots.py`: Main module (empty - ready for utility functions)
  - `styles/ipaplots.mplstyle`: Complete matplotlib style sheet with IPA styling

### Examples & Data ✅ COMPLETED
- `examples/`: Complete working examples
  - `demo_plots.py`: Comprehensive script generating all 9 plot types
  - `data/ipaplots_test_data.dta`: Original Stata test data
  - `output/`: Generated plot images (ignored by git)

### Original Resources (Reference)
- `ipaplots/`: Contains the original Stata implementation
  - `scheme-ipaplots.scheme`: Original Stata color scheme (ported ✅)
  - `ipaplots_test.do`: Stata test file (recreated in Python ✅)
  - `ipaplots_test_data.dta`: Test data (used in examples ✅)
  - `graphs/`: Reference images for comparison

### Configuration Files
- `pyproject.toml`: Package configuration with uv build backend
- `Justfile`: Command runner for development tasks
- `.gitignore`: Comprehensive Python package gitignore
- `PLAN.md`: Original development plan (mostly completed)

## Development Status

### Completed Features ✅
1. **Complete matplotlib style** with IPA color palette (15 colors)
2. **Style registration** - works with `plt.style.use('ipaplots')`
3. **Working examples** - all 9 plot types from Stata version
4. **Real data integration** - uses actual Stata test data
5. **Arial font styling** - clean sans-serif typography
6. **uv build system** - modern Python packaging
7. **Comprehensive documentation** - README, examples, comments

### Future Enhancements (Not Yet Implemented)
- CLI interface for style management
- Utility functions for common plot types
- Color palette accessor functions
- Additional plot templates
- Unit tests

## Key Implementation Details

### Style Configuration
- **Font**: Arial (sans-serif) for all text elements
- **Colors**: 15 IPA brand colors converted from RGB to hex
- **Grid**: Subtle gray gridlines, clean white background
- **Line styles**: Solid for first 8 colors, dashed for remaining 7

### Working Examples
The `examples/demo_plots.py` script generates 9 plot types:
1. Scatter plot (var2 vs var5)
2. Line graph (var2 over time by group)
3. Pie chart (var1 sums by group)
4. Box plot (all 5 variables)
5. Histogram (var3 with percentage scale)
6. Horizontal bar (means of all variables)
7. Density plots (overlapping areas)
8. Range plots (error bars)
9. By graphs (subplots by group)

### Justfile Common Patterns
- Use `just get-started` for initial setup
- Use `just build-package` instead of `uv build` directly
- Use `just install-package` for testing installations
- Use `just package-workflow` for complete test/build/verify cycle
- Environment managed via `uv sync` and `.venv/`
- Cross-platform support for Windows/Linux/macOS

### Development Workflow
1. Make code changes
2. Run `just install-package` to test locally
3. Run examples: `cd examples && uv run python demo_plots.py`
4. Use `just package-workflow` for complete verification
5. Check generated plots in `examples/output/`

## Testing the Package

```bash
# Test installation and examples
just install-package
cd examples
uv run python demo_plots.py

# Verify plots are generated in examples/output/
# Compare with reference images in ipaplots/graphs/
```

## Publishing (When Ready)

```bash
# Test on TestPyPI first
just publish-test

# Publish to PyPI
just publish
```
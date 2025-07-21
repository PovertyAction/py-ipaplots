# py-ipaplots

A matplotlib style package for creating IPA-themed plots. This package provides a custom matplotlib style that matches the visual identity of Innovations for Poverty Action (IPA).

## Features

- **IPA Color Palette**: 15 carefully selected colors matching IPA's branding
- **Arial Font**: Clean sans-serif font for all text elements
- **Clean Design**: White background with subtle gridlines
- **Consistent Styling**: Uniform appearance across all plot types

## Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/PovertyAction/ipaplots.git
cd py-ipaplots

# Install with uv (recommended)
uv pip install .

# Or install with pip
pip install .
```

### For Development

```bash
# Install in editable mode
uv pip install -e .

# Or with pip
pip install -e .
```

## Usage

### Basic Usage

```python
import matplotlib.pyplot as plt
import ipaplots

# Option 1: Use the style for all plots
plt.style.use("ipaplots")

# Option 2: Use the style context manager
with plt.style.context("ipaplots"):
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()

# Option 3: Load style explicitly
ipaplots.load_style()
```

### Example: Creating a Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np
import ipaplots

# Use IPA style
plt.style.use("ipaplots")

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Example Line Plot')
plt.legend()
plt.show()
```

## Supported Plot Types

The ipaplots style works with all matplotlib plot types:

- **Scatter plots**: `plt.scatter()`
- **Line plots**: `plt.plot()`
- **Bar charts**: `plt.bar()`, `plt.barh()`
- **Histograms**: `plt.hist()`
- **Box plots**: `plt.boxplot()`
- **Pie charts**: `plt.pie()`
- **Area/Density plots**: `plt.fill_between()`
- **Subplots**: `plt.subplots()`

## Color Palette

The package includes 15 distinct colors optimized for data visualization:

1. Primary Green: `#49AC57`
2. Dark Green: `#155240`
3. Light Blue: `#84D0D4`
4. Navy Blue: `#2E4085`
5. Orange: `#F26529`
6. Light Purple: `#BE9FFA`
7. Yellow: `#F5CB57`
8. Dark Blue: `#032B6C`
9. Medium Blue: `#5566B0`
10. Light Blue: `#A0A9EA`
11. Light Orange: `#FC9757`
12. Dark Orange: `#C8420A`
13. Dark Red: `#730000`
14. Forest Green: `#2B754A`
15. Gray: `#C9C9C8`

## Examples

The package includes comprehensive examples demonstrating all plot types from the original Stata implementation:

```bash
# Install the package first
uv pip install .

# Run the demo script
cd examples
uv run python demo_plots.py
```

This will generate 9 different plot types in the `examples/output/` directory:

1. **scatter_plot.png** - Basic scatter plot
2. **line_graph.png** - Multi-group line plot with legend
3. **pie_chart.png** - Pie chart with percentages
4. **box_plot.png** - Box plot for multiple variables
5. **histogram.png** - Histogram with percentage scale
6. **hbar.png** - Horizontal bar chart with value labels
7. **density.png** - Overlapping density plots
8. **range_graphs.png** - Range plots with error bars
9. **bygraphs.png** - Grouped box plots (subplots)

All examples use the actual test data from the original Stata package (`ipaplots_test_data.dta`).

## Development

### Requirements

- Python >= 3.7
- matplotlib (core dependency)
- pandas (required for examples with Stata data)
- ipykernel (for Jupyter support)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/PovertyAction/ipaplots.git
cd py-ipaplots

# Install in development mode
uv pip install -e .

# Run examples to test
cd examples
uv run python demo_plots.py
```

### Building

This package uses the uv build backend:

```bash
# Build wheel and source distribution
uv build

# Install from built wheel
uv pip install dist/*.whl
```

### Project Structure

```
py-ipaplots/
├── src/ipaplots/
│   ├── __init__.py              # Package initialization & style registration
│   ├── ipaplots.py              # Main module (future utility functions)
│   └── styles/
│       └── ipaplots.mplstyle    # Matplotlib style sheet
├── examples/
│   ├── demo_plots.py            # Comprehensive plotting examples
│   └── data/
│       └── ipaplots_test_data.dta  # Original Stata test data
├── ipaplots/                    # Original Stata package (reference)
├── pyproject.toml               # Package configuration
└── README.md
```

## Status

This package is currently in **development** (v0.0.1). The core matplotlib style is complete and functional, but additional utility functions and CLI tools are planned for future releases.

### What's Working ✅
- Complete matplotlib style with IPA color palette and typography
- Style registration (`plt.style.use("ipaplots")`)
- Comprehensive examples with all plot types
- Real Stata test data integration
- uv build system support

### Planned Features 🚧
- Utility functions for common plot types
- Command-line interface for style management
- Color palette accessor functions
- Additional plot templates

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Based on the original Stata ipaplots scheme by Kelly Montaño and Ronny M. Condor.

## Support

- **Repository**: https://github.com/PovertyAction/py-ipaplots
- **Issues**: https://github.com/PovertyAction/py-ipaplots/issues
- **Organization**: [Innovations for Poverty Action](https://www.poverty-action.org/)

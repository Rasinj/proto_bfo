# Contributing to Proto BFO

Thank you for your interest in contributing to Proto BFO! This document provides guidelines and instructions for contributing.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Protocol Buffers compiler (`protoc`)
- Git

### Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rasinj/proto_bfo.git
   cd proto_bfo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e ".[dev]"
   ```

3. **Compile proto files**
   ```bash
   python setup.py build
   ```

4. **Run tests**
   ```bash
   pytest tests/ -v
   ```

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, protobuf version)
- **Code samples** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When suggesting an enhancement:

- **Use a clear and descriptive title**
- **Provide detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **Provide examples** of how it would be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes**
3. **Add tests** for new functionality
4. **Ensure tests pass** (`pytest tests/`)
5. **Update documentation** as needed
6. **Commit with clear messages**
7. **Submit pull request**

#### Pull Request Guidelines

- Follow the existing code style
- Write clear commit messages
- Include tests for new features
- Update documentation
- One feature/fix per pull request

## Development Guidelines

### Code Style

- **Python**: Follow PEP 8
  - Use `black` for formatting: `black examples/ tests/`
  - Use `isort` for imports: `isort examples/ tests/`
  - Use `flake8` for linting: `flake8 examples/ tests/`

- **Proto files**: Follow [Protocol Buffers Style Guide](https://developers.google.com/protocol-buffers/docs/style)
  - Use snake_case for field names
  - Use CamelCase for message names
  - Include comments for all messages and fields

### Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Use pytest fixtures for common test setup

### Documentation

- Update relevant documentation
- Add docstrings to Python functions
- Add comments to proto files
- Include examples for new features

## Project Structure

```
proto_bfo/
├── proto/
│   ├── core/           # Core BFO definitions
│   ├── common/         # Common utilities (units, identifiers, references)
│   └── domains/        # Domain-specific extensions
├── examples/           # Example code
├── tests/
│   ├── unit/          # Unit tests
│   └── integration/   # Integration tests
├── docs/              # Documentation
└── tools/             # Development tools
```

## Creating Domain Extensions

When adding a new domain extension:

1. **Create proto file** in appropriate `proto/domains/` subdirectory
2. **Import core BFO** and common utilities
3. **Extend BFO concepts** rather than creating parallel hierarchies
4. **Document thoroughly** with comments
5. **Create examples** in `examples/<domain>/`
6. **Write tests** in `tests/`
7. **Add domain guide** in `docs/domain_guides/`

Example structure:

```protobuf
syntax = "proto3";

package protobuf_world.domains.yourdomain;

import "proto/core/bfo_core.proto";
import "proto/common/units.proto";
import "proto/common/identifiers.proto";

// Your domain messages here
message YourEntity {
    MaterialEntity base_entity = 1;
    // Domain-specific fields
}
```

## Commit Messages

Follow these guidelines for commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Example:
```
Add disease progression tracking to biomedical domain

- Implement DiseaseState message
- Add temporal tracking of disease stages
- Include severity classification

Fixes #123
```

## Review Process

1. **Automated checks** must pass (CI/CD)
2. **Code review** by maintainers
3. **Testing** by reviewers if needed
4. **Approval** and merge

## Community

- Be respectful and constructive
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)
- Ask questions in issues or discussions
- Help others when you can

## Questions?

If you have questions about contributing:

- Open an issue with the "question" label
- Check existing documentation in `docs/`
- Review closed issues for similar questions

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Acknowledgments

Contributors will be acknowledged in the project README and release notes.

Thank you for contributing to Proto BFO!
